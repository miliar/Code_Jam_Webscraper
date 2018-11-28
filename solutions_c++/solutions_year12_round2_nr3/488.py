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
    ll a[20];
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

ll a[500];
int flag,b[500];
map<ll,data>m;

void see(int at, ll s) {
    if(flag) {
        return;
    }
    if(at==n) {
        if(s!=0 && m.find(s)!=m.end()) {
            flag=1;
            data temp = m[s];
            REP(i,n) {
                if(temp.a[i]) {
                    printf("%lld ",a[i]);
                }
            }
            printf("\n");
            REP(i,n) {
                if(b[i]) {
                    printf("%lld ",a[i]);
                }
            }
            printf("\n");
        } else if(s!=0) {
            data temp;
            REP(i,n) {
                temp.a[i]=b[i];
            }
            m[s]=temp;
        }
        return;
    }

    see(at+1,s);
    if(flag) {
        return;
    }
    b[at]=1;
    see(at+1,s+a[at]);
    b[at]=0;
}

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       si(n);
       REP(i,n) {
           sl(a[i]);
       }
       flag=0;
       printf("Case #%d:\n",prob+1);
       m.erase(m.begin(),m.end());
       REP(i,n) {
           b[i]=0;
       }
       see(0,0);
       if(!flag) {
           printf("Impossible\n");
       }
   }

   //system("pause");
   return 0;

}
