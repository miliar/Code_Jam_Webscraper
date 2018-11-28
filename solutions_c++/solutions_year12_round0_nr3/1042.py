#include<iostream>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    ll i = 2;
    for (; (b % (a%b)) != 0; i++)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[i % 3] = (quotient * -1 * x[(i - 1) % 3]) + x[(i - 2) % 3];
        y[i % 3] = (quotient * -1 * y[(i - 1) % 3]) + y[(i - 2) % 3];
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[(i - 1) % 3];
}

int t,n,m;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/
int p[8],a[10000000],b[10000000],bi;

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   p[0]=1;
   FOR(i,1,8) {
       p[i]=p[i-1]*10;
   }
   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       si(m);
       int l=0;
       int at=n;
       while(at) {
           l++;
           at/=10;
       }
       ll ans=0;
       FOR(i,n,m+1) {
           //memset(a, 0, sizeof(a[0]) * 10000000);
           bi=0;
           FOR(j,1,l) {
               int div=p[j];
               int at=i/div+(i%div)*p[l-j];
               if(at>=n && at<=m && at>i && (i/p[j-1])%10!=0 && a[at-n]==0) {
                   //cout<<i<<" "<<at<<endl;
                   a[at-n]=1;
                   b[bi]=at-n;
                   bi++;
                   ans++;
               }
           }
           REP(i,bi) {
               a[b[i]]=0;
           }
       }
       printf("Case #%d: %lld\n",prob+1,ans);
   }



   //system("pause");
   return 0;

}
