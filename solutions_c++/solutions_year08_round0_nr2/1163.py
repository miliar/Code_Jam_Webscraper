#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct S {
  bool ab;
  string d;
  bool operator < (const S &t) const {
    return d > t.d;
  }
};

string add(int T, string s) {
  int h, m;
  sscanf(s.c_str(), "%02d:%02d", &h, &m);
  h += (m + T) / 60;
  m = (m + T) % 60;
  char buf[6];
  sprintf(buf, "%02d:%02d", h, m);
  return string(buf);
}

main () {
  int N;
  cin >> N;
  for (int n = 0; n < N; ++n) {
    int T, NAB[2];
    cin >> T >> NAB[0] >> NAB[1];
    vector<vector<pair<string, string> > > train(2);
    for (int ab = 0; ab < 2; ++ab) {
      for (int i = 0; i < NAB[ab]; ++i) {
        string s, e;
        cin >> s >> e;
        train[ab].push_back(make_pair(s, e));
      }
    }
    int added[2] = {0}, available[2] = {0};
    priority_queue<S> que;
    for (int h = 0; h <= 23; ++h) {
      for (int m = 0; m <= 59; ++m) {
        char buf[6];
        sprintf(buf, "%02d:%02d", h, m);
        string now(buf);
        while (!que.empty() && que.top().d == now) {
          available[que.top().ab]++;
          que.pop();
        }
        for (int ab = 0; ab < 2; ++ab) {
          for (int i = 0; i < NAB[ab]; ++i) {
            if (train[ab][i].first == now) {
              if (available[ab]) {
                --available[ab];
              } else {
                ++added[ab];
              }
              S t;
              t.ab = ab ^ 1;
              t.d = add(T, train[ab][i].second);
              que.push(t);
            }
          }
        }
      }
    }
    printf("Case #%d: %d %d\n", n + 1, added[0], added[1]);
  }
}
