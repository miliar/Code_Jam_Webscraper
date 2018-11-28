#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>
#include <utility>
#include <iomanip>
#include <algorithm>

typedef unsigned int uint;

struct TestInput {
	uint S, R, t;
	std::vector<std::pair<uint, uint> > ws;
};

typedef double TestOutput;

static TestOutput runTest(const TestInput &in) {
	double runningTimeLeft = in.t;
	double timeElapsed = 0;
	for (uint i=0; i<in.ws.size(); i++) {
		double wSpeed = in.ws[i].first;
		double dist = in.ws[i].second;
		double runSpeed = in.R + wSpeed;
		double timeToRun = dist / runSpeed;
		if (timeToRun <= runningTimeLeft) {
			runningTimeLeft -= timeToRun;
			timeElapsed += timeToRun;
		} else {
			// run
			timeElapsed += runningTimeLeft;
			double distanceCovered = runningTimeLeft * runSpeed;
			runningTimeLeft = 0;
			// walk
			double distanceLeft = dist - distanceCovered;
			double walkSpeed = in.S + wSpeed;
			timeElapsed += distanceLeft / walkSpeed;
		}
	}
	return timeElapsed;
}

static void readEx() {
	throw std::runtime_error("error reading input");
}

static void writeEx() {
	throw std::runtime_error("error reading input");
}

static std::istream &operator>>(std::istream &fi, TestInput &in) {
	uint X, N;
	fi >> X >> in.S >> in.R >> in.t >> N;
	in.ws.resize(N+1);
	for (uint i=0; i<N; i++) {
		uint b, e, w;
		fi >> b >> e >> w;
		in.ws[i].first = w;
		in.ws[i].second = e - b;
		X -= e - b;
	}
	in.ws.back().first = 0;
	in.ws.back().second = X;
	std::sort(in.ws.begin(), in.ws.end());
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
