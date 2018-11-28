#include<iostream>
using namespace std;

int g[1005];

int main()
{
    int T;
    scanf("%d",&T);
    for(int TestNum=1 ; TestNum<=T ;TestNum++)
    {
        int R,N,K,total=0;
        scanf("%d%d%d",&R,&K,&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&g[i]);
            total+=g[i];
        }
        int sum=0;
        if(total<=K)
        {   
            sum=total*R;
        }
        else
        {
            int next=0;
            while(R--)
            {
                int hold=0;
                while(hold+g[next]<=K)
                {
                    hold+=g[next];
                    next=((next+1)%N);
                }
                sum+=hold;
            }
        }
        printf("Case #%d: %d\n",TestNum,sum);

    }

}
