#include <iostream>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int Case=1;T;T--,Case++)
    {
        printf("Case #%d: ",Case);
        int R,K,N,G[1001];
        int Next[1001];
        int Cost[1001];
        scanf("%d%d%d",&R,&K,&N);
        for(int j=1;j<=N;j++)
            scanf("%d",&G[j]);
        for(int i=1;i<=N;i++)
        {
            Next[i] = -1;
            int Left = K;
            for(int j=i;j<=N;j++)
            {
                if(Left < G[j])
                {
                    Next[i] = j;
                    Cost[i] = K - Left;
                    break;
                }
                Left -= G[j];
            }
            if(Next[i] == -1)
            {
                for(int j=1;j<i;j++)
                {
                    if(Left < G[j])
                    {
                        Next[i] = j;
                        Cost[i] = K - Left;
                        break;
                    }   
                    Left -= G[j];
                }
            }
            if(Next[i] == -1)
            {
                Next[i] = i;
                Cost[i] = K - Left;
            }
        }
        int Cur = 1;
        long long Ans = 0;
        for(int i=1;i<=R;i++)
        {
            Ans = Ans + (long long)Cost[Cur];
            Cur = Next[Cur];
        }
        cout<<Ans<<'\n';
    }
    return 0;
}
