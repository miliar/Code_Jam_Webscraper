#include <cstdio>
#include <iostream>
#include <string>

using namespace std;
int test = 0;
string B = "welcome to code jam";

int DP[555][20];

void go() {
  char text[555];
  cin.getline(text, 555);
  string A = text;
  int   n = A.size();
  int   m = B.size();

  memset(DP, 0, sizeof(DP));
  int j;
  for (int i = 1; i <= n; ++i)
    for (j = 1, DP[i-1][0] = 1; j <= m; ++j) { 
      
      DP[i][j] = DP[i-1][j] +  DP[i-1][j-1] * (A[i-1] == B[j-1]);
      DP[i][j] %= 10000;
    }
  printf("Case #%d: %04d\n", ++test, DP[n][m]);
}
int main() {
  freopen("exampleL.in", "r", stdin);
  freopen("exampleL.out", "w", stdout);
  int t;
  scanf("%d\n", &t);
  while (t--) {
    go();
  }
}
