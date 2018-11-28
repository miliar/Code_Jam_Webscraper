#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x)
{
    return x*x;
}

template <class T> T gcd(T a, T b)
{
    if(a < 0) return (gcd(-a, b));
    if(b < 0) return (gcd(a, -b));
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int m, n;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
int cmax;
int mat[105][105] = {0};
int rmat[105][105] = {0};

int Flow(int x, int y)
{
	if(rmat[x][y]) return rmat[x][y];
    int Min=mat[x][y];
    int mx, my;
    for(int k = 0; k < 4; k++)
    {
        int ci = x + dx[k];
        int cj = y + dy[k];
        if(ci < 0 || ci == m || cj < 0 || cj == n) continue;
        if(mat[ci][cj] < Min)
        {
			Min=mat[ci][cj];
            mx = ci;
            my = cj;
        }
    }
    if(Min == mat[x][y])
    {
        cmax++;
        return rmat[x][y] = cmax;
    }
    if(rmat[mx][my] != 0) return rmat[x][y] = rmat[mx][my];
    else return rmat[x][y] = Flow(mx, my);
}

int main(int argc, char** argv)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    for(int ti = 0; ti < t; ti++)
    {
        cmax = 0;
        mset(mat, 0);
        mset(rmat, 0);
        scanf("%d%d", &m, &n);

        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                scanf("%d", &mat[i][j]);
            }
        }


        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                Flow(i, j);
            }
        }
		printf("Case #%d:\n", ti+1);
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                printf("%c", rmat[i][j]+'a'-1);
                if(j==n-1) printf("\n"); else printf(" ");
            }
        }

    }
    return (EXIT_SUCCESS);
}

