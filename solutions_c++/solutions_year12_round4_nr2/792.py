#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxN = 11;
const double eps = 1e-8;
int n, p[maxN];
double w, h, r[maxN];
double ansx[maxN], ansy[maxN];

bool check()
{
    double x = 0, y = 0, ny;
    double k = r[p[0]];
    ansx[p[0]] = ansy[p[0]] = 0;
    double delta;
    
    for (int i = 1; i < n; i++)
    {
        delta = x + r[p[i]] + r[p[i - 1]];
        if (delta <= w + eps)
        {
            ansx[p[i]] = delta;
            x = ansx[p[i]];
            if (y > eps) ansy[p[i]] = y + r[p[i]];
            else ansy[p[i]] = 0;
            k = max(k, ansy[p[i]] + r[p[i]]);            
        }
        else
        {
            y = k; x = 0;
            ansx[p[i]] = 0;
            ansy[p[i]] = k + r[p[i]];
            k = max(k, ansy[p[i]] + r[p[i]]);
        }
        if (ansy[p[i]] > h) return false;
    }
    return true;
    
}
int main() 
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--)
    {
        printf("Case #%d: ", ++cas);
        scanf("%d", &n);
        scanf("%lf%lf", &w, &h);
        for (int i = 0; i < n; i++) 
            scanf("%lf", &r[i]);
        for (int i = 0; i < n; i++) p[i] = i;
        do
        {
            if (check())
            {
                for (int i = 0; i < n; i++)
                {
                    printf("%.1f %.1f", ansx[i], ansy[i]);
                    if (i == n - 1) printf("\n");
                    else printf(" ");
                }
                break;
            }
            
        }while (next_permutation(p, p + n));
        
    }
    return 0;
}

