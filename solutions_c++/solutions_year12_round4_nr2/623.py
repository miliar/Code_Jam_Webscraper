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
    ll x,y;
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
ll w,l;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

ll a[10000],visit[1000],flag;
data ans[1000],tans[1000];

void see(int at, ll nw, ll tw, ll tl) {
    if(at==n) {
        flag=1;
        memcpy(ans,tans,sizeof(tans[0])*1000);
        return;
    }

    if(at==0) {
        REP(i,n) {
            if(flag) {
                return;
            }
            visit[i]=1;
            tans[i].x=0;
            tans[i].y=0;
            see(1,a[i],-1000000000,a[i]);
            visit[i]=0;
        }
        return;
    }

    REP(i,n) {
        if(flag) {
            return;
        }
        if(!visit[i]) {
            if(tl+a[i]<=l) {
                tans[i].x=max(0LL,tw+a[i]);
                tans[i].y=tl+a[i];
                visit[i]=1;
                see(at+1,max(nw,tans[i].x+a[i]),tw,tl+2*a[i]);
                visit[i]=0;
            } else if(nw+a[i]<=w) {
                tans[i].x=nw+a[i];
                tans[i].y=0;
                visit[i]=1;
                see(at+1,nw+2*a[i],nw,a[i]);
                visit[i]=0;
            }
        }
    }
}

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       sl(w);
       sl(l);
       REP(i,n) {
           sl(a[i]);
       }
       memset(visit,0,sizeof(visit[0])*1000);
       flag=0;
       see(0,0,0,0);
       if(!flag) {
           cout<<"NOOOOOOOOOOOOOOOO"<<endl;
       }
       /*
       if(!flag) {
           see2(0,0,0,0);
       }
       */
       printf("Case #%d: ",prob+1);
       REP(i,n) {
           printf("%lld %lld ",ans[i].x,ans[i].y);
       }
       printf("\n");
   }

   //system("pause");
   return 0;

}
