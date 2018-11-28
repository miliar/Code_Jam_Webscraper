#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

typedef vector<string> message;

message parsemessage(string s);
bool match(message m, string s);

int main() {
	ifstream fin("codejama.in");
	ofstream fout("codejama.out");

	int N,D,L;
	fin>>L>>D>>N;

	vector<string> dict(D);
	for (int i = 0; i < D; i++)
		fin>>dict[i];

	message m; string s;
	int out;
	for (int i = 0; i < N; i++) {
		out=0;
		fin>>s;
		m=parsemessage(s);
		for (int j = 0; j < D; j++)
			if (match(m,dict[j])) out++;
		fout << "Case #" << i+1 << ": " << out << "\n";
	}
	return 0;
}

message parsemessage(string s) {
	message ret;
	int j;
	for (int i = 0; i < s.length(); i++) {
		if (s[i]=='(') {
			for (j=0;s[i+j]!=')';j++);
			ret.push_back(s.substr(i+1,j-1));
			i+=j;
		}
		else {
			ret.push_back(s.substr(i,1));		
		}
	}

	return ret;
}

bool contains(string s, char c) {
	for (int i = 0; i < s.length(); i++)
		if (s[i]==c) return true;
	return false;
}

bool match(message m, string s) {
	for (int i = 0; i < s.length(); i++) {
		if (!contains(m[i],s[i])) return false;
	}
	return true;
}
