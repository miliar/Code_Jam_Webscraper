#include <cstdio>
#include <iostream>
using namespace std;

int g[1005];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int T,R,K,N;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d%d",&R,&K,&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&g[i]);
        }
        int curpos=0,tmppos,prevpos;
        int sum=0;
        int total=0;
        for(int i=0;i<R;i++)
        {
            tmppos=curpos;
            prevpos=-1;
            while(sum+g[curpos]<=K && curpos!=prevpos)
            {
                sum+=g[curpos];
                curpos++;
                curpos%=N;
                prevpos=tmppos;
            }
            total+=sum;
            sum=0;
        }
        printf("Case #%d: %d\n",t,total);
    }
    return 0;
}
