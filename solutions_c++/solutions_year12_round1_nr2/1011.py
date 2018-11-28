#include <cstdio>
#include <algorithm>

using namespace std;

int p[10];

int N;
int a[10];
int b[10];

int d[59049];

int h(int l[10])
{
   int x = 0;
   for(int i=0; i<N; i++)
      x += p[i]*l[i];
   return x;
}

int f(int l[10])
{
   int s = 0;
   for(int i=0; i<N; i++)
      s += l[i];
   if(s == 2*N)
      return 0;
   int x = h(l);
   if(d[x] != -1)
      return d[x];
   d[x] = 1000000;
   for(int j=0; j<N; j++)
      if(l[j] < 1 && s >= a[j])
      {
	 l[j] = 1;
	 d[x] = min(d[x], f(l));
	 l[j] = 0;
      }
   for(int j=0; j<N; j++)
      if(l[j] < 2 && s >= b[j])
      {
	 int e = l[j];
	 l[j] = 2;
	 d[x] = min(d[x], f(l));
	 l[j] = e;
      }
   return ++d[x];
}

int main()
{
   for(int i=0, j=1; i<10; i++, j*=3)
      p[i] = j;
   int T;
   scanf("%d", &T);
   for(int i=1; i<=T; i++)
   {
      scanf("%d", &N);
      for(int j=0; j<N; j++)
	 scanf("%d %d", &a[j], &b[j]);
      for(int j=0; j<59049; j++)
	 d[j] = -1;
      int l[10];
      for(int j=0; j<N; j++)
	 l[j] = 0;
      int v = f(l);
      printf("Case #%d: ", i);
      if(v == 1000001)
	 printf("Too Bad\n");
      else
	 printf("%d\n", v);
   }
   return 0;
}