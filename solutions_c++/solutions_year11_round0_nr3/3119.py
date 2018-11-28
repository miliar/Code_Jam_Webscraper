#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <numeric>

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define EPS 1e-9
#define INF INT_MAX
#define SQR(X) (X) * (X)
#define round(x) (int)floor((x) + 0.5 + EPS)

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long LL;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <uint> vu;
typedef vector <ull> vull;
typedef vector <pii> vpii;
typedef vector <vpii> vvpii;
typedef vector <string> vs;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++)
	{
		printf("Case #%d: ", z);
		int n;
		scanf("%d", &n);
		vi piles(n);
		int res = 0;
		long long sum = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &piles[i]);
			res ^= piles[i];
			sum += piles[i];
		}
		if (res)
			printf("NO\n");
		else 
			printf("%I64d\n", sum - *min_element(all(piles)));
	}
	return 0;
}