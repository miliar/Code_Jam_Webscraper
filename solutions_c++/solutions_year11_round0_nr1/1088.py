#include <iostream>
#include <queue>
#include <set>
#include <utility>
using namespace std;

typedef pair<int, pair<int, int> > St;
char R[200];
int B[200];

int main() {
  int T, C = 1, n;
  cin >> T;
  while (T-- && cin >> n) {
    for (int i = 0; i < n; ++i)
      cin >> R[i] >> B[i];
    
    int best;
    queue<pair<int, St> > Q;
    set<St> S;
    Q.push(make_pair(0, make_pair(0, make_pair(1, 1))));
    S.insert(make_pair(0, make_pair(1, 1)));
    while (!Q.empty()) {
      int d = Q.front().first;
      int i = Q.front().second.first;
      int r0 = Q.front().second.second.first;
      int r1 = Q.front().second.second.second;
      Q.pop();

      if (i == n) {
        best = d;
        break;
      }

      if (R[i] == 'O' && r0 == B[i])
        for (int k = -1; k <= 1; ++k) {
          if (r1+k < 1 || r1+k > 100)
            continue;
          St next = make_pair(i+1, make_pair(r0, r1+k));
          if (S.find(next) == S.end())
            Q.push(make_pair(d+1, next)), S.insert(next);
        }

      if (R[i] == 'B' && r1 == B[i])
        for (int k = -1; k <= 1; ++k) {
          if (r0+k < 1 || r0+k > 100)
            continue;
          St next = make_pair(i+1, make_pair(r0+k, r1));
          if (S.find(next) == S.end())
            Q.push(make_pair(d+1, next)), S.insert(next);
        }
      
      for (int j = -1; j <= 1; ++j)
        for (int k = -1; k <= 1; ++k) {
          if (r0+j < 1 || r0+j > 100 || r1+k < 1 || r1+k > 100)
            continue;
          St next = make_pair(i, make_pair(r0+j, r1+k));
          if (S.find(next) == S.end())
            Q.push(make_pair(d+1, next)), S.insert(next);
        }
    }
    cout << "Case #" << C++ << ": " << best << endl;
  }
}
