#include <iostream>
#include <string>
using namespace std;

int common_str(string& str){
  string C="welcome to code jam";
  int size=C.size();
  int dp[2][str.size()];
  memset(dp,0,sizeof(dp));
  
  for(int i=0;i<size;i++){
    int sum=0;
    for(int j=0;j<str.size();j++){
      if(i && C[i-1]==str[j] && dp[1][j]==i){
        sum+=dp[0][j];
      }
      sum%=10000;
      if(C[i]==str[j]){
        dp[0][j]=i?sum:1; dp[1][j]=i+1;
      }
    }
  }
  int ans=0;
  for(int i=0;i<str.size();i++){
    if(dp[1][i]==size && C[size-1]==str[i])ans+=dp[0][i];
    ans%=10000;
  }
  return ans;
}

int main(void){
  for(int N;cin>>N;){
    cin.ignore();
    for(int X=1;X<=N;X++){
      string s;
      getline(cin,s);
      printf("Case #%d: ",X);
      int ans=common_str(s);
      if(ans>=1000)printf("%d\n",ans);
      else printf("%s%d\n",ans>=100?"0":ans>=10?"00":"000",ans);
    }
  }
  return 0;
}