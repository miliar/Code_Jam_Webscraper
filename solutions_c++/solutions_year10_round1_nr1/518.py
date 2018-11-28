#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

const int N = 55;
int n,k;
char s[N][N];
char t[N][N];
int dx[]={1,0,-1,1,-1,1,0,-1};
int dy[]={1,1,1,0,0,-1,-1,-1};
bool ok(int x,int y)
{
    return x>=0&&y>=0&&x<n&&y<n;
}
bool ok(int x,int y,char z)
{
    for(int i=0;i<8;++i)
    {
        if((!ok(x-dx[i],y-dy[i])||t[x-dx[i]][y-dy[i]]!=z))
        //&&(!ok(x+dx[i]*k,y+dy[i]*k)||t[x+dx[i]*k][y+dy[i]*k]!=z))
        {
            bool flag = true;
            for(int j=0;j<k;++j)
            {
                if(!ok(x+dx[i]*j,y+dy[i]*j)||t[x+dx[i]*j][y+dy[i]*j]!=z)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)return true;
        }
    }
    return false;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,K=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;++i)
            scanf("%s",s[i]);
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<n;++j)
                t[i][j]='.';
            t[i][n]=0;
        }
        for(int i=0;i<n;++i)
        {
            int ptr=n-1;
            for(int j=n-1;j>=0;--j)
            {
                if(s[i][j]!='.')
                    t[i][ptr--]=s[i][j];
            }
        }
       // for(int i=0;i<n;++i)
       //     puts(t[i]);
       //     puts("");
        int ans = 0;
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<n;++j)
            {
                if(ok(i,j,'R'))
                    ans|=1;
                if(ok(i,j,'B'))
                    ans|=2;
            }
        }
        if(ans == 0)
            printf("Case #%d: Neither\n",K++);
        else if(ans == 1)
            printf("Case #%d: Red\n",K++);
        else if(ans == 2)
            printf("Case #%d: Blue\n",K++);
        else printf("Case #%d: Both\n",K++);
    }
    return 0;
}
