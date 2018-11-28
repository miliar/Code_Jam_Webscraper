#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int n;
long long l,h,ans,res;
long long a[10005],ll[10005],gg[10005];

long long gcd(long long a,long long b)
{
  while(b) { long long t=a%b; a=b; b=t; }
  return a;
}

long long mulmod(const long long &a,long long b,const long long &n)
{
  long long res=0,tmp=a%n;
  while(b>0)
  {
    if (b&1)
      if ((res+=tmp)>n) res-=n; 
    if ((tmp<<=1)>n) tmp-=n;
    b>>=1;
  }
  return res;
}

long long pow(long long a,long long d,const long long &n)
{ 
  long long res=1;
  while (d>0)
  { 
    if (d&1) res=mulmod(res,a,n);
    a=mulmod(a,a,n); 
    d>>=1; 
  }
  return res; 
}


const int prime[]={0,2,3,5,7,11,13,17,19,23};
bool millerrabin(long long n)
{
  if (n==2) return true;
  if (n<2||!(n&1)) return false;
  int s,k,i;
  long long d;
  for(s=0,d=n-1;!(d&1);s++,d>>=1);
  for(k=1;k<=9&&prime[k]<n;k++)
  {
    long long x=pow(prime[k],d,n);
    if (x==1) continue;
    for(i=1;i<s&&x!=n-1;i++)
      x=mulmod(x,x,n);
    if (x!=n-1) return false;
  }
  return true;
}

long long pollardrho(long long n)//n>1 and n is not a prime number
{
  for(int k=1;k<=9&&prime[k]<n;k++)
    if (n%prime[k]==0) return prime[k];
  long long x=rand()%n;
  long long y=x,d;
  while(true)
  {
    x=rand()%n;
    y=(mulmod(x,x,n)+1)%n;
    d=gcd((y+n-x)%n,n);
    while(d==1)
    {
      x=(mulmod(x,x,n)+1)%n;
      y=(mulmod(y,y,n)+1)%n;
      y=(mulmod(y,y,n)+1)%n;
      d=gcd((y+n-x)%n,n)%n;
    }
    if (d) break;
  }
  return d;
}

long long p[80],s[80];
int m;

void sub(long long x)
{
    if (millerrabin(x))
    {
        p[++m]=x;
        return;
    }
    long long d=pollardrho(x);
    sub(d);
    sub(x/d);
}

void sear(int t,long long k,long long cur)
{
    if (cur>=res) return;
    if (cur>=k)
    {
        res=cur;
        return;
    }
    if (t>m) return;
    sear(t+1,k,cur);
    for(int i=1;i<=s[t];++i)
    {
        if (p[t]>res/cur)
            break;
        cur*=p[t];
        sear(t+1,k,cur);
    }
}

long long find(long long x,long long k)
{
    res=x;
    m=0;
    if (x>1)
        sub(x);
    p[0]=1;
    sort(p+1,p+m+1);
    int i,j=0;
    for(i=1;i<=m;++i)
        if (p[i]==p[j])
            ++s[j];
        else
        {
           ++j;
           p[j]=p[i];
           s[j]=1;
        }
    m=j;
    sear(1,k,1);
    return res;
}

int main(void)
{
    int u,T,i;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    long long t,ans,ft;
    scanf("%d",&T);
    for(u=1;u<=T;++u)
    {
        scanf("%d%I64d%I64d",&n,&l,&h);
        for(i=1;i<=n;++i)
            scanf("%I64d",a+i);
        sort(a+1,a+n+1);
        ll[0]=1;
        for(i=1;i<=n;++i)
        {
            t=ll[i-1]/gcd(ll[i-1],a[i]);
            if (a[i]<=h/t)
                ll[i]=a[i]*t;
            else ll[i]=h+1;
        }
        gg[n]=a[n];
        for(i=n-1;i>=1;--i)
            gg[i]=gcd(a[i],gg[i+1]);
        ans=h+1;
        gg[n+1]=h/ll[n]*ll[n];
        for(i=1;i<=n+1;++i)
        {
            if (ll[i-1]>h)
                break;
            if (gg[i]%ll[i-1]!=0)
                continue;
            if (ll[i-1]>l)
                t=ll[i-1];
            else
            {
                t=(l+ll[i-1]-1)/ll[i-1];
                ft=gg[i]/ll[i-1];
                if (t>ft)
                    continue;
                t=find(ft,t)*ll[i-1];
            }
            ans=min(t,ans);
        }
        if (ans>h)
            printf("Case #%d: NO\n",u);
        else printf("Case #%d: %I64d\n",u,ans);
    }
    return 0;
}
