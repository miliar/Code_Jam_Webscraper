#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

int T;
int N, B;
char buf[100000];
set<string> PS;

struct Tree
{
	string s;
	double v;
	Tree *l, *r;
	~Tree() {
		delete l;
		delete r;
	}
	double solve (double _p) {
		if (s.empty()) return _p * v;
		if (PS.find (s) != PS.end())
			return l->solve (_p*v);
		else
			return r->solve (_p*v);
	}
};

string line;
int pos = 0;
Tree* root;

void make_tree (Tree* _root) {
	char ch, buf[64], l = 0;
	string pr = "";
	double val;
	while ((ch = line[pos++]) != '(');
	while ((ch = line[pos++]) == ' ');
	
	buf[l++] = ch;
	while (isdigit((ch = line[pos++])) || ch == '.')
		buf[l++] = ch;
	buf[l++] = 0;
	sscanf (buf, "%lf", &val);
	l = 0;
	pos--;
	
	while ((ch = line[pos++]) == ' ');
	if (ch >= 'a' && ch <= 'z') {
		buf[l++] = ch;
		while (isalpha (ch = line[pos++]))
			buf[l++] = ch;
		buf[l++] = 0;
		pr = string(buf);
	}
	pos--;

	if (pr.empty()) {
		while ((ch = line[pos++]) != ')');
		pos--;
		_root->l = _root->r = NULL;
		_root->s = "";
		_root->v = val;
	}
	else {
		_root->s = pr;
		_root->v = val;
		_root->l = new Tree();
		_root->r = new Tree();
		make_tree (_root->l);
		make_tree (_root->r);
	}
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt+", stdout);

	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		if (tc == T-1) {
			cerr << "";
		}
		scanf ("%d\n", &N);
		pos = 0;
		line = "";
		for (int i = 0; i < N; i++) {
			gets (buf);
			line += string (buf);
			line += " ";
		}
		line += " ";
		root = new Tree();
		make_tree (root);

		printf ("Case #%d:\n", tc+1);

		scanf ("%d\n", &B);
		for (int i = 0; i < B; i++)
		{
			PS.clear();
			string name, pi;
			cin >> name;
			int k;
			cin >> k;
			for (int j = 0; j < k; j++) {
				cin >> pi;
				PS.insert (pi);
			}
			double res = root->solve (1);
			printf ("%.7lf\n", res);
		}
		
		delete root;
	}	
	
	return 0;
}