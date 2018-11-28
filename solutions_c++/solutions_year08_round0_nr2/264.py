#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cmath>
#include <cctype>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define FOR(i, begin, end) for(int i = (begin); i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

int main() {
  int cases;
  scanf("%d", &cases);
  for (int cs = 1; cs <= cases; cs++) {
    int turn;
    int n[2];
    scanf("%d %d %d ", &turn, &n[0], &n[1]);

    vector<pair<int, int> > train[2];
    int r[2]; CLEAR(r);

    FOR(i, 0, n[0]) {
      int h1, m1, h2, m2;
      scanf("%d:%d %d:%d ", &h1, &m1, &h2, &m2);
      train[0].push_back(make_pair(60*h1+m1, 60*h2+m2));
    }
    FOR(i, 0, n[1]) {
      int h1, m1, h2, m2;
      scanf("%d:%d %d:%d ", &h1, &m1, &h2, &m2);
      train[1].push_back(make_pair(60*h1+m1, 60*h2+m2));
    }
    sort(ALL(train[0]));
    sort(ALL(train[1]));
    train[0].push_back(make_pair(9999,9999));
    train[1].push_back(make_pair(9999,9999));

    while (n[0] || n[1]) {
      int k;
      if (train[0][0].first < train[1][0].first) 
        k = 0;
      else 
        k = 1;
      r[k]++;
      int i = 0;
      int t;
      while (true) {
        t = train[k][i].second+turn;
        train[k].erase(train[k].begin()+i);
        n[k]--;
        k = 1-k;
        i = 0;
        while (i < n[k] && train[k][i].first < t)
          i++;
        if (i == n[k])
          break;
      }
    }
    cout << "Case #" << cs << ": " << r[0] << " " << r[1] << endl;
  }
}
