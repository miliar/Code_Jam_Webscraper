#include <cstdio>
#include <cstring>
using namespace std;
const int dir[4][2]={-1,0,0,-1,0,1,1,0};

int C,n,m;
int g[110][110],ans[110][110],f[110][110];

int main() {
    scanf("%d",&C);
    for (int kk=1;kk<=C;kk++) {
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
        	for (int j=1;j<=m;j++)
        	    scanf("%d",&g[i][j]);
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++) {
                f[i][j]=-1;int mn=1000000;
                for (int d=0;d<4;d++) {
                    int x=i+dir[d][0],y=j+dir[d][1];
                    if (x<1 || x>n || y<1 || y>m) continue;
                    if (g[x][y]<mn) {
                        mn=g[x][y];
                        f[i][j]=d;
                    }    
                }    
                if (mn>=g[i][j]) f[i][j]=-1;
            }    
        }    	
        printf("Case #%d:\n",kk);
        memset(ans,-1,sizeof(ans));
        int now=0;
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++) {
  				int x=i,y=j;
      			while (f[x][y]!=-1) {
      			    int d=f[x][y];
      			    x=x+dir[d][0];
      			    y=y+dir[d][1];
         		}                 
         		if (ans[x][y]==-1) ans[x][y]=now++;
         		printf("%c",'a'+ans[x][y]);
         		if (j<m) printf(" "); else printf("\n");
            }    
        }    
    }    
}    
