#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

void solve() {
  vector<pair<char, char> > combine;
  vector<char> result;
  vector<pair<char, char> > opposed;
  int comb;
  scanf("%d", &comb);
  FOR(q, comb) {
    char tmp[10];
    scanf("%s", tmp);
    combine.push_back(make_pair(tmp[0], tmp[1]));
    combine.push_back(make_pair(tmp[1], tmp[0]));
    result.push_back(tmp[2]);
    result.push_back(tmp[2]);
  }

  int opp;
  scanf("%d", &opp);
  FOR(q, opp) {
    char tmp[10];
      scanf("%s", tmp);
    opposed.push_back(make_pair(tmp[0], tmp[1]));
    opposed.push_back(make_pair(tmp[1], tmp[0]));
  }

  int len;
  char tmp[200];
  scanf("%d", &len);
  scanf("%s", tmp);
  vector<char> list;
 // printf("seq %s %d\n", tmp, len);
  FOR(q, len) {
    if (list.size() == 0) {
      list.push_back(tmp[q]);
      continue;
    }
    bool ok = false;
    FOR(i, combine.size()) {
      if (!ok &&
          combine[i].first == tmp[q] &&
          combine[i].second == list[list.size() - 1]) {
        list.pop_back();
        list.push_back(result[i]);
        ok = true;
      }
    }

    FOR(i, opposed.size()) {
      if (!ok && opposed[i].first == tmp[q]) {
        FOR(j, list.size()) {
     //     printf("(%c)", list[j]);
          if (!ok && list[j] == opposed[i].second) {
       //     printf("clear");
            ok = true;
            list.clear();
          }
        }
      }
    }
    if (!ok) {
      list.push_back(tmp[q]);
    }

  }
  printf("[");
  FOR(q, list.size()) {
    if (q != 0) printf(", ");
    printf("%c", list[q]);
  }
  printf("]\n");

}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
  }

}
