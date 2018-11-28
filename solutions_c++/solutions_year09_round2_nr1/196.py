#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "aa";

struct node {
	node * l;
	node * r;
	double p;
	string f;

	node(node * tl = 0, node * tr = 0, double tp = 0, string tf = "") {
		l = tl;
		r = tr;
		p = tp;
		f = tf;
	}
};

char buf[100000];
char bufs[100000];
char bbuf[100000];

node * parse(string & text, int & pos) {
	node * ret;
	
	while (!isdigit(text[pos])) {
		pos++;
	}
	double p;
	sscanf(buf + pos, "%lf", &p);
//	cerr << p << endl;
	while (!isalpha(text[pos]) && text[pos] != ')') {
		pos++;
	}
	string f = "";
	if (isalpha(text[pos])) {
		sscanf(buf + pos, "%s", bufs);
		f = (string)bufs;
	}

	while (text[pos] != '(' && text[pos] != ')') {
		pos++;
	}
	if (text[pos] == ')') {
		ret = new node(0, 0, p, f);
	} else {
		ret = new node(parse(text, pos), parse(text, pos), p, f);
	}
	return ret;
}

double getp(node * cur, string & name, set<string> & f) {
	if (cur == 0) {
		return 1.0;
	}
	double ret = cur->p;
	if (cur->f != "" && f.count(cur->f)) {
		ret *= getp(cur->l, name, f);
	} else {
		ret *= getp(cur->r, name, f);
	}
	return ret;
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": " << endl;
		
		int lines;
		scanf("%d\n", &lines);
		string text = "";
		for (int i = 0; i < lines; i++) {
			gets(bbuf);
			text = text + " " + (string)(bbuf);
		}
//		cerr << text << endl;
//		cerr << "HERE0" << endl;

//		cerr << text.length() << endl;
		memset(buf, 0, sizeof(buf));
//		cerr << "HERE1" << endl;
		memcpy(buf, text.c_str(), text.length());
		int tpos = 0;
//		cerr << "HERE2" << endl;
		
		node * root = parse(text, tpos);
//		cerr << "HERE3" << endl;


		int q;
		scanf("%d\n", &q);
		for (int i = 0; i < q; i++) {
			string name;
			int fn;
			cin >> name >> fn;
			set<string> fs;
			for (int j = 0; j < fn; j++) {
				string cur;
				cin >> cur;
				fs.insert(cur);
			}
			printf("%.12lf\n", getp(root, name, fs));
		
//			cerr << name << endl;
		}
//		cerr << "HERE3" << endl;

	}

	return 0;
}
