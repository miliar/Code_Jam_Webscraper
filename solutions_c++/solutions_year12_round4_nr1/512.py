#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

#define Cpy(x, y) (memcpy(x, y, sizeof(x)))
#define Fill(x, y) (memset(x, y, sizeof(x)))

using namespace std;

const int MAXN = 10005;

struct vine
 {
       int d, l;
 } a[MAXN];
int i, j, k, N, D, cases, cas, pos;
int len[MAXN];
priority_queue <pair <int, int> > heap;

void init()
 {
     scanf("%d", &N);
     for (i = 0; i < N; i ++)
      //{
            scanf("%d %d", &a[i].d, &a[i].l);
      //}
     scanf("%d", &a[N].d);
 }

int MAX(int X, int Y) { return X > Y? X : Y; }
int MIN(int X, int Y) { return X < Y ? X : Y; }
bool cmp(vine X, vine Y)
 {
     return (MAX(X.d - X.l, 0) < MAX(Y.d - Y.l,0)) || ((MAX(X.d - X.l,0) < MAX(Y.d - Y.l,0)) && X.d < Y.d);
 }

void work()
 {
     printf("Case #%d: ", cas);
     //sort(a, a + N, cmp);
     //while (!heap.empty()) heap.pop();
     //Fill(get, 0), get[0] = true;
     memset(len, 0, sizeof(len));
     len[0] = MIN(a[0].d, a[0].l);
     for (pos = i = j = 0; i < N; i ++)
      {
              if (!len[i])
               {
                 puts("NO");
                 return;
               }
              for (j = i + 1; j <= N; j ++)
                  if (a[j].d <= a[i].d + len[i])
                     len[j] = MAX(len[j], MIN(a[j].d - a[i].d, a[j].l));
         /*while (!heap.empty()) heap.pop();
         for (j = i + 1; j <= N; j ++)
             if (a[j].d <= a[i].d + curlen)
                heap.push(make_pair(a[j].d + MIN(a[j].d - a[i].d, a[j].l), j));
             else break;
         if (heap.empty())
          {
               puts("NO");
               return;
          }*/
         //i = heap.top().second, curlen = heap.top().first - a[i].d;
         //for (; a[i].d - a[i].l <= pos && i < N; i ++);
         //j = i; i --;
         //for (; a[j].d <= a[i].d + a[i].d - pos && j <= N; j ++);
         /*if (pos < a[-- j].d) pos = a[j].d; else
          {
                 puts("NO");
                 return;
          }*/
      }
     for (i = 0; i < N; i ++)
         if (a[i].d + len[i] >= a[N].d)
          {
                    puts("YES");
                    return;
          }
     puts("NO");
     //puts("YES");
     /*for (i = 1; i <= N; i ++)
      {
            for (j = 0; j < i; j ++)
                if (a[j].d + a[j].l >= a[i].d && a[j].d + a[j].)
      }*/
 }
 
int main()
 {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &cases);
    for (cas = 1; cas <= cases; cas ++)
     {
        init();
        work();
     }
    return 0;
 }
