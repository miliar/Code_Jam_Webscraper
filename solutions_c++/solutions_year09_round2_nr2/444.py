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

char s[1000];
char s1[1000];
bool mark[1000];
int len;

bool ok()
{
	fi(len)
	{
		if (s1[i] > s[i])
			return (true);
		if (s1[i] < s[i]) return (false);
	}
	return (false);
}

void solve()
{
	gets(s);
	len = strlen(s);
	fi(len + 1)
		s1[i] = s[i];

	next_permutation(s1, s1 + len);

	if (ok())
	{
		fi(len)
			cout << s1[i];
		cout << endl;
		return;
	}

	clr(mark);
	int id = -1;
	fi(len)
	{
		if (s[i] == '0') continue;
		if (id == -1 || s[id] > s[i])
			id = i;
	}

	mark[id] = true;
	cout << s[id];
	cout << "0";
	for(int i = id + 1; i < len; ++i)
		s[i - 1] = s[i];
	sort(s, s + len - 1);
	fi(len - 1)
		cout << s[i];
	cout << endl;
}

int main()
{
	initf();
	int t;
	scanf("%d\n", &t);
	fi(t)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return (0);
}