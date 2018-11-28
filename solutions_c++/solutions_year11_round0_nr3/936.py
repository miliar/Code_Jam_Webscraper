#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int inline patrickAdd(int val1, int val2)
{
   return val1 + val2 - 2 * (val1 & val2);
}

void solveCandySplitting(int testCaseNumber)
{
   int n;
   scanf("%d", &n);

   vector<int> values(n);
   for(int i = 0; i < n; i++)
   {
      int value;
      scanf("%d", &value);
      values[i] = value;
   }

   int maxValue = -1;
   for(int w = n-1; w > 0; w--)
   {
      for(int i = 0; i <= n-w; i++)
      {
         int patrickValue1 = 0, patrickValue2 = 0;
         int actualValue1 = 0, actualValue2 = 0;
         for(int j = 0; j < n; j++)
         {
            if(i <= j && j < i + w)
            {
               patrickValue1 = patrickAdd(patrickValue1, values[j]);
               actualValue1 += values[j];
            }
            else
            {
               patrickValue2 = patrickAdd(patrickValue2, values[j]);
               actualValue2 += values[j];
            }
         }
         if(patrickValue1 == patrickValue2)
         {
            if(actualValue1 > maxValue)
            {
               maxValue = actualValue1;
            }
            if(actualValue2 > maxValue)
            {
               maxValue = actualValue2;
            }
         }
      }
   }

   printf("Case #%d: ", testCaseNumber + 1);
   if(maxValue == -1)
   {
      printf("NO\n");
   }
   else
   {
      printf("%d\n", maxValue);
   }
}

int main(int argc, char** argv)
{
   int noOfTestCases = 0;
   scanf("%d", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solveCandySplitting(i);
   }
   return 0;
}