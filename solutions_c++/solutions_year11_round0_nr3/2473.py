#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);

  int t;
  in >> t;
  for (int i = 0; i < t; ++i)
  {
    int n, mc = -1, xc = 0, sc = 0;
    in >> n;
    for (int j = 0; j < n; ++j)
    {
      int c;
      in >> c;
      if (mc < 0 || c < mc)
        mc = c;
      xc ^= c;
      sc += c;
    }
    cout << "Case #" << 1 + i << ": ";
    if (xc)
      cout << "NO"; else
      cout << sc - mc;
    cout << "\n";
  }

  return 0;
}

