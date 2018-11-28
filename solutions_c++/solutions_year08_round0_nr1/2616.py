//============================================================================
// Name        : SavingtheUniverse.cpp
// Author      : Joel Costa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <iterator>

using namespace std;

int str2int(const string &str) {
	stringstream ss(str);
	int n;
	ss >> n;
	return n;
}

string int2str(int n) {
	stringstream ss;
	ss << n;
	return ss.str();
}

vector<string> readFile() {
	vector<string> returnData;
	string line;
	ifstream inputFile("A small.in"); // Create stream to read
	if (inputFile.is_open()) { // If the file is open
		while ( !inputFile.eof() ) { // While not end of file
			getline(inputFile, line); // To get the next line in the file			
			returnData.push_back(line);
		}
		inputFile.close();
	}
	copy(returnData.begin(), returnData.end(), ostream_iterator<string>(cout,
			"\n"));
	return returnData;
}

int writeFile(string fileName, string data) {
	ofstream outputFile(fileName.c_str());
	if (outputFile.is_open()) {
		outputFile << data;
		outputFile.close();
	} else
		cout << "Unable to open file";
	return 0;
}

int bestEngine(vector<string> engines, vector<string> queries) {
	int engine_pos = -1;
	int query_pos = -1;
	bool has_query = true;
	for (int i = 0; i < engines.size(); i++) {
		has_query = false;;
		for (int j = 0; j < queries.size(); j++) {
			if (engines[i] == queries[j]) {
				if (j > query_pos) {
					engine_pos = i;
					query_pos = j;
				}
				has_query = true;
				break;
			}
		}
		if (!has_query)
			return queries.size();
	}
	return query_pos;
}

int switchNum(vector<string> engines, vector<string> queries) {
	int pos = 1, num = -1;
	if (engines.size() == 0 || queries.size() == 0) {
		return 0;
	}
	while (pos > 0) {
		pos = bestEngine(engines, queries);
		queries.erase(queries.begin(), queries.begin() + pos);
		num++;
	}
	return num-1;
}

int main() {
	vector<string> queries, engines;
	int N, S, Q, c;
	string result, data;
	ifstream inputFile("A small.in"); // Create stream to read
	if (inputFile.is_open()) { // If the file is open
		if ( !inputFile.eof() ) { // While not end of file
			getline(inputFile, data); // To get the next line in the file
			N = str2int(data);
			c = 1;
			while (N > 0) {
				engines.clear();
				queries.clear();
				getline(inputFile, data);
				S = str2int(data);
				cout << "Case #" + int2str(c) + " S: " << S << endl;
				while (S > 0) {
					getline(inputFile, data);
					engines.push_back(data);
					S--;
				}
				getline(inputFile, data);
				Q = str2int(data);
				cout << "Case #" + int2str(c) + " Q: " << Q << endl;
				while (Q > 0) {
					getline(inputFile, data);
					queries.push_back(data);
					Q--;
				}
				result += "Case #" + int2str(c) + ": " + int2str(switchNum(
						engines, queries)) + "\n";
				N--;
				c++;
			}
		}
		inputFile.close();
	}
	writeFile("A small.out", result);
	return 0;
}
