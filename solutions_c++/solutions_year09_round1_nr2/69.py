#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const int MAX = 55;

int N, M;
int S[MAX][MAX], W[MAX][MAX], T[MAX][MAX];
int D[MAX][MAX][4];
bool final[MAX][MAX][4];

void check_best(int &x, int y)
{
	if (x==-1 || x>y) x = y;
}

int getW(int x, int y, int at)
{
	int t = (at + (S[x][y]+W[x][y]) - T[x][y]) % (S[x][y]+W[x][y]);
	if (t < S[x][y]) return S[x][y]-t; else return 0;
}

int getS(int x, int y, int at)
{
	int t = (at + (S[x][y]+W[x][y]) - T[x][y]) % (S[x][y]+W[x][y]);
	if (t >= S[x][y]) return (S[x][y]+W[x][y]-t); else return 0;
}

void go_forward(int x, int y, int dir, int at)
{
	check_best(D[x][y][(dir+1)%4], at+2);
	check_best(D[x][y][(dir+3)%4], at+2);

	if (dir == 0)
	{
		if (x>0 && y>0) check_best(D[x][y-1][1], at+getW(x-1, y-1, at)+1);
		if (x>0 && y>0) check_best(D[x-1][y][3], at+getS(x-1, y-1, at)+1);
	}

	if (dir == 1)
	{
		if (x>0 && y<M) check_best(D[x][y+1][0], at+getW(x-1, y, at)+1);
		if (x>0 && y<M) check_best(D[x-1][y][2], at+getS(x-1, y, at)+1);
	}

	if (dir == 2)
	{
		if (x<N && y<M) check_best(D[x][y+1][3], at+getW(x, y, at)+1);
		if (x<N && y<M) check_best(D[x+1][y][1], at+getS(x, y, at)+1);
	}

	if (dir == 3)
	{
		if (x<N && y>0) check_best(D[x][y-1][2], at+getW(x, y-1, at)+1);
		if (x<N && y>0) check_best(D[x+1][y][0], at+getS(x, y-1, at)+1);
	}
}

void dijstra()
{
	memset(D, -1, sizeof(D));
	memset(final, false, sizeof(final));
	D[N][0][1] = 0;
	while (true)
	{
		int i, j, k;
		int li, lj, lk, best;
		li=lj=lk=-1;
		best = INF;
		RP(i, N+1) RP(j, M+1) RP(k, 4) if (!final[i][j][k] && D[i][j][k]>=0 && D[i][j][k] < best)
		{
			best = D[i][j][k];
			li=i; lj=j; lk=k;
		}
		if (li == -1) break;
		if (li==0 && lj==M && lk==3) break;
		final[li][lj][lk] = true;

		go_forward(li, lj, lk, D[li][lj][lk]);
	}
}

int main()
{
	//freopen("sample.in", "r", stdin); //freopen("sample.out", "w", stdout);
	freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

	int tc, testcase, i, j;

	cin >> tc;

	RP(testcase, tc)
	{
		cin >> N >> M;
		RP(i, N) RP(j, M)
		{
			cin >> S[i][j] >> W[i][j] >> T[i][j];
			T[i][j] %= (S[i][j]+W[i][j]);
		}
		dijstra();
		printf("Case #%d: %d\n", (testcase+1), D[0][M][3]);
	}

	return 0;
}
