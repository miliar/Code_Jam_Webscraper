#include <stdio.h>
#include <string.h>

char map[55][55];
char ans[55][55];

int main()
{
    freopen("aa.in","r",stdin);
    freopen("aa.out","w",stdout);
    int i,j,n,T,cnt,m;
    cnt=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for (i=0;i<n;i++)
        {
            scanf("%s",map[i]);    
        }          
        memset(ans,0,sizeof(ans));
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                if (map[i][j]=='.') 
                {
                    ans[i][j]='.';
                    continue;                    
                }   
                if (i+1>=n || j+1>=m) continue;
                if (ans[i][j]!=0 || ans[i+1][j]!=0 || ans[i][j+1]!=0 || ans[i+1][j+1]!=0) continue;
                ans[i][j]=ans[i+1][j+1]='/';
                ans[i][j+1]=ans[i+1][j]='\\'; 
            }    
        }
        printf("Case #%d:\n",cnt++);
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                if (ans[i][j]==0) break;
            }    
            if (j<m) break;
        }
        if (i<n) printf("Impossible\n");
        else 
        {
             for (i=0;i<n;i++)
             {
                 for (j=0;j<m;j++)
                 {
                     printf("%c",ans[i][j]);    
                 }
                 printf("\n");
             }     
        }
    }    
    return 0;
}
