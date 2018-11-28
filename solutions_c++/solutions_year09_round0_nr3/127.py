#include<iostream>
#include<string>
#include<vector>

using namespace std;

string s = "welcome to code jam";
string p = "";

long long D[25][513];
long long smurf(int a, int b) {
  if (D[a][b] != -1) return D[a][b];
  if (a == s.size()) return D[a][b] = 1LL;
  if (b == p.size()) return D[a][b] = 0LL;
  long long ret = 0LL;

  for (int tb = b; tb < p.size(); ++tb) {
    if (s[a] == p[tb]) ret = (ret + smurf(a+1,tb+1)) % 10000LL;
  }

  return D[a][b] = ret;
}


int main() {
  int T;
  scanf("%d\n", &T);
  for (int i = 0; i < T; ++i) {
    memset(D, -1, sizeof(D));
    getline(cin, p);
    long long ret = smurf(0,0);
    printf("Case #%d: %04d\n", i+1, (int)ret);
  }

  return 0;
}
