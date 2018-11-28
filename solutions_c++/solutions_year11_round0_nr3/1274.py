#include <cstdio>
#include <algorithm>

using namespace std;

void solve()
{
   int minVal = 1<<30, sumTotal = 0, xor = 0, n, x;
   scanf("%d", &n);
   for (int i=0; i<n; i++){
      scanf("%d", &x);
      xor ^= x;
      if (x < minVal)
         minVal = x;
      sumTotal += x;
   }
   if (xor){
      printf("NO\n");
   }  else  {
      printf("%d\n", sumTotal - minVal);
   }
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int tst;
   scanf("%d", &tst);
   for (int iter = 1; iter <= tst; iter++){
      printf("Case #%d: ", iter);
      solve();
   }
   return 0;
}