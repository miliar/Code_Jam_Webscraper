#include<stdio.h>
#include<algorithm>
using namespace std;

int a[800],b[800];
int N;

int main()
{
    int i,T,j;
    __int64 ans;
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&N);
        for(j=0;j<N;j++)
            scanf("%d",&a[j]);
        for(j=0;j<N;j++)
            scanf("%d",&b[j]);
        sort(a,a+N);
        sort(b,b+N);
        ans=0;
        for(j=0;j<N;j++)
            ans+=(__int64)a[j]*(__int64)b[N-1-j];
        printf("Case #%d: %I64d\n",i,ans);
    }
    //scanf("%d",&N);
    return 0;
}
