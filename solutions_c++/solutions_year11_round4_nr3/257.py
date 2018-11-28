#include<iostream>
using namespace std;
const int maxn=1001000;
int p[maxn],a[maxn];
int m;
long long n;
int prime(int x)
{
    int i;
    for (i=2;i*i<=x;i++)
    if (x%i==0) return 0;
    return 1;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int i,j,k,l,ans1,ans2,ck,ans;
    int cases,tt;
    for (i=2;i<=1000000;i++)
    if (prime(i))
    {
       p[m]=i;
       m++;
    }
    long long t;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%lld",&n);
        ans=1;
        for (i=0;i<m;i++)
        {
            t=p[i];
            while (1)
            {
                  t*=p[i];
                  if (t>n) break;
                  ans++;
            }
        }
        if (n==1) ans=0;
        printf("Case #%d: %d\n",tt+1,ans);
    }
    return 0;
}
