#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int dp[501][20];

string base = "welcome to code jam";

int main(){
  int N;
  string str;
  scanf("%d",&N);
  getline(cin,str);
  for (int ii=0;ii<N;ii++){
    string str;
    memset(dp,0,sizeof(dp));
    getline(cin,str);
    for (int i=0;i<str.size();i++){
      for (int j=0;j<19;j++){
        if (i!=0) dp[i][j] = dp[i-1][j];
      }
      for (int j=18;j>=0;j--){
        if (str[i] == base[j]){
          if (j==0){
            dp[i][j] = (dp[i][j] + 1) % 1000;
          }else{
            dp[i][j] = (dp[i][j-1] + dp[i][j]) % 1000;
          }
        }
      }
    }
    printf("Case #%d: %04d\n",ii+1,dp[str.size()-1][18]);
  }
}
