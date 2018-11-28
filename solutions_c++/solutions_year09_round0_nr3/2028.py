#include <string>
#include <sstream>
#define MOD 10000
#include <iostream>
using namespace std;
int dp[501][20];
string wel, m;
int rec(int i, int j)
{
  if( j == wel.length())return 1;
  if( i>= m.length())return 0;
   if(dp[i][j] != 0)return dp[i][j];
  if(m[i] == wel[j]){
     return dp[i][j] = (rec(i+1, j+1) +rec(i+1, j))%MOD;
}
   return dp[i][j] = (rec(i+1, j))%MOD;
}
int main()
{
wel = "welcome to code jam";
  char in[512];
  int N;
  scanf("%d", &N);
     cin.ignore();
  for(int c = 1;c<=N;c++)
  {
    getline(cin, m);
    for(int i=0;i<20;i++)
      for(int j=0;j<=m.length();j++)
          dp[j][i] =0;
      int t = rec(0, 0);
      stringstream ss;
      ss<<t;
      string ans;
      ss>>ans;
      while (ans.size()<4)ans='0'+ans;
    printf("Case #%d: %s\n", c, ans.c_str());
  }
  
} 
