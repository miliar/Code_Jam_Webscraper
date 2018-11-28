#include <iostream>

const int maxn = 100;

int N;
int g[maxn][maxn];
int T;

void process()
{
     int wpw[maxn],wpl[maxn];
     double owp[maxn];
     double oowp[maxn];
     for (int i = 0; i < N; ++i)
     {
         wpw[i] = 0; wpl[i] = 0;
         for (int j = 0; j < N; ++j)
             if (g[i][j] < 0)
                wpl[i]++;
             else if (g[i][j] > 0)
                  wpw[i] ++;
     }
     for (int i = 0; i < N; ++i)
     {
         double w = 0;
         for (int j = 0; j < N; ++j)
             if (i != j)
             {
                   if (wpl[j] + wpw[j] == 0)
                      continue;
                   if (g[i][j] > 0)
                   {
                        if (wpl[j] + wpw[j] > 1)
                           w +=  wpw[j] * 1.0 / (wpl[j] + wpw[j] -1);
                   }
                   else if (g[i][j] < 0)
                   { 
                       if (wpl[j] + wpw[j] > 1)
                          w += (wpw[j] - 1) * 1.0 / (wpl[j] + wpw[j] - 1);
                   }
             }
         owp[i] = w / (wpl[i] + wpw [i]);
     }
     for (int i = 0; i < N; ++i)
     {
         double w = 0;
         for (int j = 0; j < N; ++j)
             if (i != j && g[i][j] != 0)
             {
                   w += owp[j];
             }
         oowp[i] = w / (wpl[i] + wpw[i]);
     }
     double wp[maxn];
     for (int i = 0; i < N; ++ i)
         wp[i] = 0.25 * wpw[i] / (wpw[i] + wpl[i]) + 0.5 * owp[i] + 0.25 * oowp[i];
         
     printf("Case #%d:\n",T);
     for (int i = 0; i < N; ++i)
         printf("%.8lf\n",wp[i]);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int _T;
    scanf("%d",&_T);
    for (T = 1; T <= _T; ++T)
    {
        scanf("%d",&N);
        for (int i = 0; i < N; ++i)
        {
            char s[1000];
            scanf("%s",s);
            for (int j = 0; j < N; ++j)
            {
                if (s[j] == '0')
                   g[i][j] = -1;
                else if (s[j] == '.')
                     g[i][j] = 0;
                else g[i][j] = 1;
            }
        }
        process();
    }
    return 0;    
}
