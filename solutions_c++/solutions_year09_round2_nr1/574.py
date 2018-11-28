#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <memory.h>
using namespace std;
#pragma warning (disable:4996)

typedef long long int64;
#define ll(x) ((long long)(x))


string t, s;

struct node {
	double v;
	string fe;
	node *v1, *v2;
};
int pos = 0;

bool numc(char c) {
	if (c=='.') return true;
	return (c>='0' && c<='9');
}

node *parse() {
	while (!numc(s[pos])) pos++;
	string t;
	while (numc(s[pos])) { t+=s[pos]; pos++; };
	node *d = new node;
	d->v = atof(t.c_str());
	while (s[pos]==' ') pos++;
	if (s[pos]==')') {
		pos++;
		return d;
	}
	t="";
	while (s[pos]>='a' && s[pos]<='z') { t+=s[pos]; pos++; }
	d->fe = t;
	d->v1 = parse();
	d->v2 = parse();
	while (s[pos]!=')') pos++;
	pos++;
	return d;
}

set<string> ft;

double dfs(node *d) {
	double res = d->v;
	if (d->fe.length() == 0) return res;
	if (ft.count( d->fe ) > 0)
		res *= dfs( d->v1 );
	else
		res *= dfs( d->v2 );
	return res;
}

int main() {
	ifstream cin("data.in");
	ofstream cout("data.out");
	//freopen(".in", "r", stdin);
	//freopen(".out", "w", stdout);
	int qqqq,l;
	cin >> qqqq;
	cout.precision(7);
	for (int i=0; i<qqqq; i++) {
		cout << "Case #" << i+1 << ":"<<endl;
		cin >> l;
		s = "";
		getline(cin, t);
		for (int j=0; j<l; j++) {
			getline(cin, t);
			s+=t;
		}
		pos = 0;
		node *root = parse();
		cin >> l;
		for (int j=0; j<l; j++) {
			string nm, ff;
			int cc;
			cin >> nm >> cc;
			ft.clear();
			for (int k=0; k<cc; k++) {
				cin >> ff;
				ft.insert(ff);
			}
			cout << fixed << dfs(root) << endl;
		}
	}


	return 0;
}