#include <iostream>
#include <cstdio>
#include <string>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")

using namespace std;

int main(){
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  string jam = "welcome to code jam";
  char str[100000];
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){ 
    gets(str);
    int dp[jam.sz];
    SET(dp, 0);
    FOR (i, strlen(str)){
      for (int j = jam.sz - 1; j > 0; j--)
        if (str[i] == jam[j])
          dp[j] = (dp[j] + dp[j - 1]) % 10000;
      if (str[i] == jam[0])
        dp[0] = (dp[0] + 1) % 10000;
    }
    cout << "Case #" << (test + 1) << ": ";
    int ret = dp[jam.sz - 1];
    if (ret < 10)
      cout << "000";
    else if (ret < 100)
      cout << "00";
    else if (ret < 1000)
      cout << "0";
    cout << ret << endl;
  }
  return 0;
}
