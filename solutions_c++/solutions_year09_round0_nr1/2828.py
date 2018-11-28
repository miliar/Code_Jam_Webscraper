#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int L, D;

class DictNode {
public:
	DictNode* c[26];
	DictNode();
	void add(string& w, int i = 0);
};

DictNode::DictNode() {
	memset(c, NULL, sizeof(c));
}

void DictNode::add(string& w, int i) {
	if(i == L)
		return;
	int p = w.at(i) - 'a';
	if(c[p] == NULL)
		c[p] = new DictNode();
	c[p]->add(w, i + 1);
}

DictNode dict;
	DictNode* list[75000];

int calculatePossibities(string& pattern) {
	int p = 0;
	int head = 0, tail = 0;
	list[0] = &dict;
	for(int i=0; i<L; i++) {
		bool possible[26];
		memset(possible, false, sizeof(possible));
		if(pattern.at(p) == '(') {
			p ++;
			while(pattern.at(p) != ')') {
				possible[pattern.at(p) - 'a'] = true;
				p ++;
			}
		}
		else 
			possible[pattern.at(p) - 'a'] = true;
		p ++;

		int current_tail = tail;
		for(; head<=current_tail; head++)
			for(int k=0; k<26; k++)
				if(possible[k] && list[head]->c[k] != NULL)
					list[++tail] = list[head]->c[k];
	}
	return tail - head + 1;
}

int main(int argc, char* argv[]) {
	int n;
	ifstream fin("2009QualA.in");
	fin >>L >>D >>n;
	string w;
	for(int i=0; i<D; i++) {
		fin >>w;
		dict.add(w);
	}
	string pat;
	for(int i=0; i<n; i++) {
		fin >>pat;
		cout <<"Case #" <<i+1 <<": " <<calculatePossibities(pat) <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/