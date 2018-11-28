using namespace std;
#include<cstdio>
#include<algorithm>
#define Lm 1000
int A[Lm],p,k,l;

inline bool cmp(int a, int b)
{
    return a>b;
}

long long solve()
{
    int i;
    long long ans=0;

    scanf("%d%d%d",&p,&k,&l);
    for(i=0;i<l;++i)
        scanf("%d",A+i);

    sort(A,A+l,cmp);
    for(i=0;i<l;++i)
        ans+=A[i]*(i/k+1);
    return ans;
}

int main()
{
    int n,i;
    
    freopen("text.in","r",stdin);
    freopen("text.out","w",stdout);

    scanf("%d",&n);
    for(i=1;i<=n;++i)
        printf("Case #%d: %lld\n",i,solve());
    
    return 0;
}

