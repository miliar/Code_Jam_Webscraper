#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf
int dp[105][105];
vector<int> ord;
int call(int lo, int hi )
{
 if ( hi-lo<=1) re 0;
 if ( dp[lo][hi] != -1 ) re dp[lo][hi];
 int minval= 1000000000;
 int i;
 for(i=lo+1;i<=hi-1;i++)
 {
  int val;
  val = ord[i] - ord[lo] - 1 + (ord[hi] - ord[i] -1 );
  val = val + call(lo,i) + call(i,hi);
  if ( val < minval ) minval = val;
 }
 dp[lo][hi]=minval;
 re minval;
}
int main() {
    
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    int t;
    sf("%d",&t);
    int kase=1;
    while ( t--)
    {
     int n;
     int q;
     sf("%d %d",&n,&q);
     ord.clear();
     
     int num;
     while ( q--)
           sf("%d",&num), ord.pb(num);
     ord.pb(0);
     ord.pb(n+1);
     sort(ord.begin(),ord.end() );
     int i,j;
     for(i=0;i<103;i++)
      for(j=0;j<103;j++)
       dp[i][j] = -1;
     pf("Case #%d: %d\n",kase++,call(0,ord.size()-1) );
    }
	return 0;
}
