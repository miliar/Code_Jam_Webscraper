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

int n;
pair<int, int> a[105];

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int i, j, k;
	scanf("%d", &n);
	vector<int> v[2];
	fi(n)
	{
		char c;
		scanf(" %c %d", &c, &a[i].second);
		if (c == 'B')
			a[i].first = 0;
		else
			a[i].first = 1;
		v[a[i].first].pb(a[i].second);
	}
	v[0].pb(INF);
	v[1].pb(INF);
	int g = 0, res = 0, x[2], p[2];
	x[0] = x[1] = 1;
	__(p);
	while (true)
	{
		int dx[2];
		__(dx);
		fi(2)
		{
			if (x[i] < v[i][p[i]])
				dx[i] = 1;
			else if (x[i] > v[i][p[i]])
				dx[i] = -1;
		}
		fi(2)
		{
			if (dx[i] == 0 && a[g].first == i)
			{
				g++;
				p[i]++;
				break;
			}
		}
		x[0] += dx[0];
		x[1] += dx[1];
		res++;
		if (g >= n)
			break;
	}
	cout << res << endl;
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