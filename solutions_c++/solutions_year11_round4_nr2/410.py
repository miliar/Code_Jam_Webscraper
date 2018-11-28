#include <stdio.h>
#include <string.h>

char s[20][20];

int main()
{
    int cas;
    int n,m,d;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d %d %d",&n,&m,&d);
        for(int i=0;i<n;i++)
        {
            scanf("%s",s[i]);
            for(int j=0;j<m;j++) s[i][j]-='0';
        }
        int ans=0;
        for(int i=0;i<n-2;i++)
         for(int j=0;j<m-2;j++)
         {
             for(int k=3;i+k<=n&&j+k<=m;k++)
             {
                 int sumx=0,sumy=0;
                 int pp=0;
                 for(int l=i;l<i+k;l++)
                  for(int p=j;p<j+k;p++)
                  {
                      //printf("%c",s[l
                      sumx+=l*s[l][p];
                      pp+=s[l][p];
                      sumy+=p*s[l][p];
                  }
                 sumx-=i*s[i][j]+i*s[i][j+k-1]+
                       (i+k-1)*s[i+k-1][j]+(i+k-1)*s[i+k-1][j+k-1];

                 sumy-=j*s[i][j]+(j+k-1)*s[i][j+k-1]+
                       (j)*s[i+k-1][j]+(j+k-1)*s[i+k-1][j+k-1];

                 pp-=s[i][j]+s[i][j+k-1]+
                       s[i+k-1][j]+s[i+k-1][j+k-1];
                 if (sumx*2==(i+i+k-1)*(pp)&&
                     sumy*2==(j+j+k-1)*(pp))
                     {
                         if (k>ans) ans=k;
                     }
                 //printf("%d %d %d\n",sumx,sumy,pp);
                 //printf("%.2f %.2f\n",sumx*1.0/pp,sumy*1.0/pp);
             }
         }
         if (ans==0) printf("Case #%d: IMPOSSIBLE\n",ll); else
         printf("Case #%d: %d\n",ll,ans);
    }
    return 0;
}
