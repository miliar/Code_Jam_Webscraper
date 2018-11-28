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
#define EPSILON 0.0000000001

int t,n;
double d;

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

struct node
{
    double p;
    ll v;
};

bool myfunction(node i, node j )    //use it to sort vectors
{
    if( i.p > j.p ) return false;
    if( j.p < i.p ) return true;
}


node a[200];
double p[1000000],b[1000000],sum;

int check(double at)
{

    for(int i=0;i<(int)sum;i++)
    b[i]=p[i];


    b[0]-=at;

    double mini=b[0]+d;
    double lim=d;

    for(int i=1;i<(int)sum;i++)
    {
            if(b[i]<mini && mini>at+b[i])
            return 0;
            else if(b[i]<=mini)
            {
                 b[i]=mini;
                 mini+=lim;
            }
            else if(b[i]<=mini+at)
            {
                 b[i]=mini;
                 mini+=lim;
            }
            else
            {
                 b[i]-=at;
                 mini=b[i]+lim;
            }
    }
    return 1;
}



double see(double start,double end)
{

    if(end-start<EPSILON)
    return end;

    double mid=(start+end)/2;
    if(check(mid))
    return see(start,mid);
    return see(mid,end);
}


int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   //double sum;
   for(int prob=0;prob<t;prob++)
   {
       n=ni();
       d=nf();
       sum=0;

       REP(i,n)
       {
           a[i].p=nf();
           a[i].v=nl();
           sum+=a[i].v;
           //cout<<a[i].p<<endl;
       }
       //sort(a,a+n,myfunction);
       int at=0;
       REP(i,n)
       {
               REP(j,a[i].v)
               {
                   p[at]=a[i].p;
                   at++;
               }
       }
       double maxi=(sum)*d+sum;
       //cout<<maxi<<" "<<sum<<endl;
       double ans=see(0,maxi);
       //while(!check(ans));
       printf("Case #%d: %.6lf\n",prob+1,ans);
   }




   //system("pause");
   return 0;

}
