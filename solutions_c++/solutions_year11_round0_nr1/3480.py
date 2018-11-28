#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int eval_steps(istream &in) {
  vector< vector<int> > commands(2);
  vector<int> color;
  int n, m, time;
  char c;
  in >> n;
  for(; n > 0; n--) {
    in >> c >> m;
    switch(c) {
      case 'O':
        commands[0].push_back(m);
        color.push_back(0);
        break;
      case 'B':
        commands[1].push_back(m);
        color.push_back(1);
        break;
    }
  }
  int pos[2] = {1, 1}, pointer[2] = {0, 0}, color_pointer = 0;
  bool sw;
  for(time = 0; pointer[0] < commands[0].size() || pointer[1] < commands[1].size(); time++) {
    if (sw) {
      color_pointer++;
      sw = false;
    }
    for(int i = 0; i < 2; i++) {
      if (pointer[i] == commands[i].size())
        continue;
      if (pos[i] == commands[i][pointer[i]]) {
        if (color[color_pointer] == i) {
          pointer[i]++;
          sw = true;
        }
      } else if (pos[i] > commands[i][pointer[i]]) {
        pos[i]--;
      } else {
        pos[i]++;
      }
    }
  }
  return time;
}

int main() {
  ifstream in("A-small.in");
  ofstream out("A-small.out");
  int t;
  in >> t;
  for (int i = 1; i <= t; i++) {
    out << "Case #" << i << ": " << eval_steps(in) << endl;
  }
  in.close();
  out.close();
  return 0;
}
