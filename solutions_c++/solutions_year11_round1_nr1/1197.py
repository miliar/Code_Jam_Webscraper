#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::string;
using std::vector;

typedef pair<long long, pair<int, int> > TestCase;

vector<TestCase> ParseInput(const string& filename) {
	vector<TestCase> cases;

	std::ifstream fin;
	fin.open(filename.c_str(), std::ifstream::in);
	if (fin.fail()) {
		cout << "Failed to open " << filename << endl;
		return cases;
	}

	int num_cases;
	fin >> num_cases;
	for (int i = 0; i < num_cases; ++i) {
		long long n;
		int pd, pg;
		fin >> n >> pd >> pg;
		TestCase testcase(n, std::make_pair(pd, pg));
		cases.push_back(testcase);
	}

	fin.close();

	return cases;
}

bool AnalyzeTestCase(const TestCase& testcase) {
	
	long long N = testcase.first;
	int PD = testcase.second.first;
	int PG = testcase.second.second;

	// 0 <= G * PG - D * PD <= 100 * (G - D)
	// -> PG * G >= PD * D
	// -> (100 - PG) * G >= (100 - PD) * D
	// G >= D
	// G * PG % 100 == 0
	// D * PD % 100 == 0

	if (PG == 0 && PD > 0)
		return false;

	if (100 - PG == 0 && 100 - PD > 0)
		return false;

	if (N < 100) {
		for (long long D = 1; D <= N; ++D) {
			if (D * PD % 100 == 0)
				return true;
		}
		return false;
	}
	
	return true;
}

int main(int argc, char** argv) {

	vector<TestCase> cases = ParseInput(string(argv[1]));

	std::ofstream fout;
	fout.open("output.txt",std::ofstream::out);
	if (fout.fail()) {
		cout << "Failed to open output.txt for writing." << endl;
		return 1;
	}

	int num_cases = cases.size();
	for (int i = 0; i < num_cases; ++i) {
		bool feasible = AnalyzeTestCase(cases[i]);
		string output = feasible ? "Possible" : "Broken";
		fout << "Case #" << i+1 << ": " << output << endl;
	}

	fout.close();

	return 0;
}