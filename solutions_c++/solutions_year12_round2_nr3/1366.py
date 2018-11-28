#include<iostream>
#include<vector>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<map>
#include<set>
#include<cstdio>
#include<algorithm>
using namespace std;
#define FOR(i,k,l) for(i=k;i<l;i++)
#define REP(i,k) for(i=0;i<k;i++)  
#define LL long long
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define MOD 10000007
int main()
{
  int kase=GI;
  int i;
  REP(i,kase)
    {
      int n=GI,j;
      int a[n+2];
      REP(j,n) a[j]=GI;
      map<int,int> m;
      int s[1<<n];
      int k;
      int sum=0;int pos=0;
      REP(j,1<<n)
	{
	  sum=0;
	  REP(k,n) if(j&(1<<k)) sum+=a[k];
	  if(sum!=0){
	  if(!(m[sum]))  m[sum]=j;
	  else if(!(m[sum]&j)) {pos=j;break;} 
	  }}

      cout<<"Case #"<<i+1<<":"<<endl;
      REP(j,n) if((1<<j)&(pos)) cout<<a[j]<<" ";
      cout<<endl;
	    REP(j,n) if((1<<j)&m[sum]) cout<<a[j]<<" ";
      cout<<endl;

    }
}
