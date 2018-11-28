#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<vi> vvi;

const int N = 510;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int n, m, d, g[N][N];
ll X1[N][N], Y1[N][N], Z1[N][N], X2[N][N], Y2[N][N], Z2[N][N];

void init()
{
    cin>>n>>m>>d;
    for(int i = 0; i <= n; i++)
        for (int j = 0 ; j <= m ; j ++ ) X1[i][j] = Y1[i][j] = Z1[i][j] = 0;
    for(int i = 1; i <= n; i++)
    {
        string s;
        cin>>s;
        for(int j = 1; j <= m; j++)
        {
            char ch = s[j-1];
            g[i][j] = ch - '0';
            X2[i][j] = X1[i][j] = ll(d + g[i][j]) * i;
            Y2[i][j] = Y1[i][j] = ll(d + g[i][j]) * j;
            Z2[i][j] = Z1[i][j] = (d + g[i][j]);
        }
    }
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
        {
            X1[i][j] += X1[i][j-1];
            Y1[i][j] += Y1[i][j-1];
            Z1[i][j] += Z1[i][j-1];
        }
    for(int j = 1; j <= m; j++)
        for(int i = 1; i <= n; i++)
        {
            X1[i][j] += X1[i-1][j];
            Y1[i][j] += Y1[i-1][j];
            Z1[i][j] += Z1[i-1][j];
        }
}

ll getddx(int i, int j, int len)
{
    return X1[i+len][j+len] + X1[i-1][j-1] - X1[i-1][j+len] - X1[i+len][j-1] 
            - X2[i][j] - X2[i][j+len] - X2[i+len][j] - X2[i+len][j+len];
}

ll getddy(int i, int j, int len)
{
    return Y1[i+len][j+len] + Y1[i-1][j-1] - Y1[i-1][j+len] - Y1[i+len][j-1] 
			- Y2[i][j] - Y2[i][j+len] - Y2[i+len][j] - Y2[i+len][j+len];
}

ll getddz(int i, int j, int len)
{
    return Z1[i+len][j+len] + Z1[i-1][j-1] - Z1[i-1][j+len] - Z1[i+len][j-1] 
			- Z2[i][j] - Z2[i][j+len] - Z2[i+len][j] - Z2[i+len][j+len];
}

void solve(int tcase)
{
    int ans = 0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            int len = min(n - i, m - j);
            while(len >= 2)
            {
                ll ddx = getddx(i, j, len);
				ll ddy = getddy(i, j, len);
				ll ddz = getddx(i, j, len);
				if (len % 2 == 1)
                {
                    ddx *= 2, ddy *= 2;
                    int x = (i + i + len);
                    int y = (j + j + len);
                    if (ddx - ddz * x == 0LL && ddy - ddz *y == 0LL) ans = max(ans, len+1);
				}
				else
				{
				    int x = (i + i + len) / 2;
				    int y = (j + j + len) / 2;
				    if (ddx - ddz * x == 0LL && ddy - ddz *y == 0LL) ans = max(ans, len+1);
				}
                len--;
            }
        }
    }
    printf("Case #%d: ", tcase);
    if(ans >= 3) printf("%d\n", ans);
    else puts("IMPOSSIBLE");
}

int main()
{
    freopen("B.in", "r", stdin);
    //freopen("ASout.txt", "w", stdout);
    int T;
    cin>>T;
    
    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
    while(1);
}
