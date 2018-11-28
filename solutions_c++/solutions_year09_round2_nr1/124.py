#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

char buf[1000000];

struct animal {
	string name;
	set<string> features;
	animal(string s) {
		stringstream ss(s);
		ss >> name;
		int n;
		ss >> n;
		while (n--) {
			string tmp;
			ss>>tmp;
			features.insert(tmp);
		}
	}
};

struct tree {
	double p;
	bool leaf;
	string feature;
	tree *has, *hasnot;
	tree(double p): p(p), leaf(true) {	}
	tree(double p, const string &f, tree *has, tree *hasnot): p(p), feature(f), leaf(false), has(has), hasnot(hasnot) {	}
	double getProb(const animal &a) {
		if (leaf) {
			return p;
		} else {
			return (a.features.count(feature) ? has : hasnot)->getProb(a) * p;
		}
	}
};

void trim(const char  *&s) {
	while (*s == ' ') ++s;
}

tree* buildtree(const char * &s) {
	while (*s != '(') ++s;
	s++;
	trim(s);
	double p;
	sscanf(s, "%lf", &p);
	while (isdigit(*s) || *s == '.') ++s;
	trim(s);
	if (*s == ')') {
		++s;
		return new tree(p);
	} else {
		sscanf(s, "%s", buf);
		string f = buf;
		tree *has = buildtree(s);
		tree *hasnot = buildtree(s);
		while (*s != ')') ++s;
		++s;
		return new tree(p, f, has, hasnot);
	}

	return 0;
}

void solve() {
	int n;
	scanf("%d\n", &n);
	string s;
	for (int i = 0; i < n; ++i) {
		gets(buf);
		s = s + buf + ' ';
	}
	replace(s.begin(), s.end(), '\n', ' ');
	replace(s.begin(), s.end(), '\r', ' ');
	const char *t = s.c_str();
	tree *root = buildtree(t);
	scanf("%d\n", &n);
	for (int i = 0; i < n; ++i) {
		gets(buf);
		animal a(buf);
		printf("%.9lf\n", root->getProb(a));
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d:\n", i+1);
		solve();
	}
}