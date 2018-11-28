#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

struct node {
	string s;
	node *down, *left;
	node(): s(""), down(NULL), left(NULL) {}
	node(string str): s(str), down(NULL), left(NULL) {}
} *root;

void parseL(char *sss, list<string> &L) {
	int k = strlen(sss);
	string buf = "";
	FOR(i,0,k) {
		if(sss[i] == '/') {
			L.push_back(buf);
			buf = "";
		} else {
			buf += sss[i];
		}
	}
	L.push_back(buf);
	L.pop_front();
}

int Ssize(node *x) {
	if(x == NULL) return 0;
//	printf("***   %s\n", x->s.c_str());
	return Ssize(x->down) + Ssize(x->left) + 1;
}

void clear(node *x) {
	if(x == NULL) return;
	clear(x->down), clear(x->left);
	delete x;
}

int create(int n) {
	FOR(i,0,n) {
		char str[111];
		scanf("%s", str);
		list<string> L;
//printf("%s\n", str);
		parseL(str, L);
//FORE(j,L) printf("%s ", j->c_str());
//printf("\n");
		node *cur = root;
		while(!L.empty()) {
			if(cur->s == L.front()) {
				L.pop_front();
				if(cur->down == NULL && !L.empty()) {
					cur->down = new node(L.front());
				}
				cur = cur->down;
			} else {
				if(cur->left == NULL) {
					cur->left = new node(L.front());
				}
				cur = cur->left;
			}
		}
	}
	return Ssize(root);
}

int N, M;

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) {
		scanf("%d%d", &N, &M);
		root = new node("/");
		int k1 = create(N);
		int k2 = create(M);
		clear(root);
		printf("Case #%d: %d\n", zzz + 1, k2 - k1);
	}
	return 0;
}
