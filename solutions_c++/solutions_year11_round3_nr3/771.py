#include<cmath>
#include<cstdio>
#include<cstring>
#include<map>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;

#define minn(x,y) ((x)<(y)?(x):(y))
#define maxx(x,y) ((x)>(y)?(x):(y))

int T,N,L,H;
int p[105];
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("a.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N>>L>>H;
        for(int i=1;i<=N;i++)
        {
            scanf("%d",p+i);
        }

        int ans=-1;
        for(int i=L;i<=H;i++)
        {
            bool ch=true;
            for(int j=1;j<=N;j++)
            {
                if(!(i%p[j]==0||p[j]%i==0))
                {
                    ch=false;
                    break;
                }
            }
            if(ch)
            {
                ans=i;
                break;
            }
        }

        if(ans==-1)
        {
            printf("Case #%d: NO\n",ca);
        }
        else
        {
            printf("Case #%d: %d\n",ca,ans);
        }
    }
    return 0;
}








