#include <fstream>
#include <vector>
#include "math.h"

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
  for (size_t t = 0; t < n; t++)
  {
    size_t h, w;
    fin >> h >> w;
    std::vector < std::vector<int> > p;
    for (size_t i = 0; i < h; ++i)
    {
      p.push_back(std::vector<int>());
      for (size_t j = 0; j < w; ++j)
      {
        char ch;
        fin >> ch;
        if (ch == '.')
          p.back().push_back(0);
        else
          p.back().push_back(1);
      }
    }

    bool res = true;

    for (size_t i = 0; i < h; ++i)
    {
      for (size_t j = 0; j < w; ++j)
      {
        if (p[i][j] == 1)
        {
          if (i + 1 == h || j + 1 == w)
            res = false;
          else if (p[i + 1][j + 1] != 1)
            res =  false;
          else if (p[i][j + 1] != 1)
            res =  false;
          else if (p[i + 1][j] != 1)
            res =  false;

          if (!res)
            break;

          p[i][j] = 2;
          p[i + 1][j] = 3;
          p[i + 1][j +  1] = 4;
          p[i][j + 1] = 5;
        }
      }
      if (!res)
        break;
    }

    fout << "Case #" << (t + 1) << ":" << std::endl;
    if (!res)
    {
      fout << "Impossible" << std::endl;
      continue;
    }

    for (size_t i = 0; i < h; ++i)
    {
      for (size_t j = 0; j < w; ++j)
      {
        if (p[i][j] == 0)
          fout << ".";
        else if (p[i][j] == 2)
          fout << "/";
        else if (p[i][j] == 3)
            fout << "\\";
        else if (p[i][j] == 4)
          fout << "/";
        else if (p[i][j] == 5)
          fout << "\\";
      }
      fout << std::endl;
    }

  }
  fin.close();
  fout.close();
}