// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

unsigned T = 0, N = 0, k = 0, R = 0;

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
  unsigned long g[1000] = {0};

  for (int t = 0; t < T; ++t)
  {
    int euros = 0;
    input >> R >> k >> N;
    int n = 0;
    int total_people = 0;
    for (n = 0; n < N; ++n)
    {
      input >> g[n];
      total_people += g[n];
    }

    n = 0;
    for (int r = 0; r < R; ++r)
    {
      int people = 0;
      while (people + g[n] <= k && people + g[n] <= total_people)
      {
        people += g[n];
        if (++n >= N)
          n = 0;
      }
      euros += people;
    }
    cout << "Case #" << t + 1 << ": " << euros << "\n";
  }
  cout.flush();

  return 0;
}
