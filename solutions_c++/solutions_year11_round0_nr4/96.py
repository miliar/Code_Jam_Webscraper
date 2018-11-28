#include <algorithm>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <set>
using namespace std;
int a;
double memo[10001];
long long fact[10001];

double X[10000];
double x(int n)
{
   if(  n<2 )    return 0.0;
   if(n==2) return .5;
   if( X[n]>=-.1  ) return X[n];
   double sum=0.0;
   sum=(n-1)*(  x(n-1)/(double)n+x(n-2)/(double)(n*(n-1)) );
   return X[n]=sum;
}

double mem(int n)
{
    if(n<2) return 0.0;
    if(n==2) return 2.0;
    if( memo[n]>=-.1 ) return memo[n];
    double res=0;
    for(int r=2;r<n;r++)
    {
       res+=x(r)*(  mem(r)/(double)(fact[n-r]) );
    }
    return memo[n]=(res+1.0)/(1.0-x(n));
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long f=1;
    for(int r=1;r<=1000;r++)
     {
       f*=(long long)r;
       f=min(f,(long long)((long long)1<<50));
       fact[r]=f;
     }
     int N;
   scanf("%d",&N);
   for(int _r=0;_r<N;_r++)
   {
      int n;
      double res=0;
      scanf("%d",&n);
      for(int r=0;r<=n;r++) memo[r]=-1.0,X[r]=-1.0;
      int cont=0;
      for(int r=0;r<n;r++)
      {
          scanf("%d",&a);
          if(a!=r+1) cont++;
      }
      printf("Case #%d: %lf\n",_r+1,mem(cont));
   }
}
