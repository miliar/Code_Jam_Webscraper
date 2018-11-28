#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
const long N = 50005 ,INF=1<<28;
const double eps = 1e-6,pi=acos(-1);

long min(long a,long b)
{return a<b?a:b;}
long max(long a,long b)
{return a>b?a:b;}
void swap(long &a,long &b)
{long tt;tt=a,a=b,b=tt;}
long n,a[N],m;
char s[N],s2[N];
void Init()
{
    scanf("%ld",&n);
    scanf("%s",s);
}
void Solve()
{
    long i,j,k;
    long all=1;
    long ans =INF;
    for(i=1;i<=n;i++)all*=i;
    for(i=0;i<n;i++)a[i]=i;
  //  printf("all : %ld\n",all);
    m=strlen(s);
    for(i=0;i<all;i++)
    {
        for(j=0;j<m;j+=n)
        {
            for(k=0;k<n;k++)
                s2[j+k]=s[j+a[k]];
        }
        long ct = 1;
        for(j=1;j<m;j++)
            if(s2[j]!=s2[j-1])ct++;
        ans<?=ct;
        next_permutation(a,a+n);
    }
    printf("%ld\n",ans);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T,K=1;
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
