#pragma comment (linker, "/STACK:128000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

struct node
{
	double w;
	string f;
	node *l, *r;
};

string tree;
int l;
char buf[1000];
set<string> feats;
node *root;
vector<string> data;
int p;

node *recparse()
{
	p++; // (
	node *t = new node();
	sscanf(data[p].c_str(), "%lf", &t->w);
	p++;
	if (data[p] == ")")
	{
		t->l = 0;
		t->r = 0;
	}
	else
	{
		t->f = data[p];
		p++;
		t->l = recparse();
		t->r = recparse();
	}
	p++; // )
	return t;
}

void parse()
{
	SS ss;
	for (int i = 0; i < tree.size(); i++)
		if (tree[i] == '(')
			ss << " ( ";
		else if (tree[i] == ')')
			ss << " ) ";
		else 
			ss << tree[i];
	string s;
	data.clear();
	while (ss >> s)
		data.PB(s);
	p = 0;
	root = recparse();
}

double go(node *v, double p)
{
	p *= v->w;
	if (v->l == 0)
		return p;
	if (feats.count(v->f) > 0)
		return go(v->l, p);
	else
		return go(v->r, p);
}

void solvecase() {
	scanf("%d\n", &l);
	tree = "";
	for (int i = 0; i < l; i++)
	{
		gets(buf);
		tree += string(buf);
	}
	parse();
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", buf);
		int k;
		scanf("%d", &k);
		feats.clear();
		for (int j = 0; j < k; j++)
		{
			scanf("%s", buf);
			feats.insert(string(buf));
		}
		double res = go(root, 1.0);
		printf("%.8lf\n", res);
	}
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d:\n", i+1);
		solvecase();
		//printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}