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


int t,n;
ll l,h;

int ni()
{
    int temp;
    scanf("%d",&temp);
    return temp;
}

ll nl()
{
    ll temp;
    scanf("%lld",&temp);
    return temp;
}

llu nlu()
{
    llu temp;
    scanf("%llu",&temp);
    return temp;
}

float nf()
{
    float temp;
    scanf("%f",&temp);
    return temp;
}
/*
bool myfunction( const node& i, const node& j )    //use it to sort vectors
{
    if( i.x < j.x ) return false;
    if( j.x < i.x ) return true;
    return j.c < i.c;
}
*/

/* GCD of two numbers */
long long unsigned int gcd(long long unsigned int r0,long long unsigned int r1)
{
    long long unsigned int temp;
    if(r0==0 || r1==0)
    return 1;
    if(r0<r1)
              {
                   temp = r0;
                   r0 = r1;
                   r1=temp;
              }

    //r0 is the larger number and r1 is the smaller number
    long long unsigned int remainder;

    do{
        remainder = r0%r1;

        r0=r1;
        r1=remainder;
        }while(remainder!=0);

    return r0;
}

ll g;
int a[10000];
ll fac[10000][2],fi,mini;

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       n=ni();
       l=nl();
       h=nl();
       mini=10000*10000;
       mini*=mini;
       mini+=1;
       //cout<<mini<<endl;
       REP(i,n)
       {
           a[i]=nl();

       }

       FOR(i,l,h+1)
       {
           int ans=0;
           REP(j,n)
           {
               if(a[j]%i!=0 && i%a[j]!=0)
               {
                   ans=1;
                   break;
               }
           }
           if(ans==0)
           {
               mini=i;
               break;
           }
       }
       if(mini>h)
       printf("Case #%d: NO\n",prob+1);
       else
       printf("Case #%d: %lld\n",prob+1,mini);
   }





   //system("pause");
   return 0;

}
