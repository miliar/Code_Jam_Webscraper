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

#define MOD 100003

int binom[600][600];
int sols[600][600]; 

int solve(int n)
{
	int sum = 0;
	for (int i = 1; i <= n-1; ++i)
		sum += sols[i][n];
	return sum % MOD;
}

int main()
{
	binom[0][0] = 1;
	for (int r = 1; r < 600; ++r) {
		binom[r][0] = 1;
		for (int c = 1; c <= r; ++c)
			binom[r][c] = (binom[r-1][c-1] + binom[r-1][c]) % MOD;
	}

	sols[0][1] = 1;
	for (int i = 1; i < 600; ++i) {
		for (int j = i+1; j < 600; ++j) {
			for (int k = 0; k < i; ++k) {
				LL t = sols[k][i];
				t *= binom[j-i-1][i-k-1];
				t %= MOD;
				sols[i][j] = (sols[i][j] + t) % MOD;
			}
		}
	}

	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", TC, solve(n));
	}
	return 0;
}
