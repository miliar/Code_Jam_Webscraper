/*
  TYTUŁ ZADANIA
  Author: Piotr Różański
  Compiler: GCC g++
*/

#include <cstdio>

int M[11][1024];

int min(int a, int b)
{
  return (a<b) ? a : b;
}

int wyznacz(int k, int i)
{
  if (M[k][i] >= k) return 0;
  if (k==1) return 1;
  return wyznacz(k-1,2*i) + wyznacz(k-1,2*i+1) + 1;
}

int main()
{
  unsigned testy;
  scanf("%u",&testy);
  for (unsigned test=1; test<=testy; ++test)
  {
    int P;
    scanf("%d",&P);
    const int N0 = 1<<P;
    int N = N0;
    for (int i=0; i<N; ++i)
    {
      scanf("%d",M[0]+i);
    }

    char bufor[1000000];
    for (int i=0; i<=P; ++i) fgets(bufor, sizeof bufor, stdin);
    
    for (int k=1; k<=P; ++k)
    {
      N /= 2;
      for (int i=0; i<N; ++i)
      {
        M[k][i] = min(M[k-1][2*i],M[k-1][2*i+1]);
      }
    }
    printf("Case #%u: %d\n",test,wyznacz(P,0));
  }
}
