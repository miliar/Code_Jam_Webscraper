#include <iostream>
#include <sstream>
#include <string>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; i++)
#define REP(i, n) FOR(i, 0, (n))

string line, greeting = "welcome to code jam";
int cache[1000][30];

string i2s(int n) {
  stringstream ss; ss << n; return ss.str();
}

int cal(int i, int j) {
  if (j == greeting.size()) return 1;
  if (i == line.size()) return 0;

  int & ret = cache[i][j];
  if (ret != -1) return ret;

  ret = cal(i+1, j);
  if (line[i] == greeting[j]) ret += cal(i+1, j+1);
  ret %= 10000;
  return ret;
}

int main() {
  int N;
  cin >> N; getline(cin, line);

  FOR(C, 1, N+1) {
    getline(cin, line);
    memset(cache, -1, sizeof cache);
    int tmp = cal(0, 0);
    string ans = i2s(tmp);
    while (ans.size() < 4) ans = '0' + ans;
    cout << "Case #" << C << ": " << ans << endl;
  }
}
