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

#define fo(a,b,c) for (a = (b); a < (c); a++)
#define fr(a,b) fo(a, 0, (b))
#define fi(n) fr(i, (n))
#define fj(n) fr(j, (n))
#define fk(n) fr(k, (n))
#define fd(a,b,c) for (a = (b); a >= (c); a--)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define _(a,b) memset((a), (b), sizeof(a))
#define __(a) memset((a), 0, sizeof(a))
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1 << 20;
const double EPS = 1e-8;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("c-small.txt", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

int a[2][105][105];
int c;

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int i, j, k;
	int x1, x2, y1, y2;
	int r;
	c = 0;
	scanf("%d", &r);
	__(a);
	c = 0;
	int n, m;
	n = 0;
	m = 0;
	fk(r)
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		if (x1 > x2)
			swap(x1, x2);
		if (y1 > y2)
			swap(y1, y2);
		x1--;
		x2--;
		y1--;
		y2--;
		fo(i, y1, y2 + 1)
		{
			fo(j, x1, x2 + 1)
				a[c][i][j] = 1;
		}
		n = max(n, y2);
		m = max(m, x2);
	}
	n++;
	m++;
	bool ok = true;
	int res = 0;
		//fi(n)
		//{
		//	fj(m)
		//	{
		//		printf("%d", a[c][i][j]);
		//	}
		//	printf("\n");
		//}
		//printf("\n");
	while (ok)
	{
		ok = false;
		fi(n) fj(m)
		{
			if (a[c][i][j])
			{
				ok = true;
				break;
			}
			if (ok)
				break;
		}
		if (!ok)
			break;
		res++;
		fi(n)
		{
			fj(m)
			{
				a[c ^ 1][i][j] = a[c][i][j];
				if ((i == 0 || a[c][i - 1][j] == 0) && (j == 0 || a[c][i][j - 1] == 0))
				{
					a[c ^ 1][i][j] = 0;
				}
				if (i > 0 && j > 0 && a[c][i - 1][j] == 1 && a[c][i][j - 1] == 1)
				{
					a[c ^ 1][i][j] = 1;
				}
			}
		}
		c = 1 - c;
		//fi(n)
		//{
		//	fj(m)
		//	{
		//		printf("%d", a[c][i][j]);
		//	}
		//	printf("\n");
		//}
		//printf("\n");
	}
	cout << res << '\n';
}

int main()
{
	prepare();
	int number_of_tests, i;
	cin >> number_of_tests;
	fi(number_of_tests)
		solve(i + 1);
	return 0;
}