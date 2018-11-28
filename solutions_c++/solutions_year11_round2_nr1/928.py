#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 256
char t[MAX][MAX];
double WP[MAX], adj_OWP[MAX][MAX], OWP[MAX], OOWP[MAX];
int N;

void ret_wp(int i, double &rwp, double &rwin, double &rplay)
{
  rwp = rwin = rplay = 0.0;
  for(int j = 0; j < N; j++)
  {
    if (t[i][j] == '.') continue;
    rplay += 1.0;
    if (t[i][j] == '1') rwin += 1.0;
  }
  if (rplay > 0.0)
    rwp = rwin/rplay;
}

int main(void)
{
  int caso, T;
  double rw, rp;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
      scanf("%s", t[i]);

    for(int i = 0; i < N; i++)
      ret_wp(i, WP[i], rw, rp);

    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        if (t[i][j] != '.')
        {
          char ch = t[j][i];
          t[j][i] = '.';
          ret_wp(j, adj_OWP[i][j], rw, rp);
          t[j][i] = ch;
        }

    for(int i = 0; i < N; i++)
    {
      OWP[i] = rp = 0.0;
      for(int j = 0; j < N; j++)
        if (t[i][j] != '.')
        {
          OWP[i] += adj_OWP[i][j];
          rp += 1.0;
        }
      OWP[i] /= rp;
    }
    for(int i = 0; i < N; i++)
    {
      OOWP[i] = rp = 0.0;
      for(int j = 0; j < N; j++)
        if (t[i][j] != '.')
        {
          OOWP[i] += OWP[j];
          rp += 1.0;
        }
      OOWP[i] /= rp;
    }

    printf("Case #%d:\n", caso);
    for(int i = 0; i < N; i++)
      printf("%.10lf\n", 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i]);
  }

  return(0);
}

