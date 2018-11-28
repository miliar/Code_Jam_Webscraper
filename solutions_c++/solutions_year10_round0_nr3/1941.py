#include <iostream>
#include <fstream>
#include <utility>
#include <stdint.h>

using namespace std;

int main()
{
  ifstream fin("C-small.in");
  ofstream fout("C-small.out");

  int T;
  fin >> T;
  for(int test = 1; test <= T; test++)
  {
    int R, k;
    size_t N;
    fin >> R;
    fin >> k;
    fin >> N;

    int *g = new int[N];
    for(size_t i = 0; i < N; i++)
    {
      fin >> g[i];
    }

    uint64_t *gn = new uint64_t[N];
    size_t *gs = new size_t[N];
    for(size_t i = 0; i < N; i++)
    {
      uint64_t n = 0;
      size_t s;
      for(s = 0; s < N; s++)
      {
        if(n + g[(i + s) % N] > (uint64_t) k)
        {
          break;
        }
        n += g[(i + s) % N];
      }
      gn[i] = n;
      gs[i] = s;
    }
/*
    for(size_t i = 0; i < N; i++)
    {
      cout << gn[i] << " " << gs[i] << endl;
    }
*/
    uint64_t money = 0;
    size_t pos = 0;
    for(int i = 0; i < R; i++)
    {
//      cout << pos << endl;
      money += gn[pos];
      pos += gs[pos];
      pos %= N;
    }

    cout << "Case #" << test << ": " << money << endl;
    delete [] g;
  }
}

