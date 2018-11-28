// Daremonai
// OS: Ubuntu
// Compiler version: g++ 4.5.2

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int N;

int main(int argc, const char *argv[])
try {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " filename" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }
  int T = 0;
  input >> T;
  int a[101][101] = { -1 };
  double wp[101] = { -1 };
  double owp[101] = { -1 };
  double oowp[101] = { -1 };
  double count[101] = { 0 };
  double rpi = 0;
  cout.precision(12);
  for(int t = 1; t <= T; ++t) {
    input >> N;
    rpi = 0;

    string s;

    int won = 0;
    for (int n = 0; n < N; ++n) {
      input >> s;
      count[n] = 0;
      won = 0;
      for (int j=0;j < N; ++j) {
        if (s[j] == '.')
          a[n][j] = -1;
        else if (s[j] == '1') {
          a[n][j] = 1;
          ++count[n];
          ++won;
        }
        else {
          a[n][j] = 0;
          ++count[n];
        }
      }
      wp[n] = won*1.0/count[n];
    }

    double wp2;
    int skip = 1;
    for (int j = 0; j < N; ++j) {
      wp2 = 0;
      skip = 1;
      for (int n = 0; n < N; ++n) {
        if (j == n)
          continue;
        if (a[n][j] == -1) {
          ++skip;
          continue;
        } else if (a[n][j] == 1) {
          wp2 += (wp[n] * count[n] - 1) / (count[n] - 1);
        } else {
          wp2 += (wp[n] * count[n]) / (count[n] - 1);
        }
      }

      owp[j] = wp2*1.0 / (N-skip);
    }

    double owp2;
    for (int n = 0; n < N; ++n) {
      oowp[n] = 0;
      skip = 1;
      for (int n2=0;n2<N;++n2) {
        if(n2==n)
          continue;
        if (a[n][n2] == -1) {
          ++skip;
          continue;
        }
        oowp[n] += owp[n2];
      }
      oowp[n] = oowp[n]*1.0 / (N-skip);
    }
    
    cout << "Case #" << t << ":" << endl;
    for (int n = 0; n < N; ++n) {
      rpi = (0.25 * wp[n]) + (0.50 * owp[n]) + (0.25 * oowp[n]);
      cout << rpi << endl;
    }
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
