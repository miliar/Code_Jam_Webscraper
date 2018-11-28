#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef stack<int> STI;
typedef set<int> SI;
typedef queue<int> QI;
typedef vector<PII > VPII;
typedef stack<PII > STPII;
typedef set<PII > SPII;
typedef queue<PII > QPII;

#define MAXK 1000001
#define MAXN 101

int next[MAXK];
int order[MAXK];

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		int K,n;
		scanf("%d %d", &K, &n);
		for(int i = 0; i < K-1; ++i)
			next[i] = i+1;
		next[K-1] = 0;
		for(int i = 0; i < K; ++i)
			order[i] = -1;
		
		int p = K-1;
		for(int i = 1; i <= K; ++i) {
			for(int j = 0; j < i; ++j) {
				p = next[p];
				int p2 = p;
				while(order[p] >= 0)
					p = next[p];
				if(p != p2)
					next[p2] = p;
			}
			order[p] = i;
		}
		
		printf("Case #%d:", t);
		for(int i = 0; i < n; ++i) {
			int d;
			scanf("%d", &d);
			printf(" %d", order[d-1]);	
		}
		printf("\n");
	}
	return 0;
}
