#include <cstdio>
#include <queue>

#define mlen 1000
#define ll long long

ll a[mlen];
bool was[mlen];

int main()
{
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int j = 0; j < t; j++)
  {
   int r,k,n;
   scanf("%d%d%d", &r, &k, &n);
   for (int i = 0; i < n; i++) was[i] = 0;
   std::queue<int> q;
   for (int i = 0; i < n; i++)
   {
      scanf("%lld", &a[i]);
      q.push(i);
   }
   int x = 0;
   ll sumX = 0;
   while (!was[q.front()])
   {
      was[q.front()] = 1;
      ll sum = 0;
      for (int i = 0; i < n && sum + a[q.front()] <= k; q.pop(), i++)
      {
         sum += a[q.front()];
	 q.push(q.front());
      }
      x++;
      sumX += sum;
   }
   int num = q.front();
   int y = 0;
   ll sumY = 0;
   do
   {
      ll sum = 0;
      for (int i = 0; i < n && sum + a[q.front()] <= k; q.pop(), i++)
      {
         sum += a[q.front()];
	 q.push(q.front());
      }
      y++;
      sumY += sum;
   }
   while (q.front() != num);
   x -= y;
   sumX -= sumY;
   ll ans = 0;
   ans += sumX;
   r -= x;
   int p = r / y, u = r % y;
   ans += sumY * p;
   for (int i = 0; i < u; i++)
   {
      ll sum = 0;
      for (int i = 0; i < n && sum + a[q.front()] <= k; q.pop(), i++)
      {
         sum += a[q.front()];
	 q.push(q.front());
      }
      ans += sum;
   }
   printf("Case #%d: %lld\n", j + 1, ans);
 }
   return 0;
}
