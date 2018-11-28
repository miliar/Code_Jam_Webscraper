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

int t,n,s,p;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

int a[100],b[100][2],dp[100][101];

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       si(s);
       si(p);
       REP(i,n) {
           si(a[i]);
       }
       REP(i,n) {
           int at=a[i];
           b[i][0]=0;
           b[i][1]=0;
           FOR(q,p,11) {
               if((q>0 && q+2*(q-1)==at) || (q>0 && 2*q+q-1==at) || 3*q==at) {
                   b[i][0]=1;
               }
               if(q>1 && (q+q-1+q-2==at || q+2*(q-2)==at || 2*q+q-2==at)) {
                   b[i][1]=1;
               }
           }
           //cout<<b[i][0]<<" "<<b[i][1]<<endl;
       }
       REP(i,s+1) {
           dp[0][i]=0;
       }
       dp[0][0]=b[0][0];
       dp[0][1]=b[0][1];
       FOR(i,1,n) {
           dp[i][0]=dp[i-1][0];
           if(b[i][0]==1) {
               dp[i][0]++;
           }
           FOR(j,1,s+1) {
               dp[i][j]=dp[i-1][j-1];
               if(b[i][1]==1) {
                   dp[i][j]++;
               }
               int temp=dp[i-1][j];
               if(b[i][0]==1) {
                   temp++;
               }
               if(temp>dp[i][j]) {
                   dp[i][j]=temp;
               }
           }
       }
       printf("Case #%d: %d\n",prob+1,dp[n-1][s]);
   }

   //system("pause");
   return 0;

}
