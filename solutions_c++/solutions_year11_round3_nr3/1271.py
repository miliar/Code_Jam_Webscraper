#include <cstdio>
#include <vector>
#include <algorithm>
#define MaxN 1111111

using namespace std;

long long T;
int a[MaxN], n;
long long freq[MaxN];
int H, L;

long long gcd(long long a, long long b){
   if (b == 0)
      return a;
   if (a == 0)
      return b;
   return gcd(b, a % b);
}

bool isGood(int x)
{
   for (int i=0; i<n; i++)
      if (x && freq[i] && freq[i] % x && x % freq[i])
         return false;
   return true;
}

void solve()
{
   scanf("%d %d %d", &n, &H, &L);
   for (int i=0; i<n; i++)
      scanf("%I64d", freq + i);
   long long pos = freq[0];
   for (int i=H; i<=L; i++)
      if (isGood(i)){
         printf("%d\n", i);
         return;
      }
   printf("NO\n");
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