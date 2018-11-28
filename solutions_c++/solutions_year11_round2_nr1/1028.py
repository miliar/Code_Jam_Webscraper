#include <fstream>
#include <vector>

int main()
{

  std::ifstream fin("input.txt");
  std::ofstream fout("output.txt");

  size_t n;
  fin >> n;
  
  for (size_t i = 0; i < n; ++i)
  {
    size_t m;
    fin >> m;
    std::vector< std::vector< int > > res;

    for (size_t j = 0; j < m; j++)
    {
      res.push_back(std::vector< int >());
      for (size_t k = 0; k < m; k++)
      {
        char ch;
        fin >> ch;
        if (ch == '0')
          res.back().push_back(0);
        else if (ch == '1')
          res.back().push_back(1);
        else
          res.back().push_back(2);
      }
    }

    std::vector<double> played;
    std::vector<double> won;
    std::vector<double> wp;
    
    for (size_t j = 0; j < m; ++j)
    {
      double p = 0;
      double w = 0;
      for (size_t k = 0; k < m; ++k)
      {
        if (res[j][k] != 2)
          p += 1;
        if (res[j][k] == 1)
          w += 1;
      }
      played.push_back(p);
      won.push_back(w);
      wp.push_back(w / p);
    }

    std::vector<double> owp;

    for (size_t j = 0; j < m; ++j)
    {
      double res1 = 0;
      double cnt = 0;
      for (size_t k = 0; k < m; ++k)
      {
        if (res[j][k] == 2)
          continue;

        cnt += 1;
        double op = played[k] - 1;
        double ow = won[k];
        if (res[j][k] == 0)
          ow -= 1;

        res1 += (ow / op);
      }
      if (cnt != 0)
        res1 /= cnt;
      owp.push_back(res1);
    }

    fout << "Case #" << i + 1 << ":" << std::endl;

    for (size_t j = 0; j < m; ++j)
    {
      double res1 = 0;
      double cnt = 0;
      for (size_t k = 0; k < m; ++k)
      {
        if (res[j][k] == 2)
          continue;
        res1 += owp[k];
        cnt += 1;
      }

      if (cnt != 0)
        res1 /= cnt;

      fout << wp[j] * 0.25 + 0.5 * owp[j] + 0.25 * res1 << std::endl;
    }
  }

  fin.close();
  fout.close();
}