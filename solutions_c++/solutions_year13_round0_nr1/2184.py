#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct Line {
  int X, O, T;

  Line(void) {
    X = O = T = 0;
  }

  void put(char c) {
    if (c == 'X')
      ++X;
    else if (c == 'O')
      ++O;
    else if (c == 'T')
      ++T;
  }

  char win(void) {
    return (((X + T) == 4) ? ('X') : (((O + T) == 4) ? ('O') : ('.')));
  }

  bool full(void) {
    return ((X + O + T) == 4);
  }
};

int main(int argc, char** argv) {

  ifstream I((argc == 1) ? ("sample_input.txt") : (argv[1]));
  ofstream O("output.txt");
  string line;

  int T; I >> T;

  for (int t = 0; t < T; ++t) {

    vector<Line> lines(10);

    I >> line;
    lines[0].put(line[0]); lines[4].put(line[0]); lines[8].put(line[0]);
    lines[1].put(line[1]); lines[4].put(line[1]);
    lines[2].put(line[2]); lines[4].put(line[2]);
    lines[3].put(line[3]); lines[4].put(line[3]); lines[9].put(line[3]);

    I >> line;
    lines[0].put(line[0]); lines[5].put(line[0]);
    lines[1].put(line[1]); lines[5].put(line[1]); lines[8].put(line[1]);
    lines[2].put(line[2]); lines[5].put(line[2]); lines[9].put(line[2]);
    lines[3].put(line[3]); lines[5].put(line[3]);

    I >> line;
    lines[0].put(line[0]); lines[6].put(line[0]);
    lines[1].put(line[1]); lines[6].put(line[1]); lines[9].put(line[1]);
    lines[2].put(line[2]); lines[6].put(line[2]); lines[8].put(line[2]);
    lines[3].put(line[3]); lines[6].put(line[3]);

    I >> line;
    lines[0].put(line[0]); lines[7].put(line[0]); lines[9].put(line[0]);
    lines[1].put(line[1]); lines[7].put(line[1]);
    lines[2].put(line[2]); lines[7].put(line[2]);
    lines[3].put(line[3]); lines[7].put(line[3]); lines[8].put(line[3]);


    int i;
    bool full = true;
    O << "Case #" << (t + 1) << ": ";
    for (i = 0; i < 10; ++i) {
      char w = lines[i].win();
      if (w != '.') {
        O << w << " won" << endl;
        break;
      }
      else if (full)
        full = lines[i].full();
    }

    if (i == 10) {
      O << ((full) ? ("Draw") : ("Game has not completed")) << endl;
    }
  }

  I.close();
  O.close();

  return 0;
}
