#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;

//long long ans = 0;
int n, cases;
bool no[110][110];
int ans[110][110];
int x,y,h,w,r,a,b;
int main()
{
    freopen("D-small-attempt0.in", "rt", stdin);
    freopen("2.out", "wt", stdout);
    scanf("%d",&cases);
    for(int t=0; t<cases; t++)
    {
        
        for(x=0;x<110;x++)
        for(y=0;y<110;y++)
        {
            no[x][y]=0;
            ans[x][y]=0;
        }
        scanf("%d%d%d",&h,&w,&r);
        for(x=0;x<r;x++)
        {
            scanf("%d%d",&a,&b);
            no[a-1][b-1]=1;
        }
        ans[0][0]=1;
        for(x=0;x<h;x++)
        {
        for(y=0;y<w;y++)
        {
            if(no[x][y]==0)
            {
                ans[x+2][y+1]+=ans[x][y];
                ans[x+2][y+1]%=10007;
                ans[x+1][y+2]+=ans[x][y];
                ans[x+1][y+2]%=10007;
            }
          //  printf("%d ",ans[x][y]);
        }
       // printf("\n");
    }
//        ans =0;
        cout<<"Case #"<<t+1<<": "<<ans[h-1][w-1]<<endl;
    }
    return 0;
}
