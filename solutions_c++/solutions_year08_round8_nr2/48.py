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
  int t = 50;
  int n = 300;
  printf("%d\n", t);
  forn (i, t)
  {
    printf("%d\n", n);
    forn (i, n)
      printf("%d %d %d\n", rand() % 10, rand() % 11 * 1000 + 1, rand() % 11 * 1000);
  }
  return 0;
}
