#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <assert.h>
#include <math.h>
using namespace std;

#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))

int T;
int X, Y;
char zeile[1000];

typedef vector<int> VI;
VI adj[2][10000];

int enc(int x, int y) {
	x = MOD(x, X);
	y = MOD(y, Y);
	return x+X*y;
}

void visdel(int i) {
	int s = 1;
	while(true) {
		if (adj[s][i].size() != 1)
			return;
		int k = adj[s][i][0];
		//printf("del %d %d-%d\n", s, i, k);
		adj[s][i].clear();
		VI neu;
		FOREACH(it, adj[1-s][k]) {
			if (*it != i)
				neu.push_back(*it);
		}
		adj[1-s][k] = neu;
		i = k;
		s = 1-s;
	}
}

bool vis[2][10000];

void viszus(int i) {
	int s = 0;
	while(true) {
		vis[s][i] = true;
		FOREACH(it, adj[s][i]) {
			if (!vis[1-s][*it]) {
				s = 1-s;
				i = *it;
				goto weiter;
			}
		}
		return;
		weiter:;
	}
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		//scanf("%d %d ", &X, &Y);
		gets(zeile);
		sscanf(zeile, "%d %d", &Y, &X);
		for (int i = 0; i < X*Y; i++) {
			adj[0][i].clear();
			adj[1][i].clear();
			vis[0][i] = vis[1][i] = false;
		}
		for (int y = 0; y < Y; y++) {
			//scanf("%s ", zeile);
			gets(zeile);
			for (int x = 0; x < X; x++) {
				//printf("%c\n", zeile[x]);
				if (zeile[x] == '-') {
					adj[0][x+X*y].push_back(enc(x+1,y));
					adj[0][x+X*y].push_back(enc(x-1,y));
				} else if (zeile[x] == '|') {
					adj[0][x+X*y].push_back(enc(x,y+1));
					adj[0][x+X*y].push_back(enc(x,y-1));
				} else if (zeile[x] == '/') {
					adj[0][x+X*y].push_back(enc(x+1,y-1));
					adj[0][x+X*y].push_back(enc(x-1,y+1));
				} else if (zeile[x] == '\\') {
					adj[0][x+X*y].push_back(enc(x+1,y+1));
					adj[0][x+X*y].push_back(enc(x-1,y-1));
				} else {
					assert(false);
				}
			}
		}
		for (int i = 0; i < X*Y; i++) {
			FOREACH(it, adj[0][i]) {
				adj[1][*it].push_back(i);
			}
		}
		//for (int i = 0; i < X*Y; i++) {
		//	printf("%d: %d %d\n", i+1, adj[0][i].size(), adj[1][i].size());
		//}
		for (int i = 0; i < X*Y; i++) {
			visdel(i);
		}
		bool ok = true;
		for (int s = 0; s < 2; s++) {
			for (int i = 0; i < X*Y; i++) {
				if (adj[s][i].size() != 2 && adj[s][i].size() != 0) {
					ok = false;
					//printf("%d %d %d\n", s, i, adj[s][i].size());
				}
			}
		}
		if (!ok) {
			printf("0\n");
			continue;
		}
		int res = 1;
		for (int i = 0; i < X*Y; i++) {
			if (!vis[0][i] && adj[0][i].size() == 2) {
				res = (res*2)%1000003;
				viszus(i);
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
