
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N - 1; i >= 0; --i)

#define ABS(N) (((N) < 0) ? (-(N)) : (N))
#define MIN(A, B) (((A) < (B)) ? (A) : (B))
#define MAX(A, B) (((A) > (B)) ? (A) : (B))
#define EPS 1e-7
#define ALL(V) V.begin(), V.end()
#define pb push_back
#define mp make_pair
#define Pi 3.14159265358979323846
#define SIZE(V) V.size()


typedef vector <int> VI;
typedef pair <int, int> PI;
typedef long long Long;
typedef unsigned int Uint;
typedef unsigned long long ULong;
typedef unsigned char Uchar;

#define SZ 120

int H;
int W;
int R;
int res[SZ][SZ];
bool b[SZ][SZ];

void solve()
{
	memset(res, 0, sizeof(res));
	memset(b, 0, sizeof(b));
	scanf("%d%d%d", &H, &W, &R);
	int x;
	int y;
	REP(i, R)
	{
		scanf("%d%d", &x, &y);
		b[x - 1][y - 1] = 1;
	}
	res[0][0] = 1;
	REP(i, H)
		REP(j, W)
		{
			if(!b[i + 2][j + 1])
			{
				res[i + 2][j + 1] += res[i][j];
				res[i + 2][j + 1] %= 10007;
			}
			if(!b[i + 1][j + 2])
			{
				res[i + 1][j + 2] += res[i][j];
				res[i + 1][j + 2] %= 10007;
			}
		}
	printf("%d\n", res[H - 1][W - 1]);
}

int N;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &N);
	REP(i, N)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}