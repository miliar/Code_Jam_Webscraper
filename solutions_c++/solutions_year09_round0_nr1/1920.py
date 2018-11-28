#include <iostream>
#include <fstream>
#include <cstdlib> // for exit function
#include <algorithm>
#include <math.h>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int l;
int d;
int n;
vector<char*> words;
vector<char*> patterns;

bool match(char* pattern, char* word) {
	int k = 0;
	bool ok = true;
	int wsize = l + 1;
	for (int i = 0; i < wsize; i++) {
		if (i == l) {
			if (ok)
				break;
			else {
				//cout << "Match between " << word << " and " << pattern << " break at the end, no match" << endl;
				return false;
			}
		}
		if (!ok) {
			//cout << "Match between " << word << " and " << pattern << " break early, no match" << endl;
			return false;
		}
		ok = false;
		if (pattern[k] == '(') {
			int endpos = k + 1;
			for (; pattern[endpos] != ')'; endpos++);
			for (int j = k; j < endpos; j++) {
				if (pattern[j] == word[i]) {
					ok = true;
					break;
				}
			}
			k = endpos + 1;
		} else {
			if (pattern[k] == word[i])
				ok = true;
			k++;
		}
	}
	//cout << "Match between " << word << " and " << pattern << " found match" << endl;
	return true;
}

void solve(ofstream& outdata) {
	for (int i = 0; i < n; i++) {
		char* pattern = patterns[i];
		int count = 0;
		cout << "Progress: " << i << " out of " << n << endl;
		for (int j = 0; j < d; j++) {
			char* w = words[j];
			if (match(pattern, w))
				count++;
		}
		outdata << "Case #" << (i + 1) << ": " << count << endl;
	}
}

int main() {
	ifstream indata; // indata is like cin
	ofstream outdata;
	indata.open("A-small.in"); // opens the file
	outdata.open("A-small.out");
	if(!indata) { // file couldn't be opened
		cerr << "Error: file could not be opened" << endl;
		exit(1);
	}
	indata >> l;
	indata >> d;
	indata >> n;

	words.reserve(d);
	patterns.reserve(n);

	for (int i = 0; i < d; i++) {
		char* c = new char[l + 1];
		memset(c, 0, sizeof(char) * (l + 1));
		indata >> c;
		words.push_back(c);
	}
	for (int i = 0; i < n; i++) {
		char* c = new char[l * d + 1];
		memset(c, 0, sizeof(char) * (l * d + 1));
		indata >> c;
		patterns.push_back(c);
	}

	solve(outdata);
	
	outdata.close();

	return 0;
}