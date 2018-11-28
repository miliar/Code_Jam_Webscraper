#include <iostream>

using namespace std;

__int64 q[11][2000][11] = {0};

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int p;
    cin >> p;
    int m[2000];
    for (int i = 0; i < (1 << p); i++)
    {
      cin >> m[i];
    }
    int price[11][2000];
    for (int i = 1; i <= p; i++)
    {
      for (int j = 0; j < (1 << (p-i)); j++)
        cin >> price[i][j];
    }
    for (int i = 0; i < (1 << p); i++)
      {
        for (int j = 0; j <= m[i]; j++)
          q[0][i][j] = 0;
        for (int j = m[i]+1; j < 11; j++)
          q[0][i][j] = -1;
      }
    for (int i = 1; i <= p; i++)
    {
      for (int j = 0; j < (1 << (p-i)); j++)
      {
        for (int k = 0; k < 11; k++)
        {
          if ((q[i-1][j*2][k] < 0) || (q[i-1][j*2+1][k] < 0))
          {
            q[i][j][k] = -1;
            continue;
          }
          q[i][j][k] = price[i][j] + q[i-1][j*2][k] + q[i-1][j*2+1][k];
          if (k < 10 && (q[i-1][j*2][k+1] >= 0) && (q[i-1][j*2+1][k+1] >= 0))
            q[i][j][k] = min(q[i-1][j*2][k+1] + q[i-1][j*2+1][k+1], q[i][j][k]);
        }
      }
    }
    cout << q[p][0][0];
    cout << endl;
  }
  return 0;
}