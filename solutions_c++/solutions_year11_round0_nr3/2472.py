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
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1 << 30;
const double EPS = 1e-9;

void prepare()
{
	freopen("c-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

int a[1005], n;

void solve2(int test_num)
{
	printf("Case #%d: ", test_num);
	int i, j, k;
	scanf("%d", &n);
	fi(n)
		scanf("%d", &a[i]);
	sort(a, a + n);
	int res = -1;
	fi(n) if (i)
	{
		int r1 = 0, r2 = 0, s = 0;
		fj(i)
			r1 ^= a[j];
		fo(j, i, n)
		{
			r2 ^= a[j];
			s += a[j];
		}
		if (r1 == r2)
		{
			res = s;
			break;
		}
	}
	if (res < 0)
		cout << "NO\n";
	else
		cout << res << endl;
}

void solve1(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int i, j, k;
	scanf("%d", &n);
	fi(n)
		scanf("%d", &a[i]);
	sort(a, a + n);
	int res = -1;
	int _2n1 = (1 << n) - 1;
	for (int mask = 1; mask < _2n1; mask++)
	{
		int r1 = 0, r2 = 0, s = 0;
		fi(n)
		{
			if ((mask >> i) & 1)
			{
				s += a[i];
				r1 ^= a[i];
			}
			else
				r2 ^= a[i];
		}
		if (r1 == r2)
			res = max(res, s);
	}
	if (res < 0)
		cout << "NO\n";
	else
		cout << res << endl;
}

int main()
{
	prepare();
	int number_of_tests, i;
	cin >> number_of_tests;
	fi(number_of_tests)
		solve2(i + 1);
	return 0;
}