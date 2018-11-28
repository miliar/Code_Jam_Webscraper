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

int t,n;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

double a[200],s,b[200];

int see(int at, double x) {
    REP(i,n) {
        b[i]=a[i];
    }
    b[at]+=((s*x));
    double top=b[at];
    double sum=0;
    REP(i,n) {
        if(i!=at && b[i]<top) {
            sum+=(top-b[i]);
        }
    }
    if(sum<s*(1-x)) {
        return 0;
    }
    return 1;
}

double binary(int at, double start, double end) {
    if(end-start<1e-8) {
        return start;
    }

    double mid=(start+end)/2;
    if(see(at,mid)) {
        return binary(at,start,mid);
    } else {
        return binary(at,mid,end);
    }
}

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   double temp=1e-6;
   //cout<<temp<<endl;
   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       REP(i,n) {
           sd(a[i]);
       }
       s=0;
       REP(i,n) {
           s+=a[i];
       }
       printf("Case #%d: ",prob+1);
       REP(i,n) {
           printf("%.6lf ",binary(i,0,1)*100);
       }
       printf("\n");
   }

   //system("pause");
   return 0;

}
