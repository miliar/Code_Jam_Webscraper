#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T = 3, tc = 0;
	scanf("%d", &T);
	while (T--)
	{
          int X, S, R, t, N;
          scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
          vector <int> speed(X, 0);
          for (int i = 0; i < N; ++i)
          {
              int b, e, s;
              scanf("%d %d %d", &b, &e, &s);
              for (int j = b; j < e && j < X; ++j)
              {
                  if (speed[j] < s)
                  {
                      speed[j] = s;
                  }
              }
          }
          sort(speed.begin(), speed.end());
          double res = .0, tt = t;
          for (int i = 0; i < X; ++i)
          {
              if (tt > .0)
              {
                  if ((R + speed[i]) * tt >= 1.0)
                  {
                      double temp = 1.0 / (R + speed[i]);
                      res += temp;
                      tt -= temp;
                  }
                  else
                  {
                      double temp = tt * (R + speed[i]);
                      res += tt + (1 - temp) / (speed[i] + S);
                      tt = -1.0;
                  }
              }
              else
              {
                  res += 1.0 / (speed[i] + S);
              }
          }
          printf("Case #%d: %.8lf\n", ++tc, res);
	}
	return 0;
}
