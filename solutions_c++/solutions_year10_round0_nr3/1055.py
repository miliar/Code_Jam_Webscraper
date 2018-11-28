#include <iostream>
#include <queue>

using namespace std;

int g[10];

int main()
{
  freopen("C-small-attempt0.in","r", stdin);
  freopen("out.txt", "w", stdout);

  int T;

  scanf("%d", &T);

  int R, K, N;

  for(int i = 1; i <= T; i++)
  {
      queue<int> q;
      queue<int> q1;
      scanf("%d %d %d",&R, &K, &N);
      for(int j = 0; j < N; j++)
      {
          scanf("%d",  &g[j]);
          q.push(j);
      }

      int money = 0;

      for(int t = 0; t < R; t++)
      {
         int K1 =  K;
         for(int k = q.front(); g[k] <= K1; k = q.front())
         {
             K1 -=  g[k];
             q.pop();
             q1.push(k);
             money += g[k];
             //printf("%d ", k+1);
             if(q.empty()) break;
         }
         while(!q1.empty())
         {
             q.push(q1.front());
             q1.pop();
         }
         //printf(":money=%d\n", money);
      }

      printf("Case #%d: %d\n", i, money);

  }
  return 0;
}
