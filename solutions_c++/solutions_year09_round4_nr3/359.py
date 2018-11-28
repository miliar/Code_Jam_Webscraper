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

int N, K;

int data[111][27];

bool crosses[128][128];
bool ok[70000];

int sign(int x)
{
	if (x < 0) return -1;
	if (x == 0) return 0;
	return 1;
}

bool check_cross(int a, int b)
{
	int s = sign(data[a][0] - data[b][0]);
	if (s == 0)
		return true;
	for (int i = 1; i < K; ++i) {
		if (s != sign(data[a][i] - data[b][i]))
			return true;
	}
	return false;
}

bool bm_ok(int bm)
{
	vector<int> v;
	int m = 1;
	for (int i = 0; i < N; ++i, m *= 2) {
		if (bm & m) {
			for (int j = 0; j < SZ(v); ++j) {
				if (crosses[i][v[j]])
					return false;
			}
			v.push_back(i);
		}
	}
	return true;
}

int cache[70000];

int solve(int used)
{
	if (used == (1<<N)-1)
		return 0;
	if (cache[used] != -1)
		return cache[used];
	int best = 1234567890;
	int used_i = (~used) & ((1 << N) - 1);
	for (int bm = used_i; bm > 0; bm = (bm-1) & used_i) {
		if (bm & used)
			continue;
		if (!ok[bm])
			continue;
		min2(best, solve(used | bm) + 1);
	}
	cache[used] = best;
	return best;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		fprintf(stderr, "solving case %d\n", TC);
		memset(cache, -1, sizeof cache);
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < K; ++j) {
				scanf("%d", &data[i][j]);
			}
		}
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				crosses[i][j] = check_cross(i, j);
		for (int i = 0; i < (1 << N); ++i) {
			ok[i] = bm_ok(i);
		}
		printf("Case #%d: %d\n", TC, solve(0));
	}
	return 0;
}
