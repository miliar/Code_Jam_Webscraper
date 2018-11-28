#include <iostream>
#include <vector>

using namespace std;

int dp[100][1000];

main () {
  string dummy;

  int N;
  cin >> N; getline(cin, dummy);
  for (int n = 0; n < N; ++n) {
    int S;
    cin >> S; getline(cin, dummy);
    vector<string> engine(S);
    for (int i = 0; i < S; i++) {
      getline(cin, engine[i]);
      //cout << engine[i] << endl;
    }

    int Q;
    cin >> Q; getline(cin, dummy);
    vector<string> query(Q);
    for (int i = 0; i < Q; i++) {
      getline(cin, query[i]);
      //cout << query[i] << endl;
    }

    for (int i = Q - 1; i >= 0; --i) {
      for (int j = 0; j < S; ++j) {
        if (i == Q - 1) {
          if (engine[j] == query[i]) {
            dp[j][i] = 1;
          } else {
            dp[j][i] = 0;
          }
        } else {
          if (engine[j] == query[i]) {
            int MIN = INT_MAX;
            for (int k = 0; k < S; ++k) {
              if (k != j) {
                MIN <?= dp[k][i + 1];
              }
            }
            dp[j][i] = MIN + 1;
          } else {
            dp[j][i] = dp[j][i + 1];
          }
        }
      }
    }
    int answer = INT_MAX;
    for (int i = 0; i < S; ++i) {
      answer <?= dp[i][0];
    }
    printf("Case #%d: %d\n", n + 1, answer);
  }
}
