#include <iostream>
#define MAXN 101
#define INFINIT 2000000000

using namespace std;

int n,m;
int Case,CASE;
int a[MAXN+1][MAXN+1];
char fun[MAXN*MAXN+1];
int color[MAXN+1][MAXN+1];
char Ans[MAXN+1][MAXN+1];
int Color = 1;
int fx[] = {-1,0,0,1};
int fy[] = {0,-1,1,0};

int dfs(int x,int y){
	if (color[x][y]) return color[x][y];
     int t;
     int Min = INFINIT;
	for (int i = 0; i<4; i++)
		Min = min(Min,a[x+fx[i]][y+fy[i]]);
	if (Min>=a[x][y]){
		Color++;
	    color[x][y] = Color;
	    return Color;
		}
	for (int i = 0; i<4; i++)
	if (a[x+fx[i]][y+fy[i]] == Min) return color[x][y] = dfs(x+fx[i],y+fy[i]);
     
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&CASE);
    for (int Case = 1; Case<=CASE; Case++){
        scanf("%d%d",&n,&m);
        memset(a,0,sizeof(a));
        memset(color,0,sizeof(color));
        memset(Ans,0,sizeof(Ans));
        memset(fun,0,sizeof(fun));
        Color = 0;
        for (int i = 0; i<=n+1; i++)
            a[i][0] = a[i][m+1] = INFINIT;
        for (int i = 0; i<=m+1; i++)
            a[0][i] = a[n+1][i] = INFINIT;
        for (int i = 1; i<=n; i++)
        for (int j = 1; j<=m; j++)
        scanf("%d",&a[i][j]);
        for (int i = 1; i<=n; i++)
        for (int j = 1; j<=m; j++)
        if (!color[i][j]) 
			dfs(i,j);
        int ch = 'a';
        for (int i = 1; i<=n; i++)
        for (int j = 1; j<=m; j++)
        if (!fun[color[i][j]]) fun[color[i][j]] = ch++;
        printf("Case #%d:\n",Case);
        /*for (int i = 1; i<=n; i++)
        {
	        for (int j = 1; j<=m; j++)
	        printf("%d ",color[i][j]);
   			printf("\n");
		}*/
        for (int i = 1; i<=n; i++)
        {
            printf("%c",fun[color[i][1]]);
            for (int j = 2; j<=m; j++)
                printf(" %c",fun[color[i][j]]);
            printf("\n");
        }
    }
    return 0;
}
