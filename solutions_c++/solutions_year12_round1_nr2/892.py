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
    int at,a,b;
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


bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.a < j.a ) return true;
    if( j.a < i.a ) return false;
    return i.b>j.b;
}


data a[2][1000];
int visit[1000][2],ans,globFlag;


int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       REP(i,n) {
           si(a[0][i].a);
           si(a[1][i].a);
           a[0][i].at=i;
           a[0][i].b=a[1][i].a;
           a[1][i].at=i;
           a[1][i].b=0;
       }
       ans=0;
       //sort(a[0],a[0]+n,myfunction);
       sort(a[1],a[1]+n,myfunction);
       memset(visit,0,sizeof(visit[0][0])*1000*2);
       int e=0,atx=n-1,aty=0,cnt=0;
       while(aty!=n) {
           while(aty<n && e>=a[1][aty].a) {
               data temp = a[1][aty];
               visit[temp.at][1]=1;
               int add=1;
               if(visit[temp.at][0]==0) {
                   add++;
               }
               e+=add;
               aty++;
               ans++;
           }
           if(aty==n) {
               break;
           }
           atx=n-1;
           while(atx>=aty) {
               int at = a[1][atx].at;
               if(a[0][at].a<=e && visit[at][0]==0) {
                   break;
               }
               atx--;
           }
           if(atx<aty) {
               break;
           }
           int at = a[1][atx].at;
           visit[at][0]=1;
           ans++;
           e+=1;
           //cnt++;
       }

       if(aty==n) {
           printf("Case #%d: %d\n",prob+1,ans);
       } else {
           printf("Case #%d: Too Bad\n",prob+1);
       }
   }
   //system("pause");
   return 0;

}
