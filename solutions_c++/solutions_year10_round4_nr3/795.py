#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int t,n;
int map1[105][105];
int map2[105][105];
int ans;
int x1,x2,y2;
int y;

int main()
{
    int i,j,k;
    int i1,j1;
    freopen("C-small-attempt0.in","r",stdin);
  //   freopen("A-small-attempt1.in","r",stdin);
  //  freopen("A-small-attempt2.in","r",stdin);
  //  freopen("A-large.in","r",stdin);
    freopen("Cout.txt","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        memset(map1,0,sizeof(map1));
        memset(map2,0,sizeof(map2));
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d %d %d %d",&x1,&y,&x2,&y2);
            for(i1=x1;i1<=x2;i1++)
                for(j1=y;j1<=y2;j1++)
                    map1[i1][j1]=1;
        }
        ans=0;
        while(1)
        {
            int flag=0;
            for(i=1;i<=100;i++)
                for(j=1;j<=100;j++)
                    if(map1[i][j]==1)
                        flag=1;
            if(flag==0)
                break;
            for(i=1;i<=100;i++)
                for(j=1;j<=100;j++)
                {
                    if(map1[i][j]==1)
                    {
                        if(map1[i-1][j]==1||map1[i][j-1]==1)
                            map2[i][j]=1;
                        else
                            map2[i][j]=0;
                    }
                    if(map1[i][j]==0)
                    {
                        if(map1[i-1][j]==0||map1[i][j-1]==0)
                            map2[i][j]=0;
                        else
                            map2[i][j]=1;
                    }
                }
            ans++;
            for(i=1;i<=100;i++)
                for(j=1;j<=100;j++)
                    map1[i][j]=map2[i][j];
            
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
