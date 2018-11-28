#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

#define sz(c) ((int)c.size())
#define pb push_back

struct node {
	double pr;
	string ch;
	node *l, *r;
	node (double p, string c) : pr(p), ch(c) {}
};

map <string, bool> traits;

double calc(node *cur, double res) {
	res *= (cur->pr);
	if ((cur->ch) == "") return res;
	if (traits.count(cur->ch))
		return calc(cur->l, res);
	else return calc(cur->r, res);
}

node* parse(string s) {
	double pr; string tr;
	int x = 0;
	while (s[x] != '(') x++; x++;
	s = s.substr(x);
	stringstream ss(s);
	ss >> pr >> tr;
	if (tr[0] == ')') {
		return new node(pr, "");
	}
	else {
		node *cur = new node(pr, tr);
		x = 0;
		while (s[x] != '(') x++;
		(cur->l) = parse(s.substr(x));
		int cnt = 0;
		x++;
		while (s[x] != ')' || cnt > 0) {
			if (s[x] == '(') cnt++;
			else if (s[x] == ')') cnt--;
			x++;
		} x++;
		(cur->r) = parse(s.substr(x));
		return cur;
	}
}

int main() {
	ifstream fin("A.txt");
	FILE *fout = fopen("A.out", "w");

	int numtests;
	fin >> numtests;
	for (int i = 1; i <= numtests; i++) {
		int L; string t; string s;
		fin >> L;
		getline(fin, t);
		for (int j = 0; j < L; j++) {
			getline(fin, t);
			s += t;
		}

		// maketree
		node *root = parse(s);
		
		int numanimals;
		fin >> numanimals;
		getline(fin, t);
		fprintf(fout, "Case #%d:\n", i);
		for (int j = 0; j < numanimals; j++) {
			string name, tr; int numtraits;
			fin >> name >> numtraits;
			traits.clear();
			for (int k = 0; k < numtraits; k++) {
				fin >> tr; traits[tr] = 1;
			}
			fprintf(fout, "%lf\n", calc(root, 1));
		}
	}

	fin.close();
	fclose(fout);
	return 0;
}


