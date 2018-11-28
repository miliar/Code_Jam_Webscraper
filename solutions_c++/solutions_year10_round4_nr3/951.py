#include <cstdio>
#include <cstring>

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,j,k,test,ttest,ans,r,x1,y1,x0,y0,x,y,n,m;
    bool a[110][110],b[110][110];
    scanf("%d",&test);
    for (ttest = 1; ttest<=test; ttest++) {
        scanf("%d",&r);
        n = m = 0;
        memset(a,0,sizeof(a));
        for (i = 1; i<=r; i++) {
          scanf("%d %d %d %d",&x0,&y0,&x1,&y1);
          if (x1>n) n = x1;
          if (y1>m) m = y1;
          for (x = x0; x<=x1; x++)
            for (y = y0; y<=y1; y++)
              b[x][y] = 1;
        }
        ans = 0;
        while (1) {
          int flag = 0;
          for (i = 1; i<=n; i++)
            for (j = 1; j<=m; j++) {
              a[i][j] = b[i][j];
              if (a[i][j]) flag = 1;  
            }          
          if (!flag) break;    
          memset(b,0,sizeof(b));
          for (i = 1; i<=n; i++)
            for (j = 1; j<=m; j++) {
              if (a[i][j]) b[i][j] = 1;
                 else if (a[i-1][j] && a[i][j-1]) b[i][j] = 1;   
              if (a[i][j] && !a[i-1][j] && !a[i][j-1]) b[i][j] = 0;
            }
          ans++;
        }
        printf("Case #%d: %d\n",ttest,ans);
    }
    return 0;
}
