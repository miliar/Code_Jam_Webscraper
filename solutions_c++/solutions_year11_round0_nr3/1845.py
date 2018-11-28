#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
int ar[10000];

int main()
{
    int tst,cas;
    freopen("C.in","rt",stdin);
    freopen("C.out","wt",stdout);
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        scanf("%d",&n);
        int no=0,sum=0;
        int mn=100000000;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&ar[i]);
            no=(no^(ar[i]));
            sum+=ar[i];
            if(ar[i]<mn) mn=ar[i];
        }
        printf("Case #%d: ",cas);
        if(no!=0)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n",sum-mn);
        }
    }
    return 0;
}
