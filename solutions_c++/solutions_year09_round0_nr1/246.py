#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <numeric>
#include <complex>
#include <utility>
#include <fstream>
#include <ostream>
#include <istream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;


#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define FOR(i,n)	for(int i=0; i<(n); ++i)


struct Node {
	bool tag; Node *t[26];
}z[300000];  int zn=0;
Node root;
typedef Node *NodePtr;

void insert(char *s) {
	NodePtr p = &root;
	while(*s) {
		if(p->t[*s-'a'] == NULL) {
			p->t[*s-'a'] = z + zn;
			memset(z+zn, 0, sizeof(Node));
			++zn;
		}
		p = p->t[*s-'a'];
		++s;
	}
	p->tag = true;
}

int  L, D, N;
int  adj[128][128], deg[128];

int cnt(NodePtr p, int k) {
	int cc=0;
	if(k == L) {
		if(p->tag) return 1;
		return 0;
	}
	for(int i=0, c; i<deg[k]; ++i) {
		c = adj[k][i]-'a';
		if(p->t[c] == NULL) continue;
		cc += cnt(p->t[c], k+1);
	}
	return cc;
}

int calc(char *s) {
	CLR(deg, 0);
	int  i, j, k;
	for(i=0, j=0, k=1; s[j]; ++j) {
		if(s[j] == '(') k=0;
		if(islower(s[j])) {
			adj[i][deg[i]++] = s[j];
			i += k;
		}
		if(s[j] == ')') ++i, k=1;
		if(i > L) break;
		//putchar(s[j]);
		//if(k) putchar('\n');
	}
	if(i>L) return 0;
	return cnt(&root, 0);
}


char *input_file = "E:/google/CodeJam/CodeJam/A-large.in";
char *output_file = "E:/google/CodeJam/CodeJam/A-large.out";
const bool zzzz = true;

int main() {
	if(zzzz) {freopen(input_file, "r", stdin);freopen(output_file, "w", stdout);}
	scanf("%d%d%d", &L, &D, &N);
	char  cs[1024];
	CLR(&root, 0);
	while(D--) {
		scanf("%s", cs);
		insert(cs);
	}
	int  i=0;
	for(i=1; i<=N; ++i) {
		scanf("%s", cs);
		printf("Case #%d: %d\n", i, calc(cs));
	}
	return 0;
}

