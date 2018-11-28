#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define all(x) x.begin(), x.end()
#define mp make_pair

const int inf = (1 << 30) - 1;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;
typedef char str[200];

str s1[200], s, s2[2000];
bool u[200];
int iter;

void go ()
{
  int n, m;
  scanf ("%d", &n);
  gets (s);
  for (int i = 0; i < n; i ++)
    gets (s1[i]);
  scanf ("%d", &m);
  gets (s);
  for (int i = 0; i < m; i ++)
    gets (s2[i]);
  int ans = 0;
  memset (u, 0, sizeof (u));
  int num = n;
  for (int i = 0; i < m; i ++)
    {
      int x = -1;
      for (int j = 0; j < n; j ++)
        if (strcmp (s2[i], s1[j]) == 0)
          {
            x = j;
            break;
          }
      if (x != -1)
        {
          if (!u[x])
            {
              if (num == 1)
                {
                  memset (u, 0, sizeof (u));
                  ans ++;
                  num = n - 1;
                }
               else
                {
                  num --;
                }
              u[x] = true;
            }
        }
    }
  printf ("Case #%d: %d\n", iter+1, ans);
}

int main ()
{
  freopen ("in", "r", stdin);
  freopen ("out", "w", stdout);
  int n;
  scanf ("%d", &n);
  gets (s);
  cerr << s << endl;
  for (iter = 0; iter < n; iter ++)
    go ();
}
