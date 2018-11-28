#include<iostream>
using namespace std;
int a[3000][3000];
int b1[3000],b2[3000];
int ans[3000];
int main()
{
    int casen;
    int m,n;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d",&n);
        scanf("%d",&m);
        int t;
        memset(a,0,sizeof(a));
        memset(b1,0,sizeof(b1));
        memset(b2,0,sizeof(b2));
        for (int i=1;i<=m;i++)
        {
            scanf("%d",&t);
            int x,y;
            for (int j=1;j<=t;j++)
            {
                scanf("%d%d",&x,&y);
                a[i][x]=y+1;
                if (y==0)b1[i]++;else b2[i]=x;
            }
        }
        memset(ans,0,sizeof(ans));
        bool find=true;
        bool find1=false;
        while(find)
        {
                   find=false;
                   int ii=0;
                   for (int i=1;i<=m;i++)
                     if (b1[i]==0)
                     {
                                  if (b2[i]!=0){find=true;ii=b2[i];break;}
                                  else {find1=true;break;}
                     }
                   if (find1)break;
                   ans[ii]=1;
                   for (int i=1;i<=m;i++)
                   {
                       if (a[i][ii]==1)b1[i]--;
                       if (a[i][ii]==2)b1[i]++;
                   }
        }
        printf("Case #%d:",casei);
        if (find1)printf(" IMPOSSIBLE");
        else
          for (int i=1;i<=n;i++)
            printf(" %d",ans[i]);
        printf("\n");
    }
    return 0;
}
              
        
                   
                   
