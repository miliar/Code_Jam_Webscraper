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
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

const int maxn = 105;

int n;
string s[maxn];
double wp[maxn], owp[maxn], oowp[maxn];

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d:\n", test_num);
	scanf("%d", &n);
	panic(n < maxn);
	fi(n)
		cin >> s[i];
	__(wp);
	__(owp);
	__(oowp);
	int cnt;
	fi(n)
	{
		cnt = 0;
		fj(n)
		{
			if (s[i][j] == '1')
				wp[i]++;
			if (s[i][j] != '.')
			{
				panic(s[i][j] == '1' || s[i][j] == '0');
				cnt++;
			}
		}
		if (cnt)
			wp[i] /= cnt;
	}
	fi(n)
	{
		cnt = 0;
		fj(n)
		{
			if (s[i][j] != '.')
			{
				double _wp = 0;
				int _cnt = 0;
				fk(n)
				{
					if (k != i)
					{
						if (s[j][k] == '1')
							_wp++;
						if (s[j][k] != '.')
							_cnt++;
					}
				}
				owp[i] += _wp / _cnt;
				cnt++;
			}
		}
		if (cnt)
			owp[i] /= cnt;
	}
	fi(n)
	{
		cnt = 0;
		fj(n)
		{
			if (s[i][j] != '.')
			{
				oowp[i] += owp[j];
				cnt++;
			}
		}
		if (cnt)
			oowp[i] /= cnt;
	}
	fi(n)
	{
		printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
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