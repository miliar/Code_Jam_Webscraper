#include<iostream>

using namespace std;

int t, n, m;
int a[10001];
int ch[10001];
int p[10001];
int v;
int f[10001][2];




int main()
{
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int inf = 200000;
  cin >> t;
  for (int tt = 0; tt < t; tt++)
  {
    cin >> n >> v;
    for (int i = 1; i <= n/2; i++)
    {
      cin >> p[i] >> ch[i];
    }
    for (int i = n/2+1; i <= n; i++)
      cin >> a[i];
  
/*    for (int i = n/2; i >= 1; i--)
    {
      if (p[i] == 1) 
        a[i] = a[2*i] & a[2*i+1];
      else
        a[i] = a[2*i] || a[2*i+1];
    }
*/
    for (int i = n/2+1; i<=n; i++)
    {
      f[i][a[i]] = 0;
      f[i][1-a[i]] = inf;
    }

    for (int i = n/2; i >= 1; i--)
    {
      f[i][0] = inf;
      f[i][1] = inf;
      if (p[i])
      {
        f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][0]);
        f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][1]);
        f[i][0] = min(f[i][0],f[2*i][1] + f[2*i+1][0]);
        f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][1]);
        if (ch[i])
        {
          f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][0] + 1);
          f[i][1] = min(f[i][1],f[2*i][0] + f[2*i+1][1] + 1);
          f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][0] + 1);
          f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][1] + 1);
        }
      }
      else
      {
        f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][0]);
        f[i][1] = min(f[i][1],f[2*i][0] + f[2*i+1][1]);
        f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][0]);
        f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][1]);
        if (ch[i])
        {
          f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][0] + 1);
          f[i][0] = min(f[i][0],f[2*i][0] + f[2*i+1][1] + 1);
          f[i][0] = min(f[i][0],f[2*i][1] + f[2*i+1][0] + 1);
          f[i][1] = min(f[i][1],f[2*i][1] + f[2*i+1][1] + 1);
        }
      }
    
    }
    if (f[1][v] >= inf)
      cout << "Case #" << tt+1 << ": IMPOSSIBLE" << endl; 
    else
      cout << "Case #" << tt+1 << ": " << f[1][v] << endl; 
  }

  return 0;
}