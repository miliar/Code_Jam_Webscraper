#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cctype>

using std::cout;
using std::endl;
using std::ios;
using std::ifstream;
using std::ofstream;
using std::stringstream;
using std::string;
using std::getline;

int PrintUsage(void);

int main(int argc, char* argv[]) {
	if(argc < 3)
		return PrintUsage();

	string infile = argv[1], outfile = argv[2];
	string line;
	int numOfTestCases(0), testCase(1);

	ifstream ifs(infile.c_str(), ios::in);
	ofstream ofs(outfile.c_str(), ios::out);

	getline(ifs, line);
	numOfTestCases = atoi(line.c_str());
	
	while(testCase <= numOfTestCases) {
		getline(ifs, line);
		stringstream ss(line);
		int N(0), S(0), p(0), count(0), score(0);
		int qualified(0), unqualified(0), tbd(0), suprising(0);
		ss >> N >> S >> p;
		while(count < N) {
			ss >> score;
			if(score < p * 3 - 4) {
				++unqualified;
				if(score > 1)
					++suprising;
			}
			else if(score >= p * 3 - 2) {
				++qualified;
				++suprising;
			}
			else 
				++tbd;
			++count;
		}

		int total = qualified;
		if(tbd > S)
			total += S;
		else if (suprising > S)
			total += tbd;
		else
			total += suprising - S;

		cout << "Case #" << testCase << ": " << total << endl;
		ofs << "Case #" << testCase << ": " << total << endl;
		++testCase;
	}

	ifs.close();
	ofs.close();

	return 0;
}

int PrintUsage(void) {
	cout << "Usage\n\tDancingWithTheGooglers.exe [infile] [outfile]" << endl;
	return 0;
}