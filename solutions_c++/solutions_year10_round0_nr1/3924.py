#include <cstdio>
#include <vector>
using namespace std;
bool l[31];

int main()
{
    long int T;
    scanf("%ld",&T);
    for(long int cnt=1;cnt<=T;cnt++)
    {
        int N,K;
        scanf("%d %d",&N,&K);
        if(K == 0 || K<N)
            printf("Case #%ld: OFF\n",cnt);
        else
        {
            int exp = 1;
            for(int i=1;i<=N;i++)
                exp = exp * 2;
            if((K+1)%exp == 0)
                printf("Case #%ld: ON\n",cnt);
            else
                printf("Case #%ld: OFF\n",cnt);

        }
    }
    return 0;
}
