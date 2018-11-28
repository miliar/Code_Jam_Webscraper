// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int T, N;

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

  input >> T;

  for (int t = 0; t < T; ++t) {
    input >> N;
    int result = 0;
    int maxA = 0;
    int c[10002] = {0};

    for (int n = 0; n < N; ++n) {
      unsigned long a;
      unsigned long b;
      input >> a;
      input >> b;
      //cout << a << ' ' << b << endl;
      c[a] = b;
      maxA < a ? maxA = a : maxA = maxA;
    }

    if (N <= 1)
    {
      cout << "Case #" << t + 1 << ": " << 0 << '\n';
      continue;
    }

    for (int i = 0; i <= maxA; ++i)
    {
      if (c[i] == 0)
        continue;
      //cout << "i: " << i << ": " << c[i] << endl;
      for (int j = i + 1; j <= maxA; ++j)
      {
        if (c[j] == 0)
          continue;
        //cout << "j: " << j << ' ';
        if (c[j] < c[i])
          ++result;
        //cout << c[j] << " Result: " << (c[i] < c[j]) << endl;
      }
    }
    cout << "Case #" << t + 1 << ": " << result << '\n';
  }
  cout.flush();
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
