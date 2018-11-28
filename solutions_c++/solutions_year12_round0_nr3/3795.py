#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

int rep[2000001];
int n, a, b;

int getrep(int n)
{
  int res = n;
  int next = n;
  int base = 1;
  
  while (base * 10 <= n) base *= 10;
  do
  {
    int nextt = (next / 10) + base * (next % 10);
    if (next % 10) res = min(res, nextt);
    next = nextt;
  }
  while (next != n);

  return res;
}

long long solve(int a, int b)
{
  long long res = 0;
  map<int, int> m;

  for (int i = a; i <= b; i++)
    m[rep[i]]++;
  for (map<int, int>::iterator i = m.begin(); i != m.end(); i++)
    res += (long long)i->second * (i->second - 1) / 2;
  return res;
}

int main()
{
  for (int i = 0; i <= 2000000; i++)
    rep[i] = getrep(i);

  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {   
    scanf("%d %d", &a, &b);
    printf("Case #%d: %lld\n", i + 1, solve(a, b));
  }

  return 0;
}
