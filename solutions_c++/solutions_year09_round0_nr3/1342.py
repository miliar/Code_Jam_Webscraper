#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const string msg = "welcome to code jam";
const int MOD = 10000;
string str;
int C[520][50];

int dp(int p, int pm) {
  int &N = C[p][pm];
  if (N != -1)
    return N;

  if (pm == msg.size())
    return N = 1;
  if (p == str.size())
    return N = 0;

  N = dp(p+1, pm);
  if (str[p] == msg[pm])
    N = (N+dp(p+1, pm+1))%MOD;
  
  return N;
}

int main() {
  int n;
  cin >> n;
  cin.get();
  for (int CC = 1; CC <= n; ++CC) {
    getline(cin, str);
    memset(C, -1, sizeof C);
    printf("Case #%d: %04d\n", CC, dp(0, 0));
  }
}
