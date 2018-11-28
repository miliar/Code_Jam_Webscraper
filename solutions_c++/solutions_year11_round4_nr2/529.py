#pragma comment(linker, "/stack:128000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <memory.h>
#include <cassert>

using namespace std;

#define fo(a,b,c) for (int a = (b); a < (c); a++)
#define fr(a,b) fo(a, 0, (b))
#define fi(n) fr(i, (n))
#define fj(n) fr(j, (n))
#define fk(n) fr(k, (n))
#define fd(a,b,c) for (int a = (b); a >= (c); a--)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define _(a,b) memset((a), (b), sizeof(a))
#define __(a) memset((a), 0, sizeof(a))
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

typedef long long lint;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1 << 30;
const double EPS = 1e-9;

void prepare()
{
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

int n, m, d;
lint a[505][505], w[505][505], py[505][505], px[505][505];
char c[505][505];

lint calc2(lint a[505][505], int i1, int j1, int i2, int j2)
{
	if (i1 < 0 || j1 < 0 || i2 < 0 || j2 < 0)
		return 0;
	if (i1 == 0 && j1 == 0)
		return a[i2][j2];
	return calc2(a, 0, 0, i2, j2) - calc2(a, 0, 0, i1 - 1, j2) - calc2(a, 0, 0, i2, j1 - 1) + calc2(a, 0, 0, i1 - 1, j1 - 1);
}

lint calc(lint a[505][505], int i1, int i2, int j1, int j2)
{
	return
		calc2(a, i1, j1, i2, j2) -
		calc2(a, i1, j1, i1, j1) -
		calc2(a, i1, j2, i1, j2) -
		calc2(a, i2, j1, i2, j1) - 
		calc2(a, i2, j2, i2, j2); 
}

void solve(int test_num)
{
	cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	scanf("%d%d%d", &n, &m, &d);
	fi(n)
	{
		scanf("%s", c[i]);
		fj(m)
			a[i][j] = c[i][j] - '0' + d;
	}
	fi(n)
	{
		fj(m)
		{
			w[i][j] = a[i][j];
			if (i)
				w[i][j] += w[i - 1][j];
			if (j)
				w[i][j] += w[i][j - 1];
			if (i && j)
				w[i][j] -= w[i - 1][j - 1];
		
			px[i][j] = a[i][j] * (2 * i + 1);
			if (i)
				px[i][j] += px[i - 1][j];
			if (j)
				px[i][j] += px[i][j - 1];
			if (i && j)
				px[i][j] -= px[i - 1][j - 1];

			py[i][j] = a[i][j] * (2 * j + 1);
			if (i)
				py[i][j] += py[i - 1][j];
			if (j)
				py[i][j] += py[i][j - 1];
			if (i && j)
				py[i][j] -= py[i - 1][j - 1];
		}
	}
	fd(k, min(n, m) / 2 + 2, 1)
	{
		fi(n)
		{
			fj(m)
			{
				if (k > i || k > j ||
					k >= n - i || k >= m - j)
					continue;
				int i1 = i - k;
				int i2 = i + k;
				int j1 = j - k;
				int j2 = j + k;
				lint sx1 = calc(px, i1, i2, j1, j2);
				lint sy1 = calc(py, i1, i2, j1, j2);
				lint s2 = calc(w, i1, i2, j1, j2);
				if (sx1 - s2 * (2 * i + 1) == 0 &&
					sy1 - s2 * (2 * j + 1) == 0)
				{
					printf("%d\n", k * 2 + 1);
					return;
				}
			}
		}

		if (k == 1)
			break;
		fi(n)
		{
			fj(m)
			{
				if (k > i + 1 || k > j + 1 ||
					k >= n - i || k >= m - j)
					continue;
				int i1 = i - k + 1;
				int i2 = i + k;
				int j1 = j - k + 1;
				int j2 = j + k;
				lint sx1 = calc(px, i1, i2, j1, j2);
				lint sy1 = calc(py, i1, i2, j1, j2);
				lint s2 = calc(w, i1, i2, j1, j2);
				if (sx1 - s2 * (2 * i + 2) == 0 &&
					sy1 - s2 * (2 * j + 2) == 0)
				{
					printf("%d\n", k * 2);
					return;
				}
			}
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	prepare();
	int number_of_tests;
	cin >> number_of_tests;
	fi(number_of_tests)
		solve(i + 1);
	return 0;
}