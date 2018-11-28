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
const int MAX = 101;

int hx[4] = {-1, 0, 0, 1};
int hy[4] = {0, -1, 1, 0};

int n, m, ld;
int a[MAX][MAX];
int d[MAX][MAX];

int nx[MAX][MAX];
int ny[MAX][MAX];

void init()
{
	memset(nx, -1, sizeof(nx));
	memset(ny, -1, sizeof(ny));
	int i, j, k, best, mx, my;
	RP(i, n) RP(j, m)
	{
		best = INF;
		RP(k, 4)
			if (i+hx[k]>=0&&i+hx[k]<n&&j+hy[k]>=0&&j+hy[k]<m&&a[i+hx[k]][j+hy[k]]<best)
			{
				best=a[i+hx[k]][j+hy[k]];
				mx=i+hx[k];
				my=j+hy[k];
			}

		if (best<a[i][j])
		{
			nx[i][j] = mx;
			ny[i][j] = my;
		}
	}
}

void flood(int x, int y)
{
	if (d[x][y]>=0) return;
	d[x][y] = ld;

	if (nx[x][y]>=0) flood(nx[x][y], ny[x][y]);

	int k;
	RP(k, 4)
		if (x+hx[k]>=0&&x+hx[k]<n&&y+hy[k]>=0&&y+hy[k]<m&&nx[x+hx[k]][y+hy[k]]==x&&ny[x+hx[k]][y+hy[k]]==y)
		{
			flood(x+hx[k], y+hy[k]);
		}
}

void output()
{
	int i, j;
	RP(i, n)
	{
		RP(j, m)
		{
			cout << (char)(d[i][j]+'a');
			if (j < m-1) cout << " ";
		}
		cout << endl;
	}
}
 
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tc, testcase, i, j;

	cin >> tc;

	RP(testcase, tc)
	{
		cin >> n >> m;
		RP(i, n) RP(j, m) cin >> a[i][j];
		init();
		memset(d, -1, sizeof(d));
		ld = 0;
		RP(i, n) RP(j, m) if (d[i][j] == -1)
		{
			flood(i, j);
			ld++;
		}
		cout << "Case #" << (testcase+1) << ":" << endl;
		output();
	}

	return 0;
}
