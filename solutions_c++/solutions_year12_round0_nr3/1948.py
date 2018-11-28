#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
  int N;
  cin >> N;
  for (int n=1; n<=N; ++n) {
    int A, B;
    cin >> A >> B;
    int C = A, nD = 1, count = 0;
    while (C /= 10) { nD++; }
    int nDi = 1;
    for (int i = 1; i < nD; ++i, nDi *= 10) {}
    for (int i = A; i <= B; ++i) {
      string d;
      for (int j = nDi; j; j /= 10) {
        int k = i / j % 10;
        d.push_back((char )k);
      }
      d += d;

      set<int> s;
      for (int j = 1; j < nD; ++j) {
        int r=0;
        for (int k = j, kk = j + nD; k < kk; ++k) {
          r *= 10;
          r += (int)d[k];
        }
        if (r > i && r <= B) { s.insert(r); }
      }
      count += (int)s.size();
    }
    cout << "Case #" << n << ": " << count << endl;
  }
  return 0;
}
