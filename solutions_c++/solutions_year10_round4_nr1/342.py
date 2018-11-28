#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
fstream inp, out;

const int oo = 0x3f3f3f3f;

const int N = 128;

char a[N][N];

int dist(int x, int y, int a, int b)
{
    return abs(x-a) + abs(y-b);
}

int n;

bool good(int x, int y)
{
  for (int i =0; i <= 2*n; ++i)
  for (int j =0; j <= 2*n; ++j)
  if ('0'<= a[i][j])
  {
      int dx = abs(i - x);
      int dy = abs(j - y);
      char t = a[i][j];

      if (x + dx < N)
      {
            if (y + dy < N)
                if (a[x+dx][y+dy] >= '0' && a[x+dx][y+dy] != t)
                 return false;
            if (y - dy >= 0)
                if (a[x+dx][y-dy] >= '0' && a[x+dx][y-dy] != t) 
                return false;
      }
      if (x - dx >= 0)
      {
            if (y + dy < N)
                if (a[x-dx][y+dy] >= '0' && a[x-dx][y+dy] != t) 
                return false;
            if (y - dy >= 0)
                if (a[x-dx][y-dy] >= '0' && a[x-dx][y-dy] != t) 
                return false;
      }
  }
  return true;
}

int main(int argc, char *argv[])
{
    int lower = 0, upper = oo;
    if (argc < 2) { cout << "specify input/output" << endl; return 1;}
    if (argc >= 3) { sscanf(argv[2], "%d", &lower); }
    if (argc >= 4) { sscanf(argv[3], "%d", &upper); }
    char lowers[32];
    sprintf(lowers, "%07d", lower);
    string iname = string(argv[1]);
    string oname = iname.substr(0, iname.size() - 3) + string(".") + string(lowers) + string(".out");
    inp.open (iname.c_str(), fstream::in);
    out.open (oname.c_str(), fstream::out);
    int T;
    inp >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        inp >> n; inp.getline(a[0], N);
        memset(a, 0, sizeof(a));
        for (int i = 0; i < 2*n-1; ++i)
        {
             inp.getline(&a[i+1][1], N);
             //cout << &a[i+1][1] << endl;
        }
        //cout << n << endl;
        if (lower <= cs && cs < upper)
        {
           int best = oo;
           for (int i = 0; i <= 2*n+1; ++i)
           for (int j = 0; j <= 2*n+1; ++j)
           {
                
                int size = max(max(dist(1, n, i, j), dist(n, 1, i, j)), max(dist(n, 2*n-1, i, j), dist(2*n-1, n, i, j))) + 1;
                if (size*size - n*n > best) continue;
                if (good(i, j)) {
                    best = size*size - n*n;
                    //cout << "at " << i << " " << j << " " << size << " " << best << endl;
                }
           }
           cout << "solved case " << cs << endl;
           out << "Case #" << cs << ": " << best << endl; 
        }
    }
    return 0;
}