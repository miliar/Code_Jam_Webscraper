// includes + defines {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define FORD(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int)((x).size()))
#define DEBUG(x) { cout << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;
// }}}

struct Node{
	map<string, Node*> ch;
};

int cnt;

void insert(Node *x, char *path){
	if(*path == '\0')
		return;

	string cur = "";

	int i;
	for(i = 1; path[i] && path[i] != '/'; ++i)
		cur += path[i];

	if(x->ch.count(cur) == 0){
		x->ch[cur] = new Node;
		++cnt;
	}

	insert(x->ch[cur], path + i);
}

void destroy(Node *x){
	FORE(i, x->ch){
		destroy(i->second);
		delete i->second;
	}
}

char buf[1024];

int main(){
	int T;
	scanf("%d", &T);
	FOR(qi, 1, T){
		int N, M;
		scanf("%d %d", &N, &M);
		Node *root = new Node;

		while(N--){
			scanf("%s", buf);
			insert(root, buf);
		}

		cnt = 0;
		while(M--){
			scanf("%s", buf);
			insert(root, buf);
		}

		printf("Case #%d: %d\n", qi, cnt);

		destroy(root);
		delete root;
	}
}
