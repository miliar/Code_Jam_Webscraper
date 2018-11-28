
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int s;
bool bacteria[2][200][200];

bool apply()
{
  bool more = false;
  for (int x = 1; x <= 100; x++)
    for (int y = 1; y <= 100; y++)
      if (bacteria[s][x][y])
      {
        more = true;
        bacteria[1-s][x][y] = !(!bacteria[s][x-1][y] && !bacteria[s][x][y-1]);
      }
      else
        bacteria[1-s][x][y] = bacteria[s][x-1][y] && bacteria[s][x][y-1];

  s = 1-s;
  return more;
}

void solve(int CASE)
{
  memset(bacteria, 0, sizeof bacteria);
  int r;
  int x0, y0, x1, y1;
  cin >> r;
  s = 0;

  for (int i = 0; i < r; i++)
  {
    cin >> x0 >> y0 >> x1 >> y1;
    for (int x = x0; x <= x1; x++)
      for (int y = y0; y <= y1; y++)
        bacteria[s][x][y]++;
  }

  int i = 0;
  while (apply()) i++;

  printf("Case #%d: %d\n", CASE, i);



}

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) solve(i+1);
  return 0;
}
