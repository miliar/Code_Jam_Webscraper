#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 1001;
int T, N; 
double S, R, t, X;
struct Node
{
       double b, e, w;
}C[maxn];
bool operator <(Node a,Node b)
{
     return a.w < b.w;
}
double sum = 0 , sum2;
int main()
{
    scanf("%d", &T);
    //freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    for (int cas = 1; cas <= T; cas++) {
        sum2 = sum = 0;
        scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
        for (int i = 0; i < N ;i++) {
            scanf("%lf%lf%lf",&C[i].b, &C[i].e, &C[i].w);
            sum += (C[i].e - C[i].b);
        }
        sort(C, C + N);
        int pi = 0;
        double ans = 0;
        if (t * R > X - sum)
        {
              ans += (X - sum) / R;
              t -= (X - sum) / R;
        }
        else
        {
            ans += t + (X - sum - R * t) / S; 
            t = 0;
        }
        if (t != 0) {
           do
           {
              double temp = (C[pi].e - C[pi].b) / (C[pi].w + R);
              if (t > temp)  t -= temp, pi++, ans += temp;
              else
              {
               C[pi].b = C[pi].b + t * (C[pi].w + R);
               ans += t; 
               t = 0;
              } 
           }while (t != 0 && pi < N);
        }
        for (int i = pi; i < N; i++) {
            ans += (C[i].e - C[i].b) / (C[i].w + S);
        }
        printf("Case #%d: %.9lf\n",cas,ans);
    }
}
