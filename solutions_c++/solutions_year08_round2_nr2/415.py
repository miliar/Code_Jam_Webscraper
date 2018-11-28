#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <queue>
#include <vector>
#include <string>
using namespace std;
#define		MAX(a,b)	((a)>(b)?(a):(b))
#define		MIN(a,b)	((a)<(b)?(a):(b))

int prime[1001];

int parent[1001];
void make(int N) { for (int i=0; i<N; ++i) parent[i] = i; }
int root(int x) { if (parent[x] == x) return x; return root(parent[x]); }
void uni(int x, int y) {
  int x_root = root(x), y_root = root(y);
  parent[x_root] = y_root;
}


int main() {
	int C;
	scanf("%d", &C);

	prime[0] = prime[1] = 1;
	for (int i = 2; i < 101; i ++) {
		for (int j = i+i; j < 1000; j += i) {
			prime[j] = 1;
		}
	}
	/*
	for (i = 0; i < 1000; i ++) {
		if (!prime[i]) printf("%d ", i);
	}
*/
	for (i = 0; i < C; i ++) {
		int A, B, P;
		__int64 ans = 0;
		scanf("%d %d %d", &A, &B, &P);
/*		int db[1001];
		memset(db, 0, sizeof(db));*/

		make(1001);

		for (int K = P; K < B; K ++) {
			if (prime[K] == 0) {
				int old = -1;
				for (int p = A; p <= B; p ++) {
					if (p % K == 0) {
						if (old == -1) {
							old = p;
						} else {
							uni(old, p);
						}
					}
				}
			}
		}
		vector<int> v;
		for (K = A; K <= B; K++) {
//			printf("%d\n", root(K));
			v.push_back(root(K));
		}

	  sort(v.begin(), v.end());
		v.erase(unique(v.begin(), v.end()), v.end());


		printf("Case #%d: %d\n", i+1, v.size());
	}

	return 0;
}