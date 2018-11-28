#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
using namespace std;

static char codeJam[] = "welcome to code jam";

int recCount(string & line, int linePos, int codeJamPos) {
	if(codeJamPos == sizeof(codeJam) - 1)
		return 1;
	int nextPos = linePos;
	int total = 0;
	while(true) {
		nextPos = line.find(codeJam[codeJamPos], nextPos);
		if(nextPos == string::npos)
			return total;
		total = (total + recCount(line, nextPos++, codeJamPos + 1)) % 10000;
	}
}

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	ofstream out;
	out.open(outFileName.c_str());
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int N;
	
	paramsStream >> N;
	
	for(int lineNum = 0; lineNum < N; lineNum++) {
		out << "Case #" << lineNum + 1 << ": ";
		string line;
		getline(in, line);
	
		out << setfill('0') << setw(4) << recCount(line, 0, 0) << endl;
	
	}
	
	string dummy;
	getline(cin, dummy);
    return 0;
}
