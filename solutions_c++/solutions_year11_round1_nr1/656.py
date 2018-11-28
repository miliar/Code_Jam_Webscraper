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


int t;
ll n;

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

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       n=nl();
       int pd=ni();
       int pg=ni();
       ll g=1;
       if(pd!=0)
       g=gcd(pd,100);
       if((pg==100 && pd!=100) || (pd!=0 && pg==0) || (pd!=0 && (100/g)>n))
       printf("Case #%d: Broken\n",prob+1);
       else
       printf("Case #%d: Possible\n",prob+1);
   }



   //system("pause");
   return 0;

}
