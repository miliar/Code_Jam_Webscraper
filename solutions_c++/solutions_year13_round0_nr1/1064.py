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
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

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

char s[10];
int a[5][5];

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++) {
       REP(i,4) {
           ss(s);
           REP(j,4) {
             if(s[j] == '.') {
               a[i][j]=0;
             } else if(s[j]=='X') {
               a[i][j]=1;
             } else if(s[j]=='O') {
               a[i][j]=2;
             } else {
               a[i][j]=3;
             }
           }
       }
       int win=0;

       // ROW ME
       REP(i,4) {
         int flag=0;
         REP(j,4) {
           if(a[i][j]==0 || a[i][j]==2) {
             flag=1;
             break;
           }
         }
         if(!flag) {
           win=1;
           break;
         }
       }
       REP(i,4) {
         int flag=0;
         REP(j,4) {
           if(a[i][j]==0 || a[i][j]==1) {
             flag=1;
             break;
           }
         }
         if(!flag) {
           win=2;
           break;
         }
       }

       // COL ME

       REP(j,4) {
         int flag=0;
         REP(i,4) {
           if(a[i][j]==0 || a[i][j]==2) {
             flag=1;
             break;
           }
         }
         if(!flag) {
           win=1;
           break;
         }
       }
       REP(j,4) {
         int flag=0;
         REP(i,4) {
           if(a[i][j]==0 || a[i][j]==1) {
             flag=1;
             break;
           }
         }
         if(!flag) {
           win=2;
           break;
         }
       }

       // DIG 1
       int flag=0;
       REP(i,4) {
         if(a[i][i]==0 || a[i][i]==2) {
           flag=1;
           break;
         }
       }
       if(!flag) {
         win=1;
       }
       flag=0;
       REP(i,4) {
         if(a[i][i]==0 || a[i][i]==1) {
           flag=1;
           break;
         }
       }
       if(!flag) {
         win=2;
       }

       // DIG 2
       flag=0;
       REP(i,4) {
         if(a[i][3-i]==0 || a[i][3-i]==2) {
           flag=1;
           break;
         }
       }
       if(!flag) {
         win=1;
       }
       flag=0;
       REP(i,4) {
         if(a[i][3-i]==0 || a[i][3-i]==1) {
           flag=1;
           break;
         }
       }
       if(!flag) {
         win=2;
       }


       if(win==0) {
         flag=0;
         REP(i,4) {
           REP(j,4) {
             if(a[i][j]==0) {
               flag=1;
               break;
             }
           }
         }
         if(!flag) {
           win=3;
         }
       }
       if(win==0) {
         printf("Case #%d: Game has not completed\n", prob+1);
       } else if(win==1) {
         printf("Case #%d: X won\n", prob+1);
       } else if(win==2) {
         printf("Case #%d: O won\n", prob+1);
       } else {
         printf("Case #%d: Draw\n",prob+1);
       }
   }

   //system("pause");
   return 0;

}
