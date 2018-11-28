#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define ll long long
#define oo 1<<30
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define N 1000001

using namespace std;

int T,a1,a2,b1,b2;
int I[N];
int lim[N];
int *cota;
int howmany(int a){
   int l=I[a],r=l+a-1;
   if(r<b1)return b2-b1+1;
   if(l>b2)return b2-b1+1;
   return b2-b1-(min(r,b2)-max(l,b1));
}

int main()
{
   I[1]=1; lim[1]=1;lim[2]=3; cota=lim+1;
   f(x,2,N){
      if(x>*cota) I[x]=I[x-1]+1, cota++;
      else I[x]=I[x-1];
      lim[x]=I[x]+x-1;
      //if(x<100)cout<<I[x]<<" "<<lim[x]<<endl;
   }
   cin>>T;
   f(t,0,T){
      cin>>a1>>a2>>b1>>b2;
      ll res=0;
      f(i,a1,a2+1){
         res+=howmany(i);
      }
      cout<<"Case #"<<t+1<<": "<<res<<endl;
   }
}
