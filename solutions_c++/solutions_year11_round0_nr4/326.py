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

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       n=ni();
       int temp;
       float cnt=0;
       REP(i,n)
       {
           temp=ni();
           if(temp!=i+1)
           cnt+=1;
       }
       printf("Case #%d: %.6f\n",prob+1,cnt);
   }


   //system("pause");
   return 0;

}
