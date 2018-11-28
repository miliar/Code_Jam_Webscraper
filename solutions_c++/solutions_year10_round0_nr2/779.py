#include <stdio.h>
#include <stdlib.h>

long long unsigned int mdc(long long unsigned int a, long long unsigned int b)
{
   if (b == 0) return a;
   return mdc(b, a % b);
}

int main()
{
  long long unsigned int event[3], MDC, min[3], LCM, mult, aux;
  int num, N, c = 0;
  scanf ("%d", &num);
  while (num)
  {	
      c++;
      num--;
      scanf("%d", &N);
      for (int i = 0; i < N; i++)
      {
	  scanf("%llu", &event[i]);
      }
      min[0] = abs(event[0] - event[1]);
      if (N == 3)
      {
	min[1] = abs(event[0] - event[2]);
	min[2] = abs(event[1] - event[2]);
	aux = mdc(min[0], mdc(min[1], min[2]));	
      }
      else
      {
	aux = min[0];
      }
      if (aux > 1 && event[0]%aux)
	printf("Case #%d: %llu\n", c, (aux - event[0]%aux));
      else
	printf("Case #%d: 0\n", c);
  }
  return 0;
}