#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>

using namespace std;

char combine[50][3];
char opposed[50][2];

char stack[1000];
char result[1000];

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
    for (int c = 0; c < C; c++)
      for (unsigned i = 0; i < 3; i++) { char x; in >> x; combine[c][i] = x; }

    int D; in >> D;
    for (int d = 0; d < D; d++)
      for (unsigned i = 0; i < 2; i++) { char x; in >> x; opposed[d][i] = x; }

    int N; in >> N;
    char x = -1;
    char prev = -1;
    int pos = 0;
    int spos = 0;
    bool last_opp = false;
    for (int i = 0; i < N; i++)
    {
      in >> x;
      result[pos] = x;
      // combine
      for (int c = 0; c < C; c++)
        if ((combine[c][0] == x && combine[c][1] == prev) ||
            (combine[c][0] == prev && combine[c][1] == x))
        {
          if (last_opp)
            spos--;
          result[pos - 1] = combine[c][2];
          // std::cout << "Combine " << combine[c][2] << std::endl;
          pos--;
          goto end;
        }

      // clear if opposed
      for (int i = 0; i < spos; i++)
        if (x == stack[i])
        {
          // std::cout << "Clear " << x << std::endl;
          pos = -1;
          spos = 0;
          goto end;
        }

      last_opp = false;
      // push opposed.
      for (int d = 0; d < D; d++)
        if (opposed[d][0] == x || opposed[d][1] == x)
        {
          if (x == opposed[d][0])
            stack[spos] = opposed[d][1];
          else
            stack[spos] = opposed[d][0];
          // std::cout << "Stack " << stack[spos] << std::endl;
          last_opp = true;
          spos++;
          break;
        }

    end:
      pos++;
      if (pos > 0)
        prev = result[pos - 1];
      else
        prev = -1;
    }

    cout << "Case #" << T + 1 << ": [";

    if (pos > 0)
      std::cout << result[0];
    for (int i = 1; i < pos; i++)
      std::cout << ", " << result[i];

    std::cout << ']' << std::endl;

  }

  return 0;
}
