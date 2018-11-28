// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int main(int argc, const char *argv[])
try {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " fielname" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }
  int T = 0;
  input >> T;
  for(int t = 1; t <= T; ++t) {
    int N = 0;
    input >> N;
    int b[2][101];
    for (int i = 0; i < 101; ++i) {
      b[0][i] = -1;
      b[1][i] = -1;
    }
    char bot[100];
    int btn[100];
    int roc = 0;
    int rbc = 0;
    int seconds = 0;
    for (int n = 0; n < N; ++n) {
      char r;
      int bc;
      input >> r;
      input >> bc;
      bot[n] = r;
      btn[n] = bc;
      if (r == 'O')
        b[0][roc++] = bc;
      else
        b[1][rbc++] = bc;
    }

    int Bi = 0;
    int Oi = 0;
    int pB = 1;
    int pO = 1;
    int dB = 0;
    int dO = 0;

    for (int i = 0; i < N; ++i) {
      char currBot = bot[i];
      int  currBtn = btn[i];

      while(1) {
        ++seconds;
        if (currBot == 'O') {
          if (b[1][Bi] != pB) {
            if (pB > b[1][Bi])
              --pB;
            else if (pB < b[1][Bi])
              ++pB;
          }

          if (currBtn != pO) {
            if (pO > b[0][Oi])
              --pO;
            else if (pO < b[0][Oi])
              ++pO;
          }
          else {
            ++Oi;
            break;
          }
        } else {
          if (b[0][Oi] != pO) {
            if (pO > b[0][Oi])
              --pO;
            else if (pO < b[0][Oi])
              ++pO;
          }

          if (currBtn != pB) {
            if (pB > b[1][Bi])
              --pB;
            else if (pB < b[1][Bi])
              ++pB;
          }
          else {
            ++Bi;
            break;
          }
        }
      }
      if (Oi == roc && Bi == rbc)
        break;
    }
    cout << "Case #" << t << ": " << seconds << endl;
  }

  return 0;
}
catch (exception & e) {
  cerr << "Error: " << e.what() << endl;
  return -2;
}
catch(...) {
  cerr << "Unknown exception." << endl;
  return -3;
}
