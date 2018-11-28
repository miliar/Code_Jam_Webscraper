#include<iostream>
#include<cstdio>
using namespace std;
const int maxn = 10010;
int datd[maxn], dati[maxn], d, n;
void init()
{
     scanf("%d", &n);
     for (int i=0; i<n; i++) scanf("%d%d", datd+i, dati+i);
     scanf("%d", &d);
}
bool work()
{
     static int h[maxn];
     h[0] = datd[0]+datd[0];
     if (h[0] >= d) return true;
     int i, j;
     int que[maxn], front, rear;
     que[front=0] = 0; rear = 1;
     for (i=1; i<=n; i++)
     {
         h[i] = -1;
         while (front < rear && h[que[front]] < datd[i]) front++;
         if (front < rear) h[i] = datd[i] + min(dati[i], datd[i]-datd[que[front]]);
         else return false;
         if (h[i] >= d) return true;
         if (front >= rear || h[i] > h[que[rear-1]]) que[rear++] = i;
     }
     return false;
}
int main()
{
    int t;
    scanf("%d", &t);
    for (int i=1; i<=t; i++)
    {
        init();
        printf("Case #%d: %s\n", i, work() ? "YES" : "NO");
    }
    return 0;
}
