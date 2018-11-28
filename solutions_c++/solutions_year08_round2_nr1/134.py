#include <iostream>
#include <math.h>

using namespace std;

double eps = 1e-7;
double pi = 3.1415296535897932;

double Abs(double x)
{
  if (x > 0)
    return x;
  else
    return -x;
}

double Abs(int x)
{
  if (x > 0)
    return x;
  else
    return -x;
}
            
long long x[100000];
long long y[100000];

long long col[10][10];

int main()
{
  long long i, j, k, t_count, test, n, m, tmp, A, B, C, D, x0, y0, M, t;

  long long x1, x2, x3, y1, y2, y3;

  freopen("A-small.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    memset(col, 0, sizeof(col));

    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

    x[0] = x0;
    y[0] = y0;
    col[x[0] % 3][y[0] % 3]++;

    for (i = 1; i < n; i++)
    {
      x[i] = (x[i - 1] * A + B) % M;
      y[i] = (y[i - 1] * C + D) % M;
//      cout << x[i] << ' ' << y[i] << endl;
      col[x[i] % 3][y[i] % 3]++;
    }

    long long ans = 0, bonus;

    for (i = 0; i < 3; i++)
      for (j = 0; j < 3; j++)
      {
        t = col[i][j];
        bonus = t * (t - 1) * (t - 2) / 6;

        if (bonus < 0)
          bonus = 0;

        ans += bonus;
      }


/*    for (i = 0; i < 3; i++)
    {
      for (j = 0; j < 3; j++)
        cout << col[i][j] << ' ';
      cout << endl;
    }
    cout << ans << endl;*/


    for (i = 0; i < 9; i++)
      for (j = i + 1; j < 9; j++)
        for (k = j + 1; k < 9; k++)
        {
          x1 = i / 3;
          y1 = i % 3;

          x2 = j / 3;
          y2 = j % 3;

          x3 = k / 3;
          y3 = k % 3;

          if ((x1 + x2 + x3) % 3 == 0 && ((y1 + y2 + y3) % 3 == 0))
            ans += col[x1][y1] * col[x2][y2] * col[x3][y3];           

        }

    cout << ans << endl;

  }

  return 0;
}