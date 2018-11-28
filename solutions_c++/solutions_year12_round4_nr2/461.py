#include<iostream>
#include<cstdio>
#include<algorithm>
#include<utility>
using namespace std;
const int maxn = 1010;
pair<double, int> datr[maxn];
double w, h;
int n;
void init()
{
     cin >> n >> w >> h;
     for (int i=0; i<n; i++)
     {
         cin >> datr[i].first;
         datr[i].second = i;
         datr[i].first = -datr[i].first;
     }
     sort(datr, datr+n);
     for (int i=0; i<n; i++) datr[i].first = -datr[i].first;
}
double ans[maxn][2];
void work(double w, double h, pair<double, int> datr[], int n, double ans[][2])
{
     double now = -datr[0].first;
     int p = 0;
     while (p < n && now+datr[p].first < w)
     {
           ans[p][0] = now + datr[p].first;
           ans[p][1] = h;
           now += datr[p].first + datr[p].first;
           p++;
     }
     if (p < n)
     {
           work(h-datr[0].first-datr[0].first, w, datr+p, n-p, ans+p);
           for (p; p<n; p++) swap(ans[p][0], ans[p][1]);
     }
}
void print()
{
     static double prt[maxn][2];
     for (int i=0; i<n; i++)
     {
         prt[datr[i].second][0] = ans[i][0];
         prt[datr[i].second][1] = ans[i][1];
     }
     for (int i=0; i<n; i++) printf(" %.4lf %.4lf", prt[i][0], prt[i][1]);
     printf("\n");
}
int main()
{
    int t;
    scanf("%d", &t);
    for (int i=1; i<=t; i++)
    {
        init();
        work(w, h, datr, n, ans);
        printf("Case #%d:", i);
        print();
    }
    return 0;
}
