// USTU Frogs
// Accepted
// I'm Feeling Lucky!

#pragma comment (linker, "/STACK:128000000");

#include <iostream>

void initf()
{
	freopen("treediff.in", "r", stdin);
	freopen("treediff.out", "w", stdout);
}

#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <cmath>

using namespace std;

#define fr(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define fi(n) for(int i = 0; i < (n); ++i)
#define fj(n) for(int j = 0; j < (n); ++j)
#define fk(n) for(int k = 0; k < (n); ++k)
#define pb push_back
#define clr(a) memset((a), 0, sizeof(a))

typedef vector < int > vi;

const int inf = 2147483647;
const int maxn = 50 * 1000 + 7;
const double eps = 1e-5;

vi g[10000];
double x[10000];
string s[10000], feat[10000];
bool end[10000];
int L;
string big_s;
double ans;
int m;

void dfs(int pos)
{
	while (!isdigit(big_s[pos]))
		++pos;
	double p;
	string s = big_s.substr(pos);
	sscanf(s.c_str(), "%lf", &p);
	ans *= p;

	while (big_s[pos] != ' ')
		++pos;
	while (big_s[pos] == ' ')
		++pos;

	if (big_s[pos] == ')')
	{
		printf("%.7lf\n", ans);
		return;
	}

	string cur = "";
	while (isalpha(big_s[pos]))
		cur.pb(big_s[pos++]);


	fi(m)
		if (feat[i] == cur)
		{
			while (big_s[pos] != '(')
				++pos;
			++pos;
			dfs(pos);
			return;
		}

	int lev = 0;

	while (pos < big_s.size() && big_s[pos] != '(')
		++pos;
	while (pos < big_s.size())
	{
		if (big_s[pos] == '(')
			++lev;
		if (big_s[pos] == ')')
			--lev;
		++pos;
		if (lev == 0)
			break;
	}
	dfs(pos);
}

void solve()
{
	scanf("%d\n", &L);
	big_s = "";
	fi(L)
	{
		string s;
		getline(cin, s, '\n');
		string new_s = "";
		fi(s.size())
		{
			if (s[i] == '(' || s[i] == ')')
				new_s.pb(' ');
			new_s.pb(s[i]);			
		}
		big_s = big_s + new_s;
	}

	int t;
	scanf("%d\n", &t);
	fi(t)
	{
		string ss;
		cin >> ss;
		cin >> m;
		fj(m)
			cin >> feat[j];

		ans = 1.0;
		int pos = 0;
		while (!isdigit(big_s[pos]))
			++pos;
		dfs(pos);
	}
}

int main()
{
	initf();
	int t;
	scanf("%d\n", &t);
	fi(t)
	{
		cout << "Case #" << i + 1 << ": \n";
		solve();
	}
	return (0);
}