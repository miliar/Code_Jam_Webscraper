#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>
#include <algorithm>

int T;
int N;

using namespace std;

int main (int argc, char **argv) {
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    queue<int> o,b;
    queue<char> q;

    // Read input
    for (int j = 0; j < N; ++j) {
      char c; int d;
      cin >> c >> d;
      q.push(c);
      if (c == 'O') {
        o.push(d);
      } else {
        b.push(d);
      }
    }
    
    int time = 0;
    char cur;
    int oPos = 1, bPos = 1;
    
    // run through examples
    for (int j = 0; j < N; ++j) {
      cur = q.front(); q.pop();
      int toMove;

      if (cur == 'O') {
        toMove = abs(oPos - o.front()) + 1;
        oPos = o.front();
        o.pop();
        if (bPos > b.front()) {
          bPos = max(b.front(), bPos - toMove);
        } else if (bPos < b.front()) {
          bPos = min(b.front(), bPos + toMove);
        }
        time += toMove;
      } else {
        toMove = abs(bPos - b.front()) + 1;
        bPos = b.front();
        b.pop();
        if (oPos > o.front()) {
          oPos = max(o.front(), oPos - toMove);
        } else if (oPos < o.front()) {
          oPos = min(o.front(), oPos + toMove);
        }
        time += toMove;
      }
    }
    cout << "Case #" << (i+1) << ": " << time << endl;
  }

  return 0;
}
