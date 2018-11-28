#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>

typedef unsigned long long ull;

typedef ull TestInput;
typedef ull TestOutput;

const ull N = 1<<20;
bool prime[N];
std::vector<ull> primes;

static TestOutput runTest(TestInput in) {
	ull res = 0;
	if (in==1) return 0;
	for (ull i=0; i<primes.size(); i++) {
		ull maxPow = 0;
		ull prod = 1;
		ull p = primes[i];
		while (prod*p<=in) {
			prod *= p;
			maxPow++;
		}
		if (maxPow==1)
			return res + 1;
		res += maxPow - 1;
	}
	throw std::runtime_error("too few primes");
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
	ull testCount;
	std::istringstream testCountSt(testCountS);
	testCountSt >> testCount;
	if (testCountSt.fail())
		readEx();
	std::vector<TestInput> res(testCount);
	for (ull i=0; i<testCount; i++)
		fi >> res[i];
	return res;
}

static void writeOutput(const char *filename, const std::vector<TestOutput> &output) {
	std::ofstream fo(filename);
	if (fo.fail())
		writeEx();
	for (ull i=0; i<output.size(); i++) {
		fo << "Case #" << (i+1) << ": " << output[i] << std::endl;
		if (fo.fail())
			writeEx();
	}
}

int main(int argc, const char **argv) {
	std::fill(prime, prime+N, true);
	prime[0] = false; prime[1] = true;
	for (ull p=2; p<N; p++) {
		if (prime[p]) {
			primes.push_back((ull)p);
			for (ull k=p*p; k<N; k+=p)
				prime[k] = false;
		}
	}

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
