#include <iostream>
#include <cstring>

using namespace std;

int main() {
  int T;
  cin >> T;
  bool check[2000001];
  for (int t = 0; t < T; ++t) {
    int A, B;
    cin >> A >> B;
    memset(check, 0, sizeof(check));
    int temp = A;
    int size = 0;
    int tens = 1;
    while ( temp > 0) {
      temp = temp / 10;
      size++;
      tens = tens * 10;
    }
    int res = 0;
    for (int i = A; i <= B; ++i) {
      if (check[i]) continue;
      if ( i % tens == 0) {
        size++; 
        tens *= 10;
      }
      int count = 0;
      int p = i;
      check[i] = true;
      for (int j = 1; j < size; ++j) {
        p = (p % (tens / 10)) * 10 + p / (tens / 10);
//        cout << p << endl;
        if ( p < tens / 10) continue;
        if (p > 2000000) continue;
        if (check[p]) break;
        if (p >= A && p <= B) {
          check[p] = true;
          count++;
        }
      }
      res += (count + 1) * (count) / 2;
    }
    cout << "Case #" << t + 1 << ": " << res << endl;
  }
}
