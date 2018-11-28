#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>
#include <limits>
#include <algorithm>
#include <iomanip>

typedef unsigned int uint;
typedef long long ll;

struct TestInput {
	struct P {
		ll pos;
		ll count;
	};
	ll dist;
	std::vector<P> p;
};

typedef double TestOutput;

struct Part {
	double pos, size;
	double time;
	Part() { }
	Part(TestInput::P p, ll dist) {
		pos = (double)p.pos;
		size = 0.5*p.count * dist;
		time = 0.5*(p.count-1) * dist;
	}
	double left() const { return pos-size; }
	double right() const { return pos+size; }
	static Part merge(Part p1, Part p2) {
		double maxTime = std::max(p1.time, p2.time);
		p1.pos -= maxTime-p1.time;
		double dist = p2.left() - p1.right();
		if (dist>0) {
			dist = std::min(dist, maxTime-p2.time);
			p2.pos -= dist;
		} else {
			double p2Dist = std::min(-dist, maxTime-p2.time);
			p2.pos += p2Dist;
			p2.time += p2Dist;
			dist = p2.left() - p1.right();
			if (dist<0) {
				p1.pos += 0.5*dist;
				p2.pos -= 0.5*dist;
				maxTime -= 0.5*dist;
			}
		}
		Part res;
		res.pos = 0.5*(p1.left()+p2.right());
		res.size = 0.5*(p2.right()-p1.left());
		res.time = maxTime;
		return res;
	}
};

static TestOutput runTest(const TestInput &in) {
	Part part(in.p[0], in.dist);
	for (uint i=1; i<in.p.size(); i++)
		part = Part::merge(part, Part(in.p[i], in.dist));
	return part.time;
}

static void readEx() {
	throw std::runtime_error("error reading input");
}

static void writeEx() {
	throw std::runtime_error("error reading input");
}

static std::istream &operator>>(std::istream &fi, TestInput &in) {
	uint c;
	fi >> c >> in.dist;
	in.p.resize(c);
	for (uint i=0; i<c; i++)
		fi >> in.p[i].pos >> in.p[i].count;
	return fi;
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
		fo << "Case #" << (i+1) << ": " << std::setprecision(12) << output[i] << std::endl;
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
