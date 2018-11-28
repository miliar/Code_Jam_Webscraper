#include<iostream>
#include<cstdio>
using namespace std;

#define MAXN 1001

struct Tedge
{
   long value;
   int next;
}g[MAXN];

int main()
{
   freopen("C-small.in", "r", stdin);
   freopen("C-small.out", "w", stdout);
   long R, K, ans;
   int T, N;
   int j, i;
   scanf("%d", &T);
   for (j = 1; j <= T; j++)
   {
      scanf("%ld%ld%d", &R, &K, &N);
	  long max = 0;
	  for (i = 1; i <= N; i++)
      {
         scanf("%ld", &g[i].value);
		 max += g[i].value;
         g[i].next = i + 1;
      }
	  g[N].next = 1;
	  if (max <= K) ans = max * R;
	  else 
	  {
          ans = 0;
          int pre = 1;
          while (R--)
		  {
			  long sum = K;
              while (g[pre].value <= sum)
			  {
				  ans += g[pre].value;
                  sum -= g[pre].value;
                  pre = g[pre].next;
			  }
		  }
	  }
      printf("Case #%d: %ld\n", j, ans);
   }
   return 0;
}