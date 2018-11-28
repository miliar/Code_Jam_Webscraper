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
		int ans = 0;
		int curB = 1, curO = 1;
		int lastB = 0, lastO = 0;
		for (int i = 0; i < n; i++)
		{
			char c;
			int num;
			scanf(" %c %d", &c, &num);
			if (c == 'O')
			{
				lastO += max(abs(num - curO) - lastB, 0) + 1;
				ans += max(abs(num - curO) - lastB, 0) + 1;
				curO = num;
				lastB = 0;
			}
			else
			{
				lastB += max(abs(num - curB) - lastO, 0) + 1;
				ans += max(abs(num - curB) - lastO, 0) + 1;
				curB = num;
				lastO = 0;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}