#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

inline int htn(int h, int m)
{
  return 60*h+m;
}

int v[2][5000];

int main()
{
  int n;
  scanf(" %d", &n);
  for(int test=1; test<=n; ++test)
    {
      memset(v, 0, sizeof(v));
      int t, na, nb;
      scanf(" %d %d %d", &t, &na, &nb);
      for(int i=0; i<na; ++i)
	{
	  int h1, m1, h2, m2;
	  scanf(" %d:%d %d:%d", &h1, &m1, &h2, &m2);
	  v[0][htn(h1, m1)]--;
	  v[1][htn(h2, m2)+t]++;
	}
      for(int i=0; i<nb; ++i)
	{
	  int h1, m1, h2, m2;
	  scanf(" %d:%d %d:%d", &h1, &m1, &h2, &m2);
	  v[1][htn(h1,m1)]--;
	  v[0][htn(h2,m2)+t]++;
	}
      int mina=0x7fffffff, minb=0x7fffffff;
      for(int i=1; i<5000; ++i)
	{
	  v[0][i] += v[0][i-1];
	  v[1][i] += v[1][i-1];
	}
      for(int i=0; i<5000; ++i)
	{
	  mina = min(v[0][i], mina);
	  minb = min(v[1][i], minb);
	}
      printf("Case #%d: %d %d\n", test, -mina, -minb);
    }
  return 0;
}
