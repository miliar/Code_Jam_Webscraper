#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cassert>

#define eps 1e-9
#define inf int(1e9)
#define inflong __int64(1e18)
#define abs(a) (((a) < 0) ? -(a) : (a))
#define sqr(a) ((a) * (a))
#define taskname "a"
#define sz(a) (int)a.size()
#define mp make_pair
#define pb push_back
#define forn(i, x, y) for (int i = (x); i <= (y); i++)
#define ford(i, y, x) for (int i = (y); i >= (x); i--)
                       
using namespace std;

const int maxn = int(2e5);
const int maxnn = int(2e3);
const double pi = M_PI;

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vii;
typedef vector <bool> vb;
typedef vector <vb> vbb;
typedef vector <ll> vl;
typedef vector <vl> vll;

int t, n;
int a[200][200];
int win[200], lost[200];
long double wp[200], owp[200], oowp[200];

int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  scanf("%d", &t);
  for (int i = 1; i <= t; i++)
  {
    printf("Case #%d:\n", i);
    scanf("%d", &n);
    memset(win, 0, sizeof(win));
    memset(lost, 0, sizeof(lost));
    cout.precision(20);
    for (int j = 0; j < n; j++)
    {
      for (int k = 0; k < n; k++)
      {
        char c;
        cin >> c;
        if (c == '.')
          a[j][k] = -1;
        else
        {
          a[j][k] = c - '0';
          if (a[j][k] == 1)
            win[j]++;
          else
            lost[j]++;
        }
      }            
    }
    for (int j = 0; j < n; j++)
      wp[j] = (win[j] * 1.0 / (win[j] + lost[j]));
    for (int j = 0; j < n; j++)
    {
      long double t = 0;
      int c = 0;
      for (int k = 0; k < n; k++)
      {
        if (k == j || a[k][j] == -1)
          continue;
        if (a[k][j] == 1)
          t += (win[k] - 1) * 1.0 / (win[k] + lost[k] - 1);
        else
          t += win[k] * 1.0 / (win[k] + lost[k] - 1);
        c++;
      }
      t /= c * 1.0;
      owp[j] = t;
    }
    for (int j = 0; j < n; j++)
    {
      long double t = 0;
      int c = 0;
      for (int k = 0; k < n; k++)
      {
        if (k == j || a[k][j] == -1)
          continue;
        t += owp[k];
        c++;
      }
      t /= c * 1.0;
      oowp[j] = t;
    }
    cout.precision(20);
    //cout << owp[1] << " " << owp[2] << '\n'; 
    //cout << wp[0] << " " << owp[0] << " " << oowp[0] << '\n'; 
    for (int j = 0; j < n; j++)
      cout << wp[j] / 4.0 + owp[j] / 2.0 + oowp[j] / 4.0 << "\n";
  }  
  return 0;
}


