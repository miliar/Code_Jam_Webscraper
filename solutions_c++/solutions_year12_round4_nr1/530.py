#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define maxit(x,y) ((x) = max((x),(y)))
#define minit(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N;
int D[11000], L[11000];
int best_len[11000];

int main()
{
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%d %d", &D[i], &L[i]);
		scanf("%d", &D[N]);
		L[N] = 0;
		memset(best_len, -1, sizeof best_len);
		best_len[0] = D[0];
		for (int i = 0; i < N; ++i) {
			if (best_len[i] == -1)
				break;
			for (int j = i+1; j <= N; ++j) {
				if (D[j] > D[i]+best_len[i])
					break;
				maxit(best_len[j], min(D[j]-D[i], L[j]));
			}
		}
		printf("Case #%d: %s\n", tc, (best_len[N]==-1?"NO":"YES"));
		fflush(stdout);
	}
	return 0;
}
