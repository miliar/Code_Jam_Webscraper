#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

int N, M;
set<int> cust[100];

void solve(int id) {
	int limit = 1 << N;
	int opt_tag = -1, opt_cnt = -1;
	for (int tag=0; tag<limit; ++tag) {
		string vis(M, 0);
		int temp = tag;
		int cnt = 0;
		for (int i=0; i<N; ++i) {
			if (temp & 1) {
				for (int k=0; k<M; ++k) {
					if (cust[k].count(i+1) )
						vis[k] = 1;
				}
			}
			else {
				for (int k=0; k<M; ++k) {
					if (cust[k].count(-i-1) )
						vis[k] = 1;
				}
			}
			temp >>= 1;
		}
		if (vis == string(M, 1) ) {
			if (opt_cnt == -1 || opt_cnt > cnt) {
				opt_cnt = cnt;
				opt_tag = tag;
			}
		}
	}

	printf("Case #%d:", id);

	if (opt_tag == -1) {
		printf(" IMPOSSIBLE\n");		
	}
	else {
		for (int i=0; i<N; ++i) {
			if (opt_tag & 1)
				printf(" 1");
			else
				printf(" 0");
			opt_tag >>= 1;
		}
		printf("\n");
	}
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	int C;
	scanf("%d", &C);
	for (int id=1; id<=C; ++id) {
		scanf("%d", &N);
		scanf("%d", &M);
		for (int i=0; i<M; ++i) {
			cust[i].clear();
			int T;
			scanf("%d", &T);
			for (int k=0; k<T; ++k) {
				int X, Y;
				scanf("%d %d", &X, &Y);
				if (Y == 1)
					cust[i].insert(X);
				else
					cust[i].insert(-X);
			}
		}
		solve(id);
	}
	return 0;
}