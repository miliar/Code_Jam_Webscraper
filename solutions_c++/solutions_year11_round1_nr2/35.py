//BEGIN_CUT
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
#include <bitset>
#include <cstring>
#include <sstream>
#include <utility>
#include <queue>
#include <cassert>
using namespace std;

#define X first
#define Y second
#define FI first
#define SE second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }
//END_CUT

struct Node {
	map<LL, Node*> e;

	int bottom;
	int dp;
	int choice;

	Node() {
		bottom = -1;
	}

	~Node() {
		FORE (it, e)
			delete it->ND;
	}

	Node* next(LL v) {
		if (e.find(v) == e.end())
			return e[v] = new Node;
		else
			return e[v];
	}
};

LL hash(VI v) {
	LL ret = 0;
	REP (i, (int)v.size())
		ret = ret * 2131 + v[i] + 1;
	return ret;
}

char p[30];
Node* root;

VI pos[10005][26];
int len[10005];
char word[10005][15];
int n;

void add(int x) {
	Node* cur = root->next(hash(VI(1, len[x])));

	for (int i = 0; i < 26; ++i)
		cur = cur->next(hash(pos[x][p[i]]));

	cur->bottom = x;
}

void dfs(Node* cur) {
	if (cur->bottom != -1) {
		cur->dp = 0;
		cur->choice = cur->bottom;
	} else {
		cur->dp = -1;
		cur->choice = -1;
		FORE (it, cur->e) {
			dfs(it->second);
			if (it->second->dp > cur->dp) {
				cur->dp = it->second->dp;
				cur->choice = it->second->choice;
			} else if (it->second->dp == cur->dp) {
				cur->choice = min(cur->choice, it->second->choice);
			}
		}
		if (cur->e.find(hash(VI())) != cur->e.end() && cur->e.size() > 1) {
			map<LL, Node*>::iterator it = cur->e.find(hash(VI()));
			if (it->second->dp + 1 > cur->dp) {
				cur->dp = it->second->dp + 1;
				cur->choice = it->second->choice;
			} else if (it->second->dp + 1 == cur->dp) {
				cur->choice = min(cur->choice, it->second->choice);
			}
		}
	}
}

void go() {
	scanf("%s", p);
	for (int i = 0; i < 26; ++i)
		p[i] -= 'a';
	root = new Node;
	for (int i = 0; i < n; ++i)
		add(i);
	dfs(root);
	printf(" %s", word[root->choice]);
	delete root;
}

void alg() {
	int m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%s", word[i]);
		for (len[i] = 0; word[i][len[i]]; ++len[i]);
		for (int j = 0; j < len[i]; ++j)
			pos[i][word[i][j] - 'a'].PB(j);
	}
	for (int i = 0; i < m; ++i)
		go();
	for (int i = 0; i < n; ++i) {
		REP (j, 26)
			pos[i][j].clear();
	}
	printf("\n");
}

int main() {
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		printf("Case #%d:", i);
		alg();
	}

    return 0;
}
