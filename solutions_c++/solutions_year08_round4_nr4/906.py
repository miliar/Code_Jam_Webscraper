#include <iostream>

using namespace std;

int order[16];

main () {
  int N;
  cin >> N;
  for (int n = 0; n < N; ++n) {
    int k;
    string S;
    cin >> k >> S;
    for (int i = 0; i < k; i++) {
      order[i] = i;
    }
    int MIN = INT_MAX;
    do {
      string s(S);
      for (int i = 0; i < s.size(); i += k) {
        string tmp = s.substr(i, k);
        for (int j = 0; j < k; j++) {
          s[i + j] = tmp[order[j]];
        }
      }
      int size = 0;
      char last = '.';
      for (int i = 0; i < s.size(); i++) {
        if (s[i] != last) {
          size++;
        }
        last = s[i];
      }
      //cout << s << endl;
      MIN = min(MIN, size);
    } while (next_permutation(order, order + k));
    printf("Case #%d: %d\n", n + 1, MIN);
  }
}
