#include <iostream>
#include <vector>

using namespace std;

main () {
  int N;
  cin >> N;
  for (int n = 0; n < N; ++n) {
    int P, K, L;
    cin >> P >> K >> L;
    vector<int> LS(L);
    for (int l = 0; l < L; ++l) {
      cin >> LS[l];
    }
    if (P * K < L) {
      cout << "Impossible" << endl;
    } else {
      sort(LS.begin(), LS.end());
      reverse(LS.begin(), LS.end());
      long long sum = 0;
      for (int i = 0; i < LS.size(); ++i) {
        sum += LS[i] * ((i/ K) + 1);
      }
      printf("Case #%d: %lld\n", n + 1, sum);
    }
  }
}
