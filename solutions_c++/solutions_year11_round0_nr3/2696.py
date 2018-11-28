#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const int maxn=1000+2;
int T, N, ans, sum;
int A[maxn];

void getin()
{
    scanf("%d",&N);
    sum=0;
    for (int i=1;i<=N;i++) 
    {
        scanf("%d",&A[i]);
        sum+=A[i];
    }
}

void work()
{
    ans=0;
    sort(A+1, A+1+N);
    for (int i=1;i<=N;i++) ans = ans ^ A[i];
    if (ans!=0) printf("NO\n");
    else 
    {
        ans=sum-A[1];
        printf("%d\n",ans);
    }
}

int main()
{
//    freopen("yy.in","r",stdin);
//    freopen("yy.out","w",stdout);
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);    
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        printf("Case #%d: ",ii);
        getin();
        work();
    }
    return 0;
}
