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

const int MAXN = 50;

int T;
int n;
char board[MAXN][MAXN];
int a[MAXN];

void solvecase(int test)
{
	cout << "Case #" << test << ": ";
	scanf("%d\n", &n);
	CLR(board, 0);
	FOR(i, n) gets(board[i]);
	CLR(a, 0);
	FOR(i, n) {
		a[i] = n;
		while (a[i] > 0 && board[i][a[i] - 1] == '0') a[i]--;
	}
	int res = 0;
	FOR(i, n)
	{
		int j = i;
		while (j + 1 < n && a[j] > i + 1) j++;
		for (int k = j; k > i; --k) 
		{
			swap(a[k], a[k - 1]);
			res++;
		}
	}
	cout << res << endl;
}

void solve()
{
	cin >> T;
	FOR(i, T)
		solvecase(i + 1);
}

int main()
{
	init();
	solve();
	return 0;
}