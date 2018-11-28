#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
typedef unsigned long long ull; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

int dp[1001][100];



int main()
{
  int i,j,k,m,n,s,q; 
  int N,S,Q;
  char buf[10000]; 

  scanf("%d\n",&N);
  for(n=1;n<=N;n++)
  {
    scanf("%d\n",&S); vs engines;
    for(s=0;s<S;s++)
    {
      gets(buf);
      engines.pb(buf);
    }
    vi queries(1,0); string temp;
    scanf("%d\n",&Q);
    for(q=0;q<Q;q++)
    {
      gets(buf);
      temp=buf;
      int waar=find(engines.begin(),engines.end(),temp)-engines.begin();
      queries.pb(waar);
    }

    memset(dp,0,sizeof(dp));
    for(q=1;q<=Q;q++)
      for(s=0;s<S;s++)
      {
        dp[q][s]=1000000; //it's difficult

        for(j=0;j<S;j++)
          if(j!=queries[q])
          {
            if(j==s) dp[q][s]=min(dp[q][s],dp[q-1][s]);
            else dp[q][s]=min(dp[q][s],dp[q-1][j]+1);
          }
      }
    int beste=(Q==0)?0:1000000;
    for(j=0;j<S;j++)
      beste=min(beste,dp[Q][j]);
    printf("Case #%d: %d\n",n,beste);

  }
  return 0;
}
