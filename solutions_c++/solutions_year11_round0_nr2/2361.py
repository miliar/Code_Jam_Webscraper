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
	freopen("b2.in", "r", stdin);
	freopen("b2.out", "w", stdout);
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
char co[330][330], op[330][330];

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	int i, j, k;
	__(co);
	__(op);
	int c, d, n;
	string s;
	scanf("%d", &c);
	fi(c)
	{
		cin >> s;
		co[s[0]][s[1]] = co[s[1]][s[0]] = s[2];
	}
	scanf("%d", &d);
	fi(d)
	{
		cin >> s;
		op[s[0]][s[1]] = op[s[1]][s[0]] = 1;
	}
	vector<char> res;
	scanf("%d", &n);
	cin >> s;
	panic(sz(s) == n);
	fi(n)
	{
		if (!res.empty() && co[res.back()][s[i]])
		{
			char x = res.back();
			res.pop_back();
			res.pb(co[x][s[i]]);
		}
		else
		{
			res.pb(s[i]);
			fj(sz(res) - 1)
			{
				if (op[res[j]][s[i]])
					res.clear();
			}
		}
	}
	printf("[");
	fi(sz(res))
	{
		if (i)
			printf(", ");
		printf("%c", res[i]);
	}
	printf("]\n");
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