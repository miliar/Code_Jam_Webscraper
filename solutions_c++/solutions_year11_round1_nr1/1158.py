#include <iostream>
#include <fstream>

using namespace std;

bool check_n(long long n, int pd)
{
  for (int i = 0; i < 100 && n >= 1; ++i, --n)
    if (n * pd % 100 == 0)
      return true;
  return false;
}

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);
  int t;
  in >> t;
  for (int i = 0; i < t; ++i)
  {
    long long n;
    int pd, pg;
    in >> n >> pd >> pg;
    cout << "Case #" << 1 + i << ": " <<
      ((pg != 100 || pd == 100) && (pg != 0 || pd == 0) && check_n(n, pd) ? "Possible" : "Broken") <<
      "\n";
  }
  return 0;
}

