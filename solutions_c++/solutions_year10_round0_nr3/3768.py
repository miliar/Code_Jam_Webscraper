#include<iostream>
#include<queue>
using namespace std;
int R,K,N;
queue<int>g;
queue<int >fu;
int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    int T,i,Case=0,a;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&R,&K,&N);
        for(i=0;i<N;i++)
        {
            scanf("%d",&a);
            g.push(a);
        }
        __int64 sum=0;__int64 ans=0;
        for(i=1;i<=R;i++)
        {
            while(!g.empty()&&sum+g.front()<=K)
            {
                int tem=g.front();g.pop();
                sum+=tem;fu.push(tem);
            }
            ans+=sum;sum=0;
            while(!fu.empty())
            {
                int tem=fu.front();fu.pop();
                g.push(tem);
            }
        }
        printf("Case #%d: %d\n",++Case,ans);
        while(!g.empty())
            g.pop();
    }
    return 0;
}
