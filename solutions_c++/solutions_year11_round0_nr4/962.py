#include<stdio.h>

int tab[1010];
int visited[1010];

int main()
{
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
    int n;
    scanf("%d", &n);
    for(int j = 1; j <= n; j++)
      scanf("%d", &tab[j]);
    
    int sum = 0;
    for(int j = 1; j <= n; j++)
    {
      if(visited[j] == i || tab[j] == j)
        continue;
        
      visited[j] = i;
      int l = 1;
      int tmp = tab[j];
      while(tmp != j)
      {
        visited[tmp] = i;
        tmp = tab[tmp];
        l++;
      }
      sum += l;
    }

    printf("Case #%d: %d\n", i, sum);
  }
}
