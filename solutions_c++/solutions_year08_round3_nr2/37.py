#include <iostream>
#include <vector>
#include <sstream>

using namespace std;
unsigned long long dp[41][210][41];
string s;
int len;
long long get_number(int a, int b){
  int cur = 0;
  for(int i=a;i<=b;i++){
    cur *= 10;
    cur += s[i]-'0';
    cur %= 210;
  }
  return cur;
}
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  getline(cin,s);
  while(cases--){
    cout << "Case #" << ++temp << ": ";    
    getline(cin,s);
    len = s.size();
    for(int i=0;i<=len;i++){
      for(int j=0;j<210;j++){
	for(int k=0;k<=len;k++){
	  dp[i][j][k] = 0;
	}
      }
    }
    dp[0][0][0] = 1;
    for(int i=0;i<len;i++){
      for(int j=0;j<210;j++){
	for(int k=0;k<=i;k++){
	  unsigned long long cur = dp[i][j][k];
	  long long num = get_number(k,i);
	  if(k!=0){
	    long long next1 = ((j-num)%210+210)%210;
	    dp[i+1][next1][i+1] += cur;
	  }
	  long long next2 = ((j+num)%210+210)%210;
	  dp[i+1][next2][i+1] += cur;
	  dp[i+1][j][k] += cur;
	}
      }
    }
    unsigned long long ret = 0;
    for(int i=0;i<210;i++){
      if(i%2==0||i%3==0||i%5==0||i%7==0){
	ret += dp[len][i][len];
      }
    }
    cout << ret << endl;
  }
  return 0;
}
