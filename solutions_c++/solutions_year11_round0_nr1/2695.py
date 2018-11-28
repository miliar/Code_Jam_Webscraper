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
    int nb; in >> nb;

    int op = 1;
    int bp = 1;
    int ot = 0;
    int bt = 0;
    int t = 0;

    for (int i = 0; i < nb; i++)
    {
      int pos;
      char x; in >> x;
      if (x == 'O')
      {
        in >> pos;
        // std::cout << "O " << pos << " ";
        ot = max(t+1, ot + abs(op-pos) + 1);
        op = pos;
        t = ot;
      }
      else
      {
        in >> pos;
        // std::cout << "B " << pos << " ";
        bt = max(t+1, bt + abs(bp-pos) + 1);
        bp = pos;
        t = bt;
      }
    }

    //    std::cout << std::endl;

    cout << "Case #" << T + 1 << ": " << t << endl;
  }

  return 0;
}
