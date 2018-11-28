#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char ** argv){
	string sub = "yhesocvxduiglbkrztnwjpfmaq";
	int numCases;
	ifstream inFile;
	inFile.open(argv[1]);

	ofstream outFile;
	outFile.open(argv[2]);
	inFile >> numCases;
	inFile.ignore();
	for (int i = 1; i <= numCases; i++){
		string line, plain;
		getline(inFile, line);
		int len = line.length();
		for (int j = 0; j < len; j++){
			char curr = line[j];
			if (curr == ' '){
				plain += ' ';
				continue;
			}
			curr -= 97;
			plain += sub[curr];
		}
		outFile << "Case #" << i << ": " << plain << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
