#include <fstream>
#include <vector>
#include "math.h"
#include "float.h"
#include "assert.h"

double calc(double st, double d, std::vector<int> const& pos)
{
  double res = 0;
  for (size_t i = 0; i < pos.size(); ++i)
  {
    double time = abs(pos[i] - st);
    st += d;
    if (time > res)
      res = time;
  }

  return res;
}

int main()
{

  std::ifstream fin("input.txt");
  std::ofstream fout("output.txt");

  size_t n;
  fin >> n;

  for (size_t mmm = 0; mmm < n; ++mmm)
  {
    int N, L, H;
    fin >> N >> L >> H;
    std::vector<int> f;
    for (size_t i = 0; i < N; ++i)
    {
      int a;
      fin >> a;
      f.push_back(a);
    }

    bool res = true;
    size_t j;
    for (j = L ; j <= H; ++j)
    {
      res = true;      
      for (size_t i = 0; i < N; ++i)
      {
        if ((f[i] % j != 0) && (j % f[i] != 0))
        {
          res = false;
          break;
        }
      }
      if (res)
        break;
    }

    fout << "Case #" << (mmm + 1) << ": ";
    if (res)
      fout << j;
    else
      fout << "NO";
    fout << std::endl;
  }


  fin.close();
  fout.close();
}