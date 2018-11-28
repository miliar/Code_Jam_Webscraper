#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

int solve(queue< pair<char, int> > &sequence, queue<int> &B, queue<int> &O)
{
  int seconds = 0,
      posO = 1,
      posB = 1;

  while (!sequence.empty()) {
    pair<char, int> step = sequence.front();
    sequence.pop();

    for (;; ++seconds) {

      bool found = false;

      if (posB == step.second && step.first == 'B') {
        B.pop();
        found = true;
      } else {
        if (!B.empty()) {
          if (posB < B.front()) {
            posB++;
          } else if (posB > B.front()) {
            posB--;
          }
        }
      }

      if (posO == step.second && step.first == 'O') {
        O.pop();
        found = true;
      } else {
        if (!O.empty()){
          if (posO < O.front()) {
            posO++;
          } else if (posO > O.front()) {
            posO--;
          }
        }
      }

      if (found) {
        seconds++;
        break;
      }
    }
  }

  return seconds;
}

int main(int argc, char **argv)
{
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    int N; // buttons to press
    cin >> N;

    queue< pair<char, int> > sequence;
    queue<int> B;
    queue<int> O;

    for (int n = 0; n < N; ++n) {
      char R;
      int P;
      cin >> R >> P;

      if (R == 'B') {
        B.push(P);
      } else {
        O.push(P);
      }

      sequence.push(make_pair(R, P));
    }

    cout << "Case #" << i << ": " << solve(sequence, B, O) << '\n';
  }

  return 0;
}
