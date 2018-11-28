/*
for 15 : quot 5 / remain 0
5 5 5       : best = 5 (quot)
4 5 6 (*)   : best = 6 (quot + 1)

for 16 : quot 5 / remain 1
5 5 6       : best = 6 (quot + 1)

for 17 : quot 5 / remain 2
5 5 7 (*)   : best = 7 (quot + 2)
5 6 6       : best = 6 (quot + 1)
*/

#include <iostream>
#include <list>
#include <string>

using namespace std;

class IntList : public list<int>
{
};

int main()
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++)
  {
    int N; cin >> N;
    int S; cin >> S;
    int P; cin >> P;
    int ok = 0;
    for (int i = 0; i < N; i++)
    {
      int total; cin >> total;
      int quot = total / 3;
      int rem  = total % 3;
      switch (rem)
      {
      case 0 : // quot or quot+1(*)
        if (quot >= P)
        {
          ok++;
        } else
        if (quot > 0 && quot + 1 == P) // (*)
        {
          if (S > 0)
          {
            S--;
            ok++;
          }
        }
        break;
      case 1 : // quot+1
        if (quot + 1 >= P)
        {
          ok++;
        }
        break;
      case 2 : // qout+1 or quot+2(*)
        if (quot + 1 >= P)
        {
          ok++;
        } else
        if (quot + 2 == P) // (*)
        {
          if (S > 0)
          {
            S--;
            ok++;
          }
        }
        break;
      }
    }
    cout << "Case #" << t << ": " << ok << endl;
  }
}