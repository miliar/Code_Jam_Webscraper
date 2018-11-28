#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

#define minn(x,y) ((x)<(y)?(x):(y))
#define maxx(x,y) ((x)>(y)?(x):(y))

int T,N,S,M,Sum;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        S=0,M=1000000000,Sum=0;
        int x;
        for(int i=1;i<=N;i++)
        {
            scanf("%d",&x);
            Sum+=x;
            if(x<M) M=x;
            S=S^x;
        }

        if(S==0)
        {
            int ans=Sum-M;
            printf("Case #%d: %d\n",ca,ans);
        }
        else
        {
            printf("Case #%d: NO\n",ca);
        }
    }
    return 0;
}

































