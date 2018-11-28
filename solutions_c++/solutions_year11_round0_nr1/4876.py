#include <fstream>
#include <iostream>
#include <cassert>
#include <cmath>
#include <stdexcept>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <cctype>
#include <algorithm>

using namespace std;

typedef unsigned long long Ullong;


int main()
{

  unsigned int T, P;
  int N;
  char R, curR;
  vector<int> P0s, P1s;
  vector<char> Rs;

  cin >> T;
  
  for (unsigned int k = 0; k < T; k++)
  {
    P0s.clear();  P1s.clear(); 
    Rs.clear();

    cin >> N;
    for (int n = 0; n < N; n++)
    {
      cin >> R >> P;
      Rs.push_back(R);
      if (R == 'O')
        P0s.push_back(P);
      else
        P1s.push_back(P);
    }
    for (int p0 = P0s.size()-1; p0 > 0; p0--)
      P0s[p0] = abs(P0s[p0] - P0s[p0-1]);
    for (int p1 = P1s.size()-1; p1 > 0; p1--)
      P1s[p1] = abs(P1s[p1] - P1s[p1-1]);
    P0s[0] -= 1;  P1s[0] -= 1;

  int p0 = 0;
  int p1 = 0;
  curR = Rs[0];
  int t = 0;
  int dt = 0;
  if (curR == 'O')
  {
    dt = P0s[0];
    p0++;
  } else
  {
    dt = P1s[0];
    p1++;
  }
  dt ++;

  for (int n = 1; n < N; n++)
  {
    if (Rs[n] == curR)
    {
      if (curR == 'O')
      {
        dt += P0s[p0] + 1;
        p0++;
      } else
      { dt += P1s[p1] + 1;
        p1++;
      }
    }
    else
    {
      curR = Rs[n];
      t += dt;
      if(curR == 'O') {
        if (P0s[p0] - dt > 0)
          dt = P0s[p0] - dt;
        else
          dt = 0;
        p0++;
      } else {
        if (P1s[p1] - dt > 0)
          dt = P1s[p1]-dt;
        else
          dt = 0;
        p1++;
      }
      dt++;
    }
  }
  t += dt;

  cout << "Case #" << k+1 << ": " << t << endl;
  }
  return 0;
}

