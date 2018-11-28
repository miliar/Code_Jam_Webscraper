#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>

#define F(i,a,b) for(int i=a;i<b;++i)
#define rep(i,b) F(i,0,b)

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  rep(t, T) {
    deque<int> oq;
    deque<int> bq;
    deque<pair<char, int> > all;
    int N;
    scanf("%d", &N);
    rep (n, N) {
      char c;
      int P;
      scanf(" %c %d", &c, &P);
      all.push_back(pair<char, int>(c, P));
      if (c == 'O') {
        oq.push_back(P);
      } else {
        bq.push_back(P);
      }
    }
    //
    int o = 1, b = 1;
    int s;
    for (s = 0; !all.empty(); ++s) {
      bool pop = false;
      if (!oq.empty()) {
        if (oq.front() != o) {
          if (oq.front() > o) ++o;
          else --o;
        } else if (oq.front() == o && all.front().first == 'O') {
          oq.pop_front();
          all.pop_front();
          pop = true;
        }
      }
      if (!bq.empty()) {
        if (bq.front() != b) {
          if (bq.front() > b) ++b;
          else --b;
        } else if (!pop && bq.front() == b && all.front().first == 'B') {
          bq.pop_front();
          all.pop_front();
        }
      }
    }
    printf("Case #%d: %d\n", t+1, s);
  }
}
