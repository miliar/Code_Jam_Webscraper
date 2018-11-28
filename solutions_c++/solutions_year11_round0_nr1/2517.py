#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

struct Button {
  int R;
  int P;
};

int N;

int getNext(int current, int R, int i, vector<Button> &turns)
{
  int result = current;
  while (i < N) {
    if (turns[i].R == R) {
      result = turns[i].P;
      break;
    }
    ++i;
  }
  return result;
}

void MakeTurn(int &p, int &next) {
  if (p < next) {
    p++;
  } else if (p > next) {
    --p;
  }
}

void Solve() {
  cin >> N;
  vector<Button> turns;
  for(int i = 0; i < N; ++i) {
    string s;
    int p;
    cin >> s >> p;
    Button turn;
    turn.P = p;
    if (s == "O") {
      turn.R = 0;
    } else {
      turn.R = 1;
    }
    turns.push_back(turn);
  }
  int answer = 0;
  int p[2] = {1, 1};
  int i = 0;
  int next[2];
  next[0] = getNext(p[0], 0, i, turns);
  next[1] = getNext(p[1], 1, i, turns);
  while (i < N) {
    int turn = turns[i].R;
    if (next[turn] == p[turn]) {
      ++i;
      next[turn] = getNext(p[turn], turn, i, turns);
    } else {
      MakeTurn(p[turn], next[turn]);
    }
    MakeTurn(p[1 - turn], next[1 - turn]);
    ++answer;
  }
  cout << answer << endl; 
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    cout << "Case #" << i + 1 << ": ";
    Solve();
  }
  return 0;
}
