#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
  ifstream fin ("A.in");
  ofstream fout ("A.out");
  int possible = 0;
  int numTimes;
  fin >> numTimes;
  for (int turn = 0; turn < numTimes; turn++) {
    int N, D;
    int P_d, P_g;
    fin >> N >> P_d >> P_g;
    bool poss = false;

    for (int D = 1; D <= N; D++) {
      int youWon = P_d * D;
      if ((youWon < (N * 100)) && (fmod((double)youWon/100.0, 1.0) == 0.0)) {
        if ((P_g == 100) && (P_d != 100)) continue;
        else if ((P_g == 0) && (P_d != 0)) continue;
        else {
          poss = true;
          break;
        }
      }
    }
    if (poss) {
      fout << "Case #" << (turn + 1) << ": Possible" << endl;
      possible++;
    }
    else {
      fout << "Case #" << (turn + 1) << ": Broken" << endl;
    }
  }
  cout << possible << endl;
}
