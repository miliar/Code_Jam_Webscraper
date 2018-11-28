#include <iostream>
#include <fstream>
using namespace std;

bool isnum(char inp) {
	return (inp == '0' || inp == '1' || inp == '2' || inp == '3' || inp == '4' || inp == '5' || inp == '6'
	 || inp == '7' || inp == '8' || inp == '9');
}

int main() {
	// Loads known input text into memory
	string input = "input.txt";
	//cout << "Input File: ";
	//cin >> input;
	//cout << input << "\n";
	string contentsInp = "";
	if (1) {
		ifstream STREAM(input.c_str());
		string line = "";
		while (STREAM.good()) {
			getline(STREAM, line);
			line.push_back('*');
			contentsInp.append(line);
		}
		STREAM.close();
	}
	
	// Loads pre-found output file into memory
	string output = "output.txt";
	//cout << "Output File: ";
	//cin >> output;
	//cout << output << "\n";
	string contentsOut = "";
	if (1) {
		ifstream STREAM(output.c_str());
		string line = "";
		while (STREAM.good()) {
			getline(STREAM, line);
			line.push_back('*');
			contentsOut.append(line);
		}
		STREAM.close();
	}
	
	
	char alpha[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
					, 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	char newAlpha[26]
	               = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
	                , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
	// Translates the text based on the input and output files
	for (unsigned int i = 0; i < contentsInp.length() && i < contentsOut.length(); i++) {
		if (!isalpha(contentsInp[i]) && !isnum(contentsInp[i])) continue;
		for (int a = 0; a < 26; a++) {
			if (contentsOut[i] == alpha[a] && newAlpha[a] == ' ') {
				newAlpha[a] = contentsInp[i];
				break;
			}
		}
	}
	// Process of elimination for the last one (if there is a last one)
	for (int i = 0; i < 26; i++) {
		if (newAlpha[i] == ' ') {
			bool onlyOne = true;
			for (int a = 0; a < 26; a++) {
				if (newAlpha[a] == ' ' && a != i) onlyOne = false;
			}
			if (onlyOne == true) {
				char lastChar = ' ';
				for (int a = 0; a < 26; a++) {
					bool foundChar = false;
					for (int b = 0; b < 26; b++) {
						if (alpha[a] == newAlpha[b]) foundChar = true;
					}
					if (foundChar == false) {
						lastChar = alpha[a];
						break;
					}
				}
				if (lastChar != ' ') {
					newAlpha[i] = lastChar;
					break;
				}
			}
		}
	}
	
	// Display what the alphabet corresponds to
	/*cout << "Our Alphabet: \n";
	for (unsigned int i = 0; i < 26; i++) {
		cout << alpha[i] << "  ";
	}
	cout << "\n\nGooglerese: \n";
	for (unsigned int i = 0; i < 26; i++) {
		cout << newAlpha[i] << "  ";
	}
	cout << "\n";*/
	
	// Load google text into memory
	string newContents = "";
	if (1) {
		ifstream STREAM("googlerese.txt");
		string line = "";
		while (STREAM.good()) {
			getline(STREAM, line);
			line.push_back('*');
			newContents.append(line);
		}
		STREAM.close();
	}
	
	// Output the translated text into the output file
	ofstream OUTPUT("googleOut.txt");
	bool newCase = true;
	int curCase = 1;
	bool outputText = false;
	for (unsigned int i = 0; i < newContents.length(); i++) {
		if (newContents[i] == '*') {
			if (i < newContents.length()-1) {
				if (outputText == true) {
					curCase++;
					OUTPUT << "\n";
					cout << "\n";
					newCase = true;
				} else {
					newCase = false;
				}
			}
			continue;
		}
		else if (newContents[i] == ' ') { cout << " "; OUTPUT << " "; continue; }
		else {
			if (newCase == true) {
				OUTPUT << "Case #" << curCase << ": ";
				cout << "Case #" << curCase << ": ";
			}
			bool outputEd = false;
			for (int a = 0; a < 26; a++) {
				if (newAlpha[a] == newContents[i] && isalpha(newContents[i])) {
					cout << alpha[a];
					OUTPUT << alpha[a];
					outputText = true;
					outputEd = true;
					break;
				}
			}
			newCase = false;
		}
	}
	OUTPUT.close();
}

