#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        int N, r1=1, r2=1, t1=0, t2=0, res = 0;
        scanf("%d",&N);
        for (int i=0;i<N;++i)
        {
            char R;
            int P;
            scanf(" %c%d",&R,&P);
            if (R=='O')
            {
                int nt = abs(r1-P);
                if (nt<=res-t1)
                    t1 = ++res;
                else
                    t1 = res = t1+nt+1;
                r1 = P;
            }
            else
            {
                int nt = abs(r2-P);
                if (nt<=res-t2)
                    t2 = ++res;
                else
                    t2 = res = t2+nt+1;
                r2 = P;
            }
        }
        printf("Case #%d: %d\n",t,res);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
