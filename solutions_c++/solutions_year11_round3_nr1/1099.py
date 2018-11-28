#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <deque>
#include <algorithm>
#include <utility>

using namespace std;

ifstream Ifs;
ofstream Ofs;
int T;
int R, C;

vector<vector<int> > ReadData()
{
  Ifs >> R >> C;
  vector<vector<int> > pic(R);
  string tmp;
  for (int i = 0; i < R; ++i)
  {
    Ifs>>tmp;
    for(int j = 0; j < C; ++j)
    {
      if (tmp[j] == '.')
        pic[i].push_back(0);
      else
        pic[i].push_back(1);
    }
  }
  return pic;
}
bool Calculate(vector<vector<int> > &pic)
{
  for(int i = 0; i < R; ++i)
  {
    for (int j = 0; j < C; ++j)
    {
      if(pic[i][j] == 0) 
      {
        if (i != 0 && (pic[i-1][j] == 2 || pic[i-1][j] == 3)) return false;
        if (j != 0 && (pic[i][j-1] == 2 || pic[i][j-1] == 4)) return false;
        continue;
      }
      int t1, t2;
      if (i != 0 && (pic[i-1][j] == 2 || pic[i-1][j] == 3)) t1 = pic[i-1][j]+2; else t1 = -1;
      if (j != 0 && (pic[i][j-1] == 2 || pic[i][j-1] == 4)) t2 = pic[i][j-1]+1; else t2 = -1;
      if (t1 == -1 && t2 == -1)
        pic[i][j] = 2;
      else
        if(t1 == -1 && t2 != -1)
          pic[i][j] = t2;
        else if (t2 == -1 && t1 != -1)
          pic[i][j] = t1;
        else if (t1 == t2)
          pic[i][j] = t1;
        else return false;
    }
    if (pic[i][C-1] == 2 || pic[i][C-1] == 4) return false;
  }
  for(int i = 0; i <C; ++i)
  {
    if (pic[R-1][i] == 2 || pic[R-1][i] == 3) return false;
  }
}
void WriteResult(vector<vector<int> >& pic)
{
  for (int i = 0; i < R; ++i)
  {
    for(int j = 0; j < C; ++j)
    {
      if (pic[i][j] == 0) Ofs<<".";
      if (pic[i][j] == 2 || pic[i][j] == 5) Ofs<<"/";
      if (pic[i][j] == 3 || pic[i][j] == 4) Ofs << "\\";
    }
    Ofs <<"\n";
  }
}

int _tmain(int argc, _TCHAR* argv[])
{
  Ifs.open("A-large.in");
  Ofs.open("result.dat");
  Ifs >> T;
  for (int i = 0; i < T; ++i)
  {
    Ofs <<"Case #"<<(i+1)<<":\n";
    vector<vector<int> > pic = ReadData();
    bool res = Calculate(pic);
    if(res)
      WriteResult(pic);
    else
      Ofs<<"Impossible\n";
  }
  Ifs.close();
  Ofs.close();
  return 0;
}

