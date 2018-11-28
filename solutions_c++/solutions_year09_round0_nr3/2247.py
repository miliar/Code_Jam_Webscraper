#include <iostream>
#include <cstring>
using namespace std;
char line[600]; char sub[]  = "welcome to code jam";
int T = 0; int L = 0;
int memo[510][20];
int solve(int m, int v)
{
  if(v >= T) return 1;  else if(m >= L) return 0;   else if(memo[m][v] >= 0) return memo[m][v];
  int ans = 0;  int ans1 = 0;
  for(int i = m; i < L; ++i)
    {
      if(line[i] == sub[v])
	{
	  ans1 = solve(i+1,v+1);	  if(ans1 >= 10000) ans1 %= 10000;
	  ans += ans1;	  if(ans >= 10000) ans %= 10000;
	}
    }
  memo[m][v] = ans;  return ans;
}
int main()
{
  int N;  scanf("%d",&N);  char c;  T = strlen(sub);
  for(int i = 0; i < N; ++i)
    {
      memset(memo, -1, 510*20*sizeof(int));      scanf("\n",&c);      scanf("%[a-z ]", line);
      L = strlen(line);
      int u = solve(0, 0);
      printf("Case #%d: ", i+1); 
      if(u < 1000) printf("0");      if(u < 100) printf("0");      if(u < 10) printf("0");
      printf("%d\n",u);
    }
}
