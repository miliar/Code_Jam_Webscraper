#include "contestIO.h"
#include <fstream>

#include <iostream>

#define MAX_LINE_LENGTH 10000

vector<string> splitLine(string line, char splitChar) {
	vector<string> split;

	size_t loc = line.find_first_of(splitChar);
	while(loc != string::npos) {
		split.push_back(line.substr(0, loc));
		line = line.substr(loc + 1, string::npos);
		loc = line.find_first_of(splitChar);
	}

	if(line.at(0) != ' ')
		split.push_back(line);

	return split;
}

// Reader
fileReader::fileReader(string name) {
	inFile.open(name.c_str());

	if(!inFile.is_open())
		cout << "Unable to open file: " << name << "\n";
}

string fileReader::getLine() {
	char *s = new char[MAX_LINE_LENGTH];
	inFile.getline(s, MAX_LINE_LENGTH);
	string line(s);
	delete s;

	return line;
}

bool fileReader::opened() {
	return inFile.is_open();
}

bool fileReader::eof() {
	return inFile.eof();
}

fileReader::~fileReader() {
	inFile.close();
}


// Writer
fileWriter::fileWriter(string name) {
	ifstream inFile;
	inFile.open(name.c_str());

	bool goOn;
	do {
		goOn = true;
		if(inFile.is_open()) {
			inFile.close();
			if (remove(name.c_str()) != 0) {
				cout << name << " exists, but unable to delete.\n";
				goOn = false;
				name = name.append("_");
				inFile.open(name.c_str());
			}
		}
	}while(!goOn);

	outFile.open(name.c_str());
	usedName = name;
}

void fileWriter::writeLine(string line) {
	outFile << line;
	if(line.at(line.length() - 1) != '\n')
		outFile << endl;
}

void fileWriter::write(string toWrite) {
	outFile << toWrite;
}


fileWriter::~fileWriter() {
	outFile.close();
}