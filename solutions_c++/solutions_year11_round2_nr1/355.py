#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <stdexcept>

typedef unsigned int uint;

struct TestInput: public std::vector<std::string> {
};

struct TestOutput: public std::vector<double> {
	TestOutput() { }
	TestOutput(size_t size): std::vector<double>(size) { }
};

	struct Stats {
		uint winCount, gameCount;
		double wp, owp, oowp;
	};

static TestOutput runTest(const TestInput &in) {
	uint n = (uint)in.size();
	std::vector<Stats> stats(in.size());
	for (uint i=0; i<n; i++) {
		stats[i].winCount = 0;
		stats[i].gameCount = 0;
		for (uint j=0; j<n; j++) {
			if (in[i][j]!='.')
				stats[i].gameCount++;
			if (in[i][j]=='1')
				stats[i].winCount++;
		}
		if (stats[i].gameCount==0) {
			std::cerr << "zero!\n";
			stats[i].gameCount = 1;
		}
	}
	for (uint me=0; me<n; me++) {
		stats[me].wp = (double)stats[me].winCount / (double)stats[me].gameCount;
		double owpSum = 0; uint owpCount = 0;
		for (uint other=0; other<n; other++) {
			if (in[me][other]!='.') {
				uint subWin = in[other][me]=='1' ? 1 : 0;
				uint subGame = in[other][me]=='.' ? 0 : 1;
				double owp = (double)(stats[other].winCount-subWin) / (double)(stats[other].gameCount-subGame);
				owpSum += owp;
				owpCount++;
			}
		}
		if (owpCount==0) {
			std::cerr << "zero!\n";
			owpCount = 1;
		}
		stats[me].owp = owpSum/owpCount;
	}
	for (uint me=0; me<n; me++) {
		double oowpSum = 0; uint oowpCount = 0;
		for (uint other=0; other<n; other++) {
			if (in[me][other]!='.') {
				oowpSum += stats[other].owp;
				oowpCount++;
			}
		}
		if (oowpCount==0) {
			std::cerr << "zero!\n";
			oowpCount = 1;
		}
		stats[me].oowp = oowpSum / oowpCount;
	}
	TestOutput res(n);
	for (uint i=0; i<n; i++)
		res[i] = 0.25*stats[i].wp + 0.50*stats[i].owp + 0.25*stats[i].oowp;
	return res;
}

static void readEx() {
	throw std::runtime_error("error reading input");
}

static void writeEx() {
	throw std::runtime_error("error reading input");
}

static std::istream &operator>>(std::istream &fi, TestInput &in) {
	uint n;
	fi >> n;
	in.resize(n);
	for (uint i=0; i<n; i++)
		fi >> in[i];
	return fi;
}

static std::ostream &operator<<(std::ostream &fo, const TestOutput &out) {
	for (uint i=0; i<out.size(); i++)
		fo << std::endl << std::setprecision(12) << out[i];
	return fo;
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
