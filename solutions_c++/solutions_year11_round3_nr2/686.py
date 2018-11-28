#include <cstdio>
#include <algorithm>
#include <iostream>
#define MAX_D 20010
using namespace std;

long long R[1000000];

void solve()
{
     long long L, t, N, C;
     scanf("%I64d%I64d%I64d%I64d", &L, &t, &N, &C);
     
     long long sum = 0;
     for (int i = 0; i < C; i++)
     {
         int a;
         scanf("%d", &a);
         for (int j = i; j < N; j += C)
         {
             sum += R[j] = a*2;
         }
     }
     
     if (L == 0) { cout << sum << endl; return; }
     
     int minTime = 1000000000;
     for (int i = 0; i < N; i++)
      for (int j = i; j < N; j++)
      {
          int time = 0;
          for (int k = 0; k < N; k++)
          {
             if (((k == i || k == j) && L == 2) || (k == i && L == 1))
             {
                   if (time >= t)
                   {        
                        time += R[k]/2;
                   }
                   else if (t - time < R[k])
                   {        
                        int t2 = t - time;
                        //cout << t2 << endl;
                        time += t2 + (R[k]-t2)/2;
                   }
                   else
                   {
                       time += R[k];
                   }
             }
             else 
             {
                  time += R[k];
             } 
          }
          minTime = min(time, minTime);
      }
     printf("%d\n", minTime);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i+1);
        solve();
    }
}
