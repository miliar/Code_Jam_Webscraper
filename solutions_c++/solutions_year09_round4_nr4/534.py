#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

const int MAX = 50;

double x[MAX], y[MAX], r[MAX];
int n;

double dist(int a, int b)
{
    return sqrt((x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b]));
}

int main()
{
    int t;
    scanf ("%d", &t);
    
    for (int c = 1; c <= t; c++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);
        }
        
        double minDiam = 1e10;
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                double diam = dist(i, j) + r[i] + r[j];
                double resp = diam;
                
                x[n] = (x[i] + x[j]) / 2;
                y[n] = (y[i] + y[j]) / 2;
                
                for (int k = 0; k < n; k++)
                {
                    if (k == i || k == j) continue;
                    
                    if (dist(k, n) + r[k] > diam / 2.0)
                    {
                        for (int l = 0; l < n; l++)
                        {
                            if (l == i || l == j) continue;

                            if (dist(l, n) + r[l] > diam / 2.0)
                            {
                                double d = dist(k, l) + r[k] + r[l];
                                if (d > resp)
                                {
                                    resp = d;
                                }
                            }
                        }
                    }
                }
                
                if (resp < minDiam) minDiam = resp;
            }
        }
        
        printf("Case #%d: %.6lf\n", c, minDiam / 2.0);
    }    

    return 0;    
}
