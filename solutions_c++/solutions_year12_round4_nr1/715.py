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

struct data {
    ll d,l;
};

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

int t,n;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

data a[100000];
ll r[100000],d;

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       REP(i,n) {
           sl(a[i].d);
           sl(a[i].l);
       }
       sl(d);
       int ans=0;
       if(a[0].l>=a[0].d) {
           REP(i,n) {
               r[i]=-1;
           }
           r[0]=a[0].d;
           int at=0;
           while(at!=n) {
               ll l=r[at];
               if(l==-1) {
                   break;
               }
               if(d-a[at].d<=l) {
                   ans=1;
                   break;
               }
               int see=at+1;
               while(see!=n) {
                   if(a[see].d-a[at].d<=l) {
                       ll temp=a[see].d-a[at].d;
                       if(a[see].l<temp) {
                           temp=a[see].l;
                       }
                       r[see]=max(temp,r[see]);
                   } else {
                       break;
                   }
                   see++;
               }

               at++;
           }
       }
       if(ans) {
           printf("Case #%d: YES\n",prob+1);
       } else {
           printf("Case #%d: NO\n",prob+1);
       }
   }

   //system("pause");
   return 0;

}
