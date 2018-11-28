#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// int cs[2097152][3];
// int numbers[1010];
void solve() {
  int N, x = 0, t, m = 1000000000, sum = 0;
  cin >> N;
  while (N--) {
    cin >> t;
    x ^= t;
    sum += t;
    m = min(m, t);
  }
  if (x) {
    cout << "NO";
  } else {
    cout << sum - m;
  }
  /*for (int x = 0; x < (1<<21); x++) {
    cs[x][0] = cs[x][1] = cs[x][2] = 0;
  }
  cs[0][2] = 1;

  int N, x = 0, realsum = 0;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> numbers[i];
    x ^= numbers[i];
    realsum += numbers[i];
  }
  if (x) {
    cout << "NO";
    return;
  }*/
  /*for (int y = 0; y < N; y++) {
    for (int x = 0; x < (1<<21); x++) {
      if (cs[x][2]) {
        cs[x ^ numbers[y]][1] = cs[x][0] + numbers[y];
        cout << (x ^ numbers[y]) << ": " << cs[x][0] + numbers[y] << endl;
      }
    }
    for (int x = 0; x < (1<<21); x++) {
      if (cs[x][0] != cs[x][1] && (cs[x][2] == 0 || cs[x][1] < cs[x][0])) {
        cs[x][0] = cs[x][1];
        cs[x][2] = 1;
      }
    }
  }
  for (int x = 0; x < (1<<21); x++) {
    if (cs[x][2]) {
      cout << x << " " << cs[x][0] << endl;
    }
  }
  cout << "NO";*/
  return;
}
int main() {
  int T, i = 0;
  cin >> T;
  while (i++ < T) {
    cout << "Case #" << i << ": "; solve(); cout << endl;
  }
  return 0;
}

