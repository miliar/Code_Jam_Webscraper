//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

int d[1001];
int n, l;
double t;
bool put[1001];

int calcIm()
{
    double tm = 0;
    for (int i = 0; i < n; ++i)
    {
        if (put[i] && tm >=  t)
        {
            tm += d[i];
        } else if (put[i] && tm + d[i] * 2 > t)
        {
            tm = t + d[i] - (t - tm) / 2;
        } else
            tm = tm + d[i] * 2;
    }
    return (int) (tm + 0.5);
}

int calc()
{
    int res = 0;
   if (l == 0)
   {
       for (int i = 0; i < n; ++i)
       {
           res += d[i] * 2;
       }
       return res;
   } else if (l == 1)
   {
       int min_v = 100000000;
       for (int i = 0; i < n; ++i)
       {
           put[i] = true;
           int x = calcIm();
           put[i] = false;
           if (x < min_v) min_v = x;
       }
       return min_v;
   } else if (l == 2)
   {
       int min_v = 100000000;
       for (int i = 0; i < n; ++i)
       {
           for (int j = i + 1; j <n; ++j)
           {
               put[i] = true; put[j] = true;

               int x = calcIm();
               if (x < min_v) min_v = x;

               put[i] = put[j] = false;
           }
       }
       return min_v;
   }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int KS, ks, c;

    scanf("%d", &KS);
    for (ks=1; ks<=KS;++ks)
    {
        printf("Case #%d: ", ks);
        scanf("%d %lf %d %d", &l, &t, &n, &c);
        for (int i = 0; i < c; ++i)
            scanf("%d", &d[i]);
        for (int i = c; i < n; ++i)
        {
            d[i] = d[i-c];
        }
        printf("%d\n", calc());
    }
}
