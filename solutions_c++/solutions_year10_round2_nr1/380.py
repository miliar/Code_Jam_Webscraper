#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <memory.h>

using namespace std;

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

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("a.txt", "w", stdout);
}

void panic()
{
	cout << "PANIC!" << endl;
	assert(false);
}

string s[105];
set<string> se;
char ch[1000];
bool f[104];
int p[1000];
int n, m;

void solve(int test_num)
{
	printf("Case #%d: ", test_num);
	cin >> n >> m;
	gets(ch);
	int i, j;
	string g;
	se.clear();
	se.insert("/");
	fi(n)
	{
		gets(ch);
		g = ch;
		se.insert(g);
	}
	fi(m)
	{
		gets(ch);
		s[i] = ch;
	}
	bool ok = true;
	int res = 0;
	int sp = 0;
	fi(m)
	{
		if (se.find(s[i]) != se.end())
			continue;
		__(p);
		sp = 0;
		fj(sz(s[i]))
			if (s[i][j] == '/')
				p[sp++] = j;
		p[0] = 1;
		p[sp] = sz(s[i]);
		for (j = sp - 1; j >= 0; j--)
		{
			if (se.find(s[i].substr(0, p[j])) != se.end())
				break;
		}
		for (; j < sp; j++)
		{
			g = s[i].substr(0, p[j + 1]);
			if (se.find(g) == se.end())
			{
				se.insert(g);
				res++;
			}
		}
	}
	printf("%d\n", res);
}

int main()
{
	prepare();
	int k, i;
	cin >> k;
	fi(k)
		solve(i + 1);
	return 0;
}