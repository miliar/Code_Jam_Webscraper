#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <math.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define DFOR(i, a, b) for (int (i) = (a) - 1; (i) >= (b); (i)--)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define VI vector <int>
#define VS vector <string>
#define PB push_back
#define MP make_pair
#define SS stringstream
#define INF 1073741824
#define PII pair <int, int>
#define ALL(a) a.begin(), a.end()
#define SZ(x) (int)x.size()

#define LL long long
#define X first
#define Y second

void init()
{
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
}

char buf[50];
string s;

void solvecase(int test)
{
	cout << "Case #" << test << ": ";
	gets(buf);
	s = string(buf);
	if (next_permutation(ALL(s)))
	{
		cout << s << endl;
	}
	else
	{
		sort(ALL(s));
		s = "0" + s;
		int i = 0;
		while (s[i] == '0') ++i;
		swap(s[i], s[0]);
		cout << s << endl;
	}
}

void solve()
{
	int T;
	scanf("%d\n", &T);
	FOR(i, T) solvecase(i + 1);
}

int main()
{
	init();
	solve();
	return 0;
}