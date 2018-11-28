#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
  int T, R, C;
  vector<string> pict;
  bool imp;

  ifstream in;
  ofstream out;

  if (argc == 3)
  {
    in.open(argv[1]);
    if (!in.is_open())
    {
      cerr << "Error opening " << argv[1] << endl;
      return 0;
    }
    out.open(argv[2]);
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening " << argv[2] << endl;
      return 0;
    }
  }
  else
  {
    in.open("in.txt");
    if (!in.is_open())
    {
      cerr << "Error opening in.txt" << endl;
      return 0;
    }
    out.open("out.txt");
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening out.txt" << endl;
      return 0;
    }
  }

  in >> T;
  for (int i = 0; i < T; i++)
  {
    out << "Case #" << i + 1 << ":" << endl;
    in >> R >> C;
    pict.resize(R);
    for (int j = 0; j < R; j++)
      in >> pict[j];

    imp = false;
    for (int j = 0; j < R; j++)
    {
      for (int k = 0; k < C; k++)
      {
        if (pict[j][k] == '#')
        {
          if (j == R - 1 || k == C - 1)
          {
            imp = true;
            break;
          }
          if (pict[j][k + 1] == '#' && pict[j + 1][k] == '#' && pict[j + 1][k + 1] == '#')
          {
            pict[j][k]         = '/';
            pict[j + 1][k + 1] = '/';
            pict[j][k + 1]     = '\\';
            pict[j + 1][k]     = '\\';
          }
          else
          {
            imp = true;
            break;
          }
        }
      }
      if (imp) break;
    }

    if (imp)
      out << "Impossible" << endl;
    else
      for (int j = 0; j < R; j++)
        out << pict[j] << endl;
  }

  return 0;
}

