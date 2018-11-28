#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	int wordCounter = 0;
	int alienCounter = 0;

	string line;
	ifstream myfile("A-large.in");

	ofstream outfile;
  	outfile.open ("A-large.out");
	
	getline(myfile, line);
	string::size_type space = line.find_first_of(" ");
	string Lstring = line.substr(0, space);
	line = line.substr(space + 1, line.length());
	space = line.find_first_of(" ");
	string Dstring = line.substr(0, space);
	line = line.substr(space + 1, line.length());
	space = line.find_first_of(" ");
	string Nstring = line.substr(0, space);

	stringstream sd(Dstring);
	int D;
	sd >> D;
	stringstream sl(Lstring);
	int L;
	sl >> L;
	stringstream sn(Nstring);
	int N;
	sn >> N;

	string dictionary[D];
	string alienWord;
	string matchCharSet;
	int i, j, k;
	int dictIndex;
	bool match[D];
	bool truthMatch[D];
	int matchCount;

	for(wordCounter = 0; wordCounter < D; wordCounter ++ ) {
		getline(myfile,line);
		dictionary[wordCounter] = line;
		match[wordCounter] = true;
		truthMatch[wordCounter] = true;
	}

	for(alienCounter = 0; alienCounter < N; alienCounter++) {		
		getline (myfile,alienWord);
		dictIndex = 0;
		// iterate through characters
		for(i = 0; i < alienWord.length(); i++) {
			// special matching case
			if(alienWord.at(i) == '(') {
				string::size_type endParen = alienWord.substr(i, alienWord.length()).find_first_of(")");
				matchCharSet = alienWord.substr(i + 1, endParen - 1);			

				// if the dictIndex doesn't match, set the match to false
				for(j = 0; j < D; j++) { 
					if(match[j] == true && matchCharSet.find(dictionary[j].at(dictIndex)) == string::npos) {
						match[j] = false;
					}
				}
				i = endParen + i;
			} else {
				// single car found if it doesn't match, set match to false
				for(j = 0; j < D; j++) { 
					if(match[j] == true && dictionary[j].at(dictIndex) != alienWord.at(i)) {
						match[j] = false;
					}
				}
			}
			dictIndex ++;
		}	
		if(dictIndex == dictionary[0].length()) {
			matchCount = 0;	
			for(wordCounter = 0; wordCounter < D; wordCounter ++ ) {
				if(match[wordCounter] == true) {
					matchCount++;
				}
			}
			cout << "Case #" << alienCounter + 1 << ": " << matchCount << endl;
			outfile << "Case #" << alienCounter + 1 << ": " << matchCount << endl;
		} else {
			cout << "Case #" << alienCounter + 1 << ": 0" << endl;
			outfile << "Case #" << alienCounter + 1 << ": 0" << endl;
		}
		for(k = 0; k < D; k++) {
			match[k] = true;
		}
	}

	myfile.close();

	return 0;
}
