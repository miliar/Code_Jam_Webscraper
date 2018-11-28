#include <cstdio>
#include <cstdlib>

int rdtsc()
{
  register int eax asm("eax");
  asm("rdtsc");
  return eax;
}

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

int main()
{
  int t = 100;
  int n = 500;
  printf("%d\n", t);
  forn (i, t)
  {
    printf("%d %d\n", n, rand() % 1000000000);
    forn (i, n - 1)
      printf("%d %d\n", i + 2, rand() % (i + 1) + 1);
  }
  return 0;
}
