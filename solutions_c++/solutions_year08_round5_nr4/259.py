#include<stdio.h>
#include<memory.h>
#include<set>
#include<map>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>
#include<iostream>
using namespace std;

int c[110][110],li[110][110],n1,i1,r,x,y,i,j,h,w;

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d %d %d",&h,&w,&r);
        memset(c,0,sizeof(c));
        for(i=1;i<=r;i++)
        {
            scanf("%d %d",&x,&y);
            c[x][y]=1;
        }
        memset(li,0,sizeof(li));
        li[1][1]=1;
        for(i=1;i<=h;i++)
            for(j=1;j<=w;j++)
            {
                if(c[i][j]!=1)
                {
                    li[i+1][j+2]+=li[i][j];
                    li[i+1][j+2]=li[i+1][j+2]%10007;
                    li[i+2][j+1]+=li[i][j];
                    li[i+2][j+1]=li[i+2][j+1]%10007;
                }
            }
        if(c[h][w]==1)
            li[h][w]=0;
        printf("Case #%d: %d\n",i1,li[h][w]);
    }
    return 0;
}       
