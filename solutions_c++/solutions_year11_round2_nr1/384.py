#include <cstdio>

using namespace std;

int n;
char b[200][200];
int won[200], tot[200];
double wp[200], owp[200], oowp[200];

int main()
{
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d", &n);
    for (int j = 0; j < n; j++) 
    {
      scanf("%s", b[j]);
      won[j] = tot[j] = 0;
      for (int k = 0; k < n; k++)
      {
        if (b[j][k] != '.') tot[j]++;
        if (b[j][k] == '1') won[j]++;
      }
      wp[j] = won[j] / (double)tot[j];
    }
    for (int j = 0; j < n; j++)
    {
      double sumwp = 0.0;
      int ile = 0;
      for (int k = 0; k < n; k++)
        if (j != k && b[j][k] != '.')
          sumwp += (won[k] - (b[k][j] - '0')) / (double)(tot[k] - 1), ile++;
      owp[j] = sumwp / (ile);
    }
    for (int j = 0; j < n; j++)
    {
      double sumowp = 0.0;
      int ile = 0;
      for (int k = 0; k < n; k++)
        if (j != k && b[j][k] != '.')
          sumowp += owp[k], ile++;
      oowp[j] = sumowp / ile;
    }
    printf("Case #%d:\n", i + 1);
    for (int j = 0; j < n; j++)
      printf("%.9lf\n", 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]);

  }
  return 0;
}
