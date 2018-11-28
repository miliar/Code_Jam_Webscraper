#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

int t, c, d, n;
int p[30][30];
string tt, s;
bool r[30][30];
char stack[200];

int main()
{
  //freopen("B-small-attempt0.in", "r", stdin);
  //freopen("B-small-attempt0.out", "w", stdout);
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    for (int j = 0; j < 30; j++)
    {
      for (int k = 0; k < 30; k++)
        p[j][k] = -1, r[j][k] = false;
    }
    cin >> c;
    for (int j = 0; j < c; j++)
    {
      cin >> tt;
      //cout << tt << '\n';
      p[tt[0] - 'A'][tt[1] - 'A'] = tt[2] - 'A';
      p[tt[1] - 'A'][tt[0] - 'A'] = tt[2] - 'A';
    }                                        
    cin >> d;
    for (int j = 0; j < d; j++)
    {
      cin >> tt;
      r[tt[0] - 'A'][tt[1] - 'A'] = true;
      r[tt[1] - 'A'][tt[0] - 'A'] = true;
    } 
    cin >> n;
    cin >> s;
    int h = 0;
    for (int j = 0; j < n; j++)
    {
      if (h == 0)
      {
        stack[h++] = s[j];
        continue;
      }
      if (h > 0 && p[s[j] - 'A'][stack[h - 1] - 'A'] != -1)
      {
        stack[h - 1] = p[s[j] - 'A'][stack[h - 1] - 'A'] + 'A';
        continue;
      }
      bool OK = false;
      for (int k = 0; k < h; k++)
      {
        if (r[stack[k] - 'A'][s[j] - 'A'])
        {
          h = 0;
          OK = true;
          break;
        }
      }
      if (OK)
        continue;
      stack[h++] = s[j];
    }
    printf("Case #%d: [", i + 1);
    for (int j = 0; j < h; j++)           
    {
      if (j < h - 1)
        cout << stack[j] << ", ";
      else
        cout << stack[j] << ']' << '\n';
    }
    if (h == 0)
      cout << ']' << '\n';
  }
  return 0;
}

