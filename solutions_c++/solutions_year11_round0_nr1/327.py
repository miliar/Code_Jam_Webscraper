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

int a[100][2];
char c[10];

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       n=ni();
       REP(i,n)
       {
           scanf("%s",c);
           //cout<<c<<endl;
           if(c[0]=='O')
           a[i][0]=0;
           else
           a[i][0]=1;
           a[i][1]=ni();
       }
       int ans=0;
       int x=1,y=1,tx=0,ty=0;
       REP(i,n)
       {
           if(a[i][0]==0)
           {
               if(ans>tx)
               {
                   int temp=ans-tx;
                   if(a[i][1]>x)
                   x=min(x+temp,a[i][1]);
                   else
                   x=max(x-temp,a[i][1]);
                   tx=ans;
               }
               if(a[i][1]>x)
               {
                   ans+=(a[i][1]-x);
                   x=a[i][1];
                   tx=ans;
               }
               else if(a[i][1]<x)
               {
                   ans+=(x-a[i][1]);
                   x=a[i][1];
                   tx=ans;
               }
               tx++;
               ans++;
           }
           else
           {
               if(ans>ty)
               {
                   int temp=ans-ty;
                   if(a[i][1]>y)
                   y=min(y+temp,a[i][1]);
                   else
                   y=max(y-temp,a[i][1]);
                   ty=ans;
               }
               if(a[i][1]>y)
               {
                   ans+=(a[i][1]-y);
                   y=a[i][1];
                   ty=ans;
               }
               else if(a[i][1]<y)
               {
                   ans+=(y-a[i][1]);
                   y=a[i][1];
                   ty=ans;
               }
               ty++;
               ans++;
           }
           //cout<<ans<<endl;
       }
       printf("Case #%d: %d\n",prob+1,ans);
   }


   //system("pause");
   return 0;

}
