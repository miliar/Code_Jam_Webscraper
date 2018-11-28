#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
	ifstream inFile;
	int numberOfLines;
	string inputStrings[31];

	inFile.open("A-small-attempt3.in");
	if (!inFile) {
		cout << "Unable to open input file.";
	} else {
		string noLines;
		getline(inFile, noLines);
		numberOfLines = atoi(noLines.c_str());
		
		int index = 0;
		while (!inFile.eof()) {
			getline(inFile, inputStrings[index]);
			index++;
		}
	}
	inFile.close();

	string decoderString = "bhxmlgvprtwfceokidsnb";

	ofstream outFile("A-small-attempt3.out");

	for (int n = 0; n < numberOfLines; n++) {
		string inputString = inputStrings[n];
		outFile<<"Case #"<<n+1<<": ";
		for (int i = 0; i < inputString.length(); i++) {
			int n = decoderString.find(inputString[i]);

			if (n!=string::npos) {
				outFile << decoderString[n+1];
			} else if (inputString[i] == 'a') {
				outFile<<'y';
			} else if (inputString[i] == 'y') {
				outFile<<'a';
			} else if (inputString[i] == 'j') {
				outFile<<'u';
			} else if (inputString[i] == 'u') {
				outFile<<'j';
			} else if (inputString[i] == 'z') {
				outFile<<'q';
			} else if (inputString[i] == 'q') {
				outFile<<'z';
			} else if (inputString[i] == ' '){
				outFile<<' ';
			} else {
				;
			}
		}

		if (n!=numberOfLines-1) 
			outFile<<endl;
	}

	return 0;
}