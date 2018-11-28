#include <cstdio>
#include <string>
using namespace std;

const int MAXN = 101;
int T;
int NA, NB;
int t[2][MAXN][2];

void readtime(int t[2])
{
    char buf[100];
    int h1,m1,h2,m2;
    gets(buf);
    sscanf(buf, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
    t[0] = h1*60+m1;
    t[1] = h2*60+m2;
}

void init()
{
    scanf("%d\n", &T);
    scanf("%d%d\n", &NA, &NB);
    for (int i=0; i<NA; i++) readtime(t[0][i]);
    for (int i=0; i<NB; i++) readtime(t[1][i]);
}

const int maxn = MAXN*2;
int nx,ny,g[maxn][maxn], sy[maxn], cx[maxn], cy[maxn];

int path(int u)
{
    for (int v=1; v<=NA+NB; v++) if (g[u][v] && !sy[v]) {
	sy[v] = 1;
	if (!cy[v] || path(cy[v])) {
	    cx[u] = v; cy[v] = u; return 1;
	}
    }
    return 0;
}

void solve()
{
    memset(g,0,sizeof(g));
    for (int i=0; i<NA; i++)
	for (int j=0; j<NB; j++) {
	    if (t[0][i][1] + T <= t[1][j][0]) g[i+1][j+1+NA] = 1;
	    if (t[1][j][1] + T <= t[0][i][0]) g[j+1+NA][i+1] = 1;
	}
    memset(cx,0,sizeof(cx)); memset(cy,0,sizeof(cy));
    for (int i=1; i<=NA+NB; i++)
	if (!cx[i]) {
	    memset(sy,0,sizeof(sy));
	    path(i);
	}
    nx = NA; ny = NB;
    for (int i=1; i<=NA; i++) if (cy[i]!=0) nx--;
    for (int i=NA+1; i<=NA+NB; i++) if (cy[i]!=0) ny--;
    printf("%d %d\n", nx, ny);
}

int main(int argc, char* argv[])
{
    freopen(argv[1], "r",stdin);
    int cases;
    scanf("%d\n", &cases);
    for (int i=1; i<=cases; i++) {
	printf("Case #%d: ", i);
	init();
	solve();
    }
}

