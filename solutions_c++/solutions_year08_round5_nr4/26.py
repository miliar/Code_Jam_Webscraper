#include <cstdio>
#include <iostream>
#include <memory>
#define MAXH 100
#define MAXW 100
using namespace std;

bool board[MAXH+1][MAXW+1];
int dp[MAXH+1][MAXW+1];
int h,w,r;

bool valid(int x,int y)
{
    if((x>=1)&&(x<=h)&&(y>=1)&&(y<=w))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int i,k,t,x,y;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        memset(board,0,sizeof(board));
        memset(dp,0,sizeof(dp));
        scanf("%d %d %d",&h,&w,&r);
        for(i=0;i<r;i++)
        {
            scanf("%d %d",&x,&y);
            board[x][y]=true;
        }
        dp[1][1]=1;
        for(i=2;i<=h+w;i++)
        {
            for(x=1;x<=h;x++)
            {
                y=i-x;
                if((y>=1)&&(y<=w)&&(dp[x][y]!=0))
                {
                    if((valid(x+1,y+2)==true)&&(board[x+1][y+2]==false))
                    {
                        dp[x+1][y+2]=(dp[x+1][y+2]+dp[x][y])%10007;
                    }
                    if((valid(x+2,y+1)==true)&&(board[x+2][y+1]==false)) 
                    {
                        dp[x+2][y+1]=(dp[x+2][y+1]+dp[x][y])%10007;
                    }
                }
            }
		}
		printf("Case #%d: %d\n",k+1,dp[h][w]);
	}
	return 0;
}
