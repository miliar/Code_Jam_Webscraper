#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

struct node {
	double f;
	string n;
	node *l, *r;
};

double getProb(node *n, set<string> &f)
{
	double prob = 1;
	node *p = n;

	while (p) {
		prob *= p->f;
		if (f.find(p->n) != f.end()) {
			p = p->l;
		} else
			p = p->r;
	}

	return prob;
}


node* buildTree(string s) {
	int p = 0, i1, i2, d;
	double w;
	
	while (p < s.size() && s[p] != '(') ++p;

	if (p >= s.size()) return 0;

	++p;
	while (!isdigit(s[p]) && s[p] != '.') ++p;
	i1 = p;
	while (isdigit(s[p]) || s[p] == '.') ++p;
	i2 = p;

	sscanf(s.substr(i1, i2-i1).c_str(), "%lf", &w);

	while (!isalpha(s[p]) && s[p] != ')') ++p;

	if (s[p] == ')') {
		node *n = new node;
		n->f = w;
		n->l = n->r = 0;
		n->n = "";
		return n;
	} else {
		node *n = new node;
		n->f = w;
		i1 = p;
		while (isalpha(s[p])) ++p;
		i2 = p;
		n->n = s.substr(i1, i2-i1);

		while (s[p] != '(') ++p;
		i1 = p;
		++p; d = 1;

		while (d > 0) {
			if (s[p] == '(') ++d;
			if (s[p] == ')') --d;
			++p;
		}
		i2 = p;

		n->l = buildTree(s.substr(i1,i2-i1));

		while (s[p] != '(') ++p;
		i1 = p;
		++p; d = 1;

		while (d > 0) {
			if (s[p] == '(') ++d;
			if (s[p] == ')') --d;
			++p;
		}
		i2 = p;

		n->r = buildTree(s.substr(i1,i2-i1));

		return n;
	}

	return 0;
}

int main()
{
	int n, tc, nLines, na, nf;
	string s, ss;

	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fin >> n;

	REP(tc,n) {
		fout <<"Case #"<<tc+1<<":"<<endl;	

		fin >> nLines;
		getline(fin, s);

		ss = "";
		REP(i,nLines) {
			getline(fin,s);
			ss.append(s);
		}

		node *t = buildTree(ss);

		fin >> na;

		string name;
		set <string> feats;
		REP(i,na) {
			fin >> name;
			fin >> nf;
			feats.clear();
			REP(j,nf) {
				fin >> name;
				feats.insert(name);
			}
			fout << getProb(t, feats) << endl;
		}		
	}

	fin.close();
	fout.close();

	return 0;
}

