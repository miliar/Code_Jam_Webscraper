#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>

using namespace std;

int max(int a, int b)
{
  if (a > b) return a;
  else return b;
}

int main(int argc, char* argv[])
{
  if (argc != 2)
    return 1;

  ifstream in(argv[1]);
  if (!in.good())
    cout << "Cannot open file " << argv[1] << std::endl;

  int nt;
  in >> nt;
  for (int T = 0; T < nt; T++)
  {
    int C; in >> C;
    int res = 0;

    for (int c = 0; c < C; c++)
    {
      int x;
      in >> x;
      if ((c + 1) != x) res++;
    }

    cout << "Case #" << T + 1 << ": " << res << std::endl;

  }

  return 0;
}
