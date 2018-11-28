#include<stdio.h>
#include<algorithm>

using namespace std;


#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int T; scanf("%d",&T);

    REP(kase,1,T)
    {
        int n; scanf("%d",&n);
        int XOR = 0;
        int sum = 0, mn = -1;

        FOR(i,n)
        {
            int A;
            scanf("%d",&A);
            XOR = XOR^A;
            sum += A;
            if(mn==-1)
                mn = A;
            else
                mn = min(A,mn);
        }

        printf("Case #%d: ",kase);
        if(XOR != 0)
        {
            puts("NO");
        }
        else
        {
            printf("%d\n",sum-mn);
        }
    }

    return 0;
}
