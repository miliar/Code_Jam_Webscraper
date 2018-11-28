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
    int r, c;
    string dummy;
    in >> r >> c;
    getline(in, dummy);
    string grid[r];
    int cnt = 0;
    for (int j = 0; j < r; ++j)
    {
      getline(in, grid[j]);
      for (int k = 0; k < c; ++k)
        if (grid[j][k] == '#')
          ++cnt;
    }
    bool possible = true;
    for (int j = 0; possible && j < r - 1; ++j)
    {
      for (int k = 0; possible && k < c - 1; ++k)
        if (grid[j][k] == '#')
        {
          if (grid[j][k + 1] == '#' && grid[j + 1][k] == '#' && grid[j + 1][k + 1] == '#')
          {
            cnt -= 4;
            grid[j][k] = '/';
            grid[j][k + 1] = '\\';
            grid[j + 1][k] = '\\';
            grid[j + 1][k + 1] = '/';
          } else
            possible = false;
        }
    }
    cout << "Case #" << 1 + i << ":\n";
    if (!possible || cnt)
    {
      cout << "Impossible\n";
    } else
    {
      for (int j = 0; j < r; ++j)
        cout << grid[j] << "\n";
    }
  }
  return 0;
}

