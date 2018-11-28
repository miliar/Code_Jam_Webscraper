#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <climits>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <stack>

using namespace std;

int main(int argc, char *argv[]) {
  int T; // num test cases
  int S; // size of case problem
  int C = 0; // current case number
  string line; // one input line
  stringstream in; // streamstring of input
  cin >> T;
  cin.ignore();
  while (getline(cin, line)) {
    C++;
    in.clear();
    in.str("");
    in << line;

    in >> S;

    queue<int> Loc[2]; // Orange, Blue
    //bool *isBlue = new bool[S + 1]; // isBlueButton[0] meaningless
    bool isBlue[1000];
    string s;
    int d;
    int i = 0;
    while (in >> s) { // an O or B
      i += 1;
      in >> d;
      if (!s.compare("O")) {
        Loc[0].push(d);
        isBlue[i] = 0;
      }
      else {
        Loc[1].push(d);
        isBlue[i] = 1;
      }
      isBlue;
    }

    long time = 0;
    long button = 1;
    int location[2] = {1, 1};
    int freeDistance = 0;
    bool sameRoom = false; // same room as previously? Then no free distance.
    while (!Loc[0].empty() || !Loc[1].empty()) {
      int current = isBlue[button] ? 1 : 0;
      if (button == 1)
        sameRoom = false;
      else
        sameRoom = (current == isBlue[button - 1]);

      int dest = Loc[current].front();
      int d = abs(dest - location[current]);
      location[current] = dest;
      Loc[current].pop();
      if (!sameRoom) {
        d = max(0, d - freeDistance);
        freeDistance = 0;
      }
      time += d + 1;
      freeDistance += d + 1;
      button++;
    }
    printf("Case #%d: %li\n", C, time);
  }
}