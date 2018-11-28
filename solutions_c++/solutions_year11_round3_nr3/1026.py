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
int N, L, H;

vector<int> ReadData()
{
  Ifs >> N >> L >> H;
  vector<int> notes;
  for (int i = 0; i < N; ++i)
  {
    int tmp;
    Ifs>>tmp;
    notes.push_back(tmp);
  }
  return notes;
}
int Calculate(vector<int> &notes)
{
  for(int i = L; i <= H; ++i)
  {
    int j;
    for(j = 0; j < N; ++j)
    {
      if(notes[j] % i != 0 && i % notes[j] != 0) break;
    }
    if(j == N) return i;
  }
  return -1;
}
void WriteResult(int res)
{
  if(res == -1) Ofs<<"NO\n"; else Ofs<<res<<"\n";
}

int _tmain(int argc, _TCHAR* argv[])
{
  Ifs.open("C-small-attempt0.in");
  Ofs.open("result.dat");
  Ifs >> T;
  for (int i = 0; i < T; ++i)
  {
    Ofs <<"Case #"<<(i+1)<<": ";
    vector<int> notes = ReadData();
    int res = Calculate(notes);
    WriteResult(res);
  }
  Ifs.close();
  Ofs.close();
  return 0;
}

