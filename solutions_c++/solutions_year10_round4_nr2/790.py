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
	freopen("b-small.txt", "w", stdout);
}

void panic(bool expression = false)
{
	if (!expression)
	{
		cerr << "PANIC!" << endl;
		assert(false);
	}
}

int a[1 << 18];
int p;
int m[1 << 15];
int pr[20][1 << 15];

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int i, j, k;
	cin >> p;
	int p2 = 1 << p;
	int shift = 1;
	while (shift < p2)
		shift <<= 1;
	__(a);
	int x;
	fi(p2)
		cin >> m[i];
	fi(p)
	{
		fj(1 << (p - i - 1))
		{
			cin >> x;
		}
	}
	fi(p2)
	{
		for (k = (shift + i) / 2, j = 1; k > 0; k /= 2, j++)
		{
			if (j > m[i])
				a[k] = 1;
		}
	}
	int res = 0;
	fi(shift + p2)
		res += a[i];
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