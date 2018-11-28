#include <cstdio>
#include <cstdlib>

int n;
int t[100][100];
double WP[100];
double OWP[100];

double calculaOWP(int a, int b)
{
  int total = 0, vitorias = 0;
  for (int i = 0; i < n; i++)
    if (t[a][i] != 0 && i != b)
    {
      total++;
      if (t[a][i] == 1)
        vitorias++;
    }
  //printf("OWP de %d sem %d é %f\n", a, b, vitorias / (double) total);
  return vitorias / (double) total;
}

void resolve()
{
  scanf("%d\n", &n);
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      char c = getchar();
      if (c == '0')
        t[i][j] = -1;
      else if (c == '1')
        t[i][j] = 1;
      else if (c == '.')
        t[i][j] = 0;
      else
      {
        printf("Erro!!!!\n");
        abort();
      }
    }
    getchar();
  }
  
  for (int i = 0; i < n; i++)
  {
    int total = 0, vitorias = 0;
    for (int j = 0; j < n; j++)
      if (t[i][j] != 0)
      {
        total++;
        if (t[i][j] > 0)
          vitorias++;
      }
    WP[i] =  vitorias / (double) total;
    //printf("WP[%d] == %f\n", i, WP[i]);
  }
  
  for (int i = 0; i < n; i++)
  {
    int count = 0;
    OWP[i] = 0;
    for (int j = 0; j < n; j++)
      if (t[i][j] != 0)
      {
        count++;
        OWP[i] += calculaOWP(j,i);
      }
    OWP[i] /= count;
    //printf("OWP[%d] == %f\n", i, OWP[i]);
  }
  
  for (int i = 0; i < n; i++)
  {
    double res = 0;
    int total = 0;
    for (int j = 0; j < n; j++)
      if (t[i][j] != 0)
      {
        res += OWP[j];
        total++;
      }
    res /= total;
    printf("%.12lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * res);
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  
  for (int i = 1; i <= T; i++)
  {
    printf("Case #%d:\n", i);
    resolve();
  }
  
  return 0;
}
