// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <exception>
#include <vector>
#include <string>

using namespace std;

int T, Pd, Pg;
long N;


int main(int argc, const char *argv[])
{
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " fielname" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }

  input >> T;

  for (int t = 0; t < T; ++t)
  {
    cout << "Case #" << t + 1 << ": ";
    input >> N >> Pd >> Pg;

    if (N == 1L) {
      if (Pd == 0 || Pd == 100)
        cout << "Possible" << endl;
      else
        cout << "Broken" << endl;
      continue;
    }

    if (Pg == 100) {
      if (Pd == 100)
        cout << "Possible" <<endl;
      else
        cout << "Broken" << endl;
      continue;
    }

    if (Pg == 0) {
      if (Pd == 0)
        cout << "Possible" << endl;
      else
        cout << "Broken" << endl;
      continue;
    }

    long i = N;
    for (; i > 0; --i) {
      if ((i * Pd) % 100 == 0)
        break;
    }
    if (i == 0) {
      cout << "Broken" << endl;
      continue;
    }
    
    cout << "Possible" << endl;
  }
  return 0;
}
