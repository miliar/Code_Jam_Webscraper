#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int getNumOfDig(int value)
{
   int nrDig = 0;
   do
   {
      ++nrDig;
      value /= 10;
   } 
   while (value != 0);

   return nrDig;
}

int count(int n, int m, int nrDig)
{
   int sum = 0, a = 0, b = 0;
   while (n < m)
   {
      for (int i = 1; i < nrDig; ++i)
      {
         a = (int)pow(10.0, i);
         b = (int)pow(10.0, nrDig-i);
         if ((((n%a)*b)+(n/a)) == m)
         {
            sum++;
         }
      }

      n++;
   }

   return sum;
}

int calcPairs(int n, int m)
{
   int nrDig = getNumOfDig(n);
   int sum = 0;
   do
   {
      sum += count(n, m, nrDig);
      --m;
   }
   while (n < m);

   return sum;
}

int main(int, char**)
{
   FILE* pInput;
   fopen_s(&pInput, "input.txt", "r");

   if (pInput != 0) {
      int t = 0;
      fscanf_s(pInput, "%d", &t);

      int i = 0;
      while (!feof(pInput) && i < t) {
         ++i;
         int n = 0, m = 0;
         fscanf_s(pInput, "%d %d", &n, &m);
         printf("Case #%d: %d\n", i, calcPairs(n, m));
      }
   }

   getchar();

   return 0;
}