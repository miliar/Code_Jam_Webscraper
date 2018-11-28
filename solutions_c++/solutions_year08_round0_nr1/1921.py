#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

const int INF=1<<29;

int n,m, dp[1005][105];
vector<string> names;

int main()
{
  int tt;
  scanf("%d",&tt);
  for(int t=1;t<=tt;t++) {
    names.clear();
    scanf("%d\n",&n);
   
    for(int i=0;i<n;i++) {
      string tmp;
      getline(cin,tmp);
      names.push_back(tmp);
    }

    scanf("%d\n",&m);

    for(int i=0;i<=m;i++)
      for(int j=0;j<=n;j++)
	dp[i][j]=INF;
    for(int i=0;i<=n;i++)
      dp[0][i]=0;

    string str;
    for(int i=1;i<=m;i++) {
      getline(cin,str);

      for(int j=0;j<n;j++)
	dp[i][j]=dp[i-1][j];
      
      int p=0;
      for(int j=1;j<n;j++)
	if(dp[i-1][j] < dp[i-1][p])
	  p=j;

      for(int j=0;j<n;j++)
	dp[i][j] = min(dp[i][j], dp[i-1][p]+1);

      p=0;
      while(names[p]!=str)p++; 
      dp[i][p]=INF;

    }

    int res=INF;
    for(int i=0;i<n;i++)
      res=min(res,dp[m][i]);
    printf("Case #%d: %d\n",t,res);
  }

  return 0;
}
