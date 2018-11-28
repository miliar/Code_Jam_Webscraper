#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())


string S=".welcome to code jam";
int dp[1001][20];


int main()
{ 
  int i,j,k;
  char buf[10000];

  int N;
  scanf("%d\n",&N);
  for(k=1;k<=N;k++)
  {
    gets(buf);
    memset(dp,0,sizeof(dp));
    dp[0][0]=1;
    for(i=0;buf[i];i++)
    {
      for(j=0;j<=19;j++)
        dp[i+1][j]=dp[i][j];
      for(j=1;j<=19;j++)
        if(buf[i]==S[j])
          dp[i+1][j]=(dp[i][j-1]+dp[i+1][j])%10000;
    }
  
    printf("Case #%d: %04d\n",k,dp[i][19]);
  }


  return 0;
}
