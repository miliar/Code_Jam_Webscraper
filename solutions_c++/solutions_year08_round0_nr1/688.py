#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

const int MAX_S = 10000;
const int MAX_Q = 10000;
const int MAX_V = 1000000;

string searchEngines[MAX_S];
string queries[MAX_Q];
int DP[MAX_S][MAX_Q];
int numSearchE, numQueries;

int go (int searchE, int querie) {
	if (querie == numQueries + 1) return 0;
	if (DP[searchE][querie] != -1) return DP[searchE][querie];
	// change
	if (searchEngines[searchE] == queries[querie]) {
		int best = MAX_V;
		for (int i = 0; i < numSearchE; i++) {
			if (i == searchE) continue;
			best = min(best, go(i, querie + 1));
		}
		DP[searchE][querie] = 1 + best;
		return DP[searchE][querie];
	}
	// not change
	else {
		DP[searchE][querie] = go(searchE, querie + 1);
		return DP[searchE][querie];
	}
}

void print () {
	cout << "Search Engines:" << endl;
	for (int i = 0; i < numSearchE; i++) {
		cout << searchEngines[i] << endl;
	}	
	cout << "Queries" << endl;
	for (int i = 0; i < numQueries; i++) {
		cout << queries[i] << endl;
	}
	cout << endl;
}

int main () {
	string buffer;
	ifstream in("A.in");
	ofstream out("A.out");
	getline(in, buffer, '\n'); 
	int cases = atoi(buffer.c_str());
	for (int c = 0; c < cases; c++) {
		getline(in, buffer, '\n'); 
		numSearchE = atoi(buffer.c_str());
		//cout << numSearchE << endl;;
		for (int i = 0; i < numSearchE; i++) {
			getline(in, buffer, '\n');
			searchEngines[i] = buffer;
			//cout << searchEngines[i] << endl;
		}
		getline(in, buffer, '\n'); 
		numQueries = atoi(buffer.c_str());
		//cout << numQueries << endl;
		for (int i = 0; i < numQueries; i++) {
			getline(in, buffer, '\n');
			queries[i] = buffer;	
			//cout << queries[i] << endl;
		}
		//print();
		int result = MAX_V;
		memset(DP, -1, sizeof(DP));
		for (int i = 0; i < numSearchE; i++) {
			result = min(result, go (i, 0));
		}
		out << "Case #" << (c + 1) << ": " << result << endl;
	}
	in.close();
	out.close();
	system("pause");
}