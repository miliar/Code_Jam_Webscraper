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

int P, N;
int missable[3000];
int cost[3000];

LL cache[3000][20];

LL solve(int match, int skipped, int p)
{
	if (p == 0) {
		match -= 1 << P;
		if (skipped > missable[match])
			return 1234567890;
		return 0;
	}

	if (cache[match][skipped] != -1)
		return cache[match][skipped];

	int u = match*2;
	int v = match*2 + 1;

	LL a = solve(u, skipped, p-1) + solve(v, skipped, p-1) + cost[match];
	LL b = solve(u, skipped+1, p-1) + solve(v, skipped+1, p-1);

	LL result = 1234567890;

	if (a >= 0)
		min2(result, a);
	if (b >= 0)
		min2(result, b);
	cache[match][skipped] = result;
	return result;
}

int main()
{
	int TC;
	scanf("%d", &TC);
	for (int T = 1; T <= TC; ++T) {
		memset(cache, -1, sizeof cache);
		scanf("%d", &P);
		N = 1 << P;
		for (int i = N-1; i >= 0; --i)
			scanf("%d", &missable[i]);
		for (int i = N-1; i > 0; --i)
			scanf("%d", &cost[i]);
		printf("Case #%d: %lld\n", T, solve(1, 0, P));
	}
	return 0;
}
