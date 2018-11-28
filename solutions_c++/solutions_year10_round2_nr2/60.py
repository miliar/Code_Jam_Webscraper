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
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int B, T, N, K;
int X[200], V[200];

bool finishes(int i)
{
	return B - X[i] <= T * V[i];
}

int main()
{
	int TC;
	scanf("%d", &TC);
	for (int TCC = 1; TCC <= TC; ++TCC) {
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for (int i = 0; i < N; ++i)
			scanf("%d", &X[i]);
		for (int i = 0; i < N; ++i)
			scanf("%d", &V[i]);

		int finished = 0;
		int swap_cnt = 0;
		int slow_pokes = 0;
		for (int i = N-1; i >= 0 && finished < K; --i) {
			if (finishes(i)) {
				finished += 1;
				swap_cnt += slow_pokes;
			} else {
				slow_pokes += 1;
			}
		}

		printf("Case #%d: ", TCC);
		if (finished >= K)
			printf("%d\n", swap_cnt);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
