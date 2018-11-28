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
    double L, t, st;
    int c;
    assert(fin);
    fin >> L;
    fin >> t;
    fin >> st;
    fin >> c;
    std::vector<double> dist;
    for (size_t i = 0; i < c; ++i)
    {
      double v;
      fin >> v;
      dist.push_back(v);
    }

    std::vector<double> pos;
    std::vector<double> pos2;
    pos2.push_back(0);
    size_t cnt = 0;
    double cur = 0;
    while (pos.size() < st)
    {
      pos.push_back(dist[cnt]);
      pos2.push_back(dist[cnt] * 2 + cur);
      cur = pos2.back();
      cnt += 1;
      cnt %= c;      
    }

    double time = 0;
    for (size_t k = 0; k < st; ++k)
    {
      time += pos[k] * 2;
    }


    
    double min = DBL_MAX;
    for (size_t i = 0; i < st; ++i)
      for (size_t j = i; j < st; ++j)
      {
        double res = 0.;
        if (L >= 1)
        {
          if (t <= pos2[i] + pos[i] * 2)
          {
            if (t <= pos2[i])
              res = pos[i];
            else
            {
              double delta = t - pos2[i];
              delta = pos[i] - delta / 2.;
              res = delta;
            }
          }
        }

        if (L >= 2 && j != i)
        {
          if (t <= pos2[j] + pos[j] * 2 - res)
          {
            if (t <= pos2[j] - res)
              res += pos[j];
            else
            {
              double delta = t - pos2[j] + res;
              delta = pos[j] - delta / 2.;
              res += delta;
            }
          }
        }

        if (time - res < min)
          min = time - res;         
        
      }

      fout << "Case #" << (mmm + 1) << ": ";
      fout << int(min + 0.1) << std::endl;
  }

  fin.close();
  fout.close();
}