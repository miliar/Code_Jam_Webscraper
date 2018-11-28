#include <iostream>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string N; cin >> N;
    int ct[10]; memset(ct, 0, sizeof(ct));
    for (int i = 0; i < N.size(); i++)
      ct[N[i]-'0']++;
    bool found = false;
    for (int i = N.size() - 1; i >= 0; i--) {
      int min = 1000, minp = -1;
      for (int j = i+1; j < N.size(); j++)
        if (N[j] > N[i] && N[j] < min) {
          min = N[j];
          minp = j;
        }
      if (minp != -1) {
        char temp = N[i];
        N[i] = N[minp];
        N[minp] = temp;
        sort(N.begin() + i + 1, N.end());
        found = true;
        break;
      }
    }
    if (!found) {
      N += "0";
      sort(N.begin(), N.end());
      for (int i = 0; i < N.size(); i++)
        if (N[i] != '0') {
          char temp = N[i];
          N[i] = N[0];
          N[0] = temp;
          break;
        }
    }
    cout << "Case #" << c << ": " << N << endl;
  }
  return 0;
}
