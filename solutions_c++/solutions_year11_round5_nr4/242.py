#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>
#include <intrin.h>
#include <nmmintrin.h>
#include <limits>

typedef unsigned int uint;
typedef unsigned long long ull;

struct BigInt {
	ull hi, lo;
	void setBit(uint bitIndex) {
		if (bitIndex<64) lo |= ((ull)1)<<bitIndex;
		else hi |= ((ull)1) << bitIndex;
	}
	ull getBit(uint bitIndex) const {
		if (bitIndex<64) return (lo >> bitIndex) & 1;
		else return (hi>>(bitIndex-64)) & 1;
	}
	bool zero() const { return hi==0 && lo==0; }
};

typedef std::string TestInput;
typedef std::string TestOutput;

ull sqrHi(ull x) {
	ull res;
	_umul128(x, x, &res);
	return res;
}

struct Range {
	ull lo, hi;
};

static bool checkAns(BigInt x, BigInt mask, ull y) {
	ull hi, lo;
	lo = _umul128(y, y, &hi);
	return ((lo^x.lo) & (~mask.lo)) == 0 && ((hi^x.hi) & (~mask.hi)) == 0;
}

static ull runHi(BigInt x, BigInt mask) {
	for (uint bit=0; bit<64; bit++) {
		if (((mask.hi>>bit)&1)!=0) {
			BigInt x2 = x, mask2 = mask;
			mask2.hi &= ~(1<<bit);
			ull res1 = runHi(x2, mask2);
			if (res1!=0)
				return res1;
			x2.hi |= ((ull)1<<bit);
			return runHi(x2, mask2);
		}
	}

	ull lo = 0;
	ull hi = std::numeric_limits<ull>::max();
	for (;;) {
		ull m = (lo + (hi-lo)/2);
		ull s = sqrHi(m);
		if (s<x.hi)
			lo = m+1;
		else if (s>x.hi)
			hi = m;
		else break;
	}
	for (ull y=lo; y<=hi; y++) {
		if (checkAns(x, mask, y))
			return y;
	}
	return 0;
}

static ull runLo(BigInt x, BigInt mask) {
	ull res=0;
	uint mask32 = (uint)(mask.lo);
	uint x32 = (uint)(x.lo);
	for (uint y=0; ; ) {
		uint yy = y*y;
		if (((x32^yy) & (~mask32)) == 0) {
			for (ull z=0; ; z += (ull)1 << 32) {
				ull hi, lo;
				ull Y = z + y;
				lo = _umul128(Y, Y, &hi);
				if (((lo^x.lo) & (~mask.lo)) == 0 && ((hi^x.hi) & (~mask.hi)) == 0)
					return Y;
				if (hi>=2*x.hi)
					break;
			}
		}
		if (++y==0) break;
	}
	return res;
}

static TestOutput runTest(const TestInput &in) {
	BigInt x, mask;
	x.hi = 0; x.lo = 0;
	mask.hi = 0; mask.lo = 0;
	for (uint i=0; i<in.size(); i++) {
		uint bitIndex = (uint)(in.size()-i-1);
		switch (in[i]) {
		case '0': break;
		case '1': x.setBit(bitIndex); break;
		default: mask.setBit(bitIndex);
		}
	}

	ull res;
	bool doRunHi = _mm_popcnt_u64(mask.hi)<_mm_popcnt_u64(mask.lo);
	//doRunHi = false;

	if (doRunHi)
		res = runHi(x, mask);
	else
		res = runLo(x, mask);
	if (res==0)
		std::cerr << "not found\n";

	BigInt ans;
	ans.lo = _umul128(res, res, &ans.hi);
	std::string resS; resS.resize(in.size());
	for (uint i=0; i<in.size(); i++) {
		uint bitIndex = (uint)(in.size()-i-1);
		resS[i] = (char)(ans.getBit(bitIndex) + '0');
	}
	return resS;
}

static void readEx() {
	throw std::runtime_error("error reading input");
}

static void writeEx() {
	throw std::runtime_error("error reading input");
}

static std::vector<TestInput> readInput(const char *filename) {
	std::ifstream fi(filename);
	std::string testCountS;
	std::getline(fi, testCountS);
	if (fi.fail())
		readEx();
	uint testCount;
	std::istringstream testCountSt(testCountS);
	testCountSt >> testCount;
	if (testCountSt.fail())
		readEx();
	std::vector<TestInput> res(testCount);
	for (uint i=0; i<testCount; i++)
		fi >> res[i];
	return res;
}

static void writeOutput(const char *filename, const std::vector<TestOutput> &output) {
	std::ofstream fo(filename);
	if (fo.fail())
		writeEx();
	for (uint i=0; i<output.size(); i++) {
		fo << "Case #" << (i+1) << ": " << output[i] << std::endl;
		if (fo.fail())
			writeEx();
	}
}

int main(int argc, const char **argv) {
	try {
		const char *inFilename = argc>=2 ? argv[1] : "in";
		const char *outFilename = argc>=3 ? argv[2] : "out";

		std::vector<TestInput> in = readInput(inFilename);
		std::vector<TestOutput> out(in.size());
		for (unsigned int i=0; i<in.size(); i++) {
			out[i] = runTest(in[i]);
			std::cerr << '\r' << (i+1) << "/" << in.size();
			std::cerr.flush();
		}
		std::cerr << std::endl;
		writeOutput(outFilename, out);
	} catch (const std::exception &ex) {
		std::cerr << "exception: " << ex.what() << std::endl;
		return 1;
	}
	return 0;
}
