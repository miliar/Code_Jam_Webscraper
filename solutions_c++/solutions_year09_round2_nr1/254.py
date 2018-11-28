#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <sstream>
#include <cstring>
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,v) for (int i = 0; i < v.size(); i++)
#define fors(i,s) for (int i = 0; i < s.length(); i++)
#define rep(i,f,t) for (int i = (int)(f); i < (int)(t); i++)
#define per(i,f,t) for (int i = f; i > t; i--)
#define fe(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define ft first
#define sd second
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PIS pair< int, string >
#define VPIS vector< PIS >
#define VPII vector< PII >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pname "domino"
#define pi 3.1415926535
#define have(u,v) (u&(1<<v))
#define maxn 50000
#define inf (1<<20)
#define ll long long
#define maxnm 105
using namespace std;

struct tnode {
	double w;
	string u;
	tnode *l,*r;
};

void parse(tnode* root, string u) {
	root->l = root->r = NULL;
	root->u = "";
	int i = 0;
	
	string v;
	stringstream ss;
	
	ss << u;
	ss >> root->w;
	
	ss >> v;
	if (v.sz != 0)root->u = v.substr(0,v.find("("));
	int d=0;
	
	while (i < u.sz && u[i] != '(')i++;
	if (i == u.sz)return;

	i++;
	d++;
	
	int st=i;
	while (i < u.sz && d > 0) {
		if (u[i]=='(')d++;
		if (u[i]==')')d--;
		i++;
	}

	root->l = new tnode();
	parse(root->l, u.substr(st,i-st));

	while (i < u.sz && u[i] != '(')i++;
	if (i == u.sz)return;

	d=0;
	i++;
	d++;
	
	int sts=i;
	while (i < u.sz && d > 0) {
		if (u[i]=='(')d++;
		if (u[i]==')')d--;
		i++;
	}

	root->r = new tnode();
	parse(root->r, u.substr(sts, i-st));
}

set< string > a[1000];
double dfs(tnode *root, int u, double p) {
	if (root == NULL)return p;
	p *= root->w;
	if (a[u].count(root->u))return dfs(root->l, u, p); 
	else return dfs(root->r, u, p);
}
char buf[1000];
void solve() {
	int l;
	string treestr="";
	cin >> l;
	gets(buf);
	while (l--) {
		gets(buf);
		string u(buf);
		treestr += u;
	}
	int i = 0;
	while (i < treestr.sz && treestr[i] != '(')i++;
	i++;
	int j = treestr.sz-1;
	while (j >= 0 && treestr[j]!=')') {
		j--;
	}
	j--;
	
	tnode *root = new tnode();
	parse(root, treestr.substr(i,j-i+1));

	int n;
	cin >> n;
	forn(i,n) {
		string dummy;
		cin >> dummy;
		a[i].clear();
		int q;
		cin >> q;
		while (q--) {
			string inp;
			cin >> inp;
			a[i].insert(inp);
		}
	}

	forn(i,n) {
		printf("%.6f\n", dfs(root, i,  1.0));
	}
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(i,t) {
		printf("Case #%d:\n",i+1);
		solve();
	}
	return 0;
}	

