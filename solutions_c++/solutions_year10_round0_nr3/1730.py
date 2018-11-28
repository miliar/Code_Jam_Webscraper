#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long i64;

const int NS = 1010;

int x[NS];
int used[NS];
int prev[NS];
i64 sum[NS];

int S = 1;
int pos;

int main() {

//	freopen("a.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("result.out", "w", stdout);

	int i, j, T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int R, k, N;	
		scanf("%d%d%d", &R, &k, &N);

		for (i = 1; i <= N; ++i) {
			scanf("%d", &x[i]);
		}
		i64 mySum = 0;

		memset (used, -1, sizeof(used));
		memset (prev, -1, sizeof(prev));
		memset (sum, 0, sizeof(sum));

		pos = 1;
		prev[0] = 0;
		sum[0] = 0;
		used[0] = 0;

		int speed = 1;

		S = 1;
		while (S <= R) {
			if (pos && used[pos] != -1 && speed) {

				int cind = used[pos];
				int prevPos = 0;
				for (int w = 1; w <= N; ++w) {
					if (used[w] == used[pos]-1) {
						prevPos = w;
						break;
					}
				}
				if (used[prevPos] == -1) prevPos = 0;

				int len = S - used[pos];
				i64 psum = mySum - sum[prevPos];

				if (psum < 0) 
					psum = psum;

				int have = R - S + 1;
				i64 ch = have / len;

				mySum += ch * psum;
				S += ch * len;
				speed = 0;
			}
			else {
				int cnt = 0;
				i64 csum = 0;
				int oldPos = pos, oldPos2 = pos;
				if (pos == 0) ++pos, oldPos2++;
				while (cnt < N && csum + x[pos] <= k) {
					csum += x[pos];
					if (++pos == N + 1) pos = 1;
					++cnt;
				}
				used[oldPos2] = S;
				prev[pos] = oldPos;
				mySum += csum;
				sum[oldPos2] = mySum;
				++S;
			}
		}
		
		printf ("Case #%d: %lld\n", t, mySum);
	}

	return 0;
}
