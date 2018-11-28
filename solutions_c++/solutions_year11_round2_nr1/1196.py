#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);
  int t;
  in >> t;
  cout << setprecision(12);
  for (int i = 0; i < t; ++i)
  {
    int n;
    string dummy;
    in >> n;
    getline(in, dummy);

    string matrix[n];
    double wp[n], owp[n], oowp[n];
    for (int j = 0; j < n; ++j)
    {
      string s;
      getline(in, s);
      matrix[j] = s;
      int cnt = 0, win = 0;
      for (int k = 0; k < n; ++k)
      {
        if (s[k] != '.') ++cnt;
        if (s[k] == '1') ++win;
      }
      wp[j] = (double)win / cnt;
    }
    for (int k = 0; k < n; ++k)
    {
      double sum = 0;
      int cnt0 = 0;
      for (int j = 0; j < n; ++j)
        if (matrix[j][k] != '.')
        {
          ++cnt0;
          int cnt1 = 0, win1 = 0;
          for (int l = 0; l < n; ++l)
            if (l != k)
            {
              if (matrix[j][l] != '.') ++cnt1;
              if (matrix[j][l] == '1') ++win1;
            }
          sum += (double)win1 / cnt1;
        }
      owp[k] = sum / cnt0;
    }
    for (int j = 0; j < n; ++j)
    {
      double sum = 0;
      int cnt = 0;
      for (int k = 0; k < n; ++k)
        if (matrix[j][k] != '.')
        {
          ++cnt;
          sum += owp[k];
        }
      oowp[j] = sum / cnt;
    }

    cout << "Case #" << 1 + i << ":\n";
    for (int j = 0; j < n; ++j)
      cout << (.25 * wp[j] + .5 * owp[j] + .25 * oowp[j]) << "\n";
  }
  return 0;
}

