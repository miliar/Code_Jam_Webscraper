#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;


int t,r,c;
char mp[55][55];
bool flag[55][55];

bool ok(int x,int y)
{
    if(x<r&&y<c&&flag[x][y]==0&&mp[x][y]=='#')
        return 1;
    return 0;
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("al1.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    int cnt=1;
    while(t--)
    {
        memset(flag,0,sizeof(flag));
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++)
            scanf("%s",mp[i]);
        printf("Case #%d:\n",cnt++);
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(ok(i,j)&&ok(i+1,j)&&ok(i,j+1)&&ok(i+1,j+1))
                {
                    //printf("  %d %d\n",i,j);
                    mp[i][j]=mp[i+1][j+1]='/';
                    mp[i+1][j]=mp[i][j+1]='\\';
                    flag[i][j]=flag[i+1][j+1]=flag[i+1][j]=flag[i][j+1]=1;
                }
            }
        }
        int flagg=0;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(mp[i][j]=='#')
                    flagg=1;
            }
        }
        if(flagg==1)
            printf("Impossible\n");
        else
        {
            for(i=0;i<r;i++)
                printf("%s\n",mp[i]);
        }
    }
    //system("pause");
    return 0;
}
