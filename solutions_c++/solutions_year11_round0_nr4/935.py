#include <stdio.h>
#include <vector>

using namespace std;

void solveGoroSort(int testCaseNumber)
{
   int n;
   scanf("%d", &n);

   vector<int> numbers(n);
   vector<bool> marked(n);
   for(int i = 0; i < n; i++)
   {
      int x;
      scanf("%d", &x);
      numbers[i] = x;
      marked[i] = false;
   }

   float noOfHits = 0.0f;
   for(int i = 0; i < n; i++)
   {
      if(marked[i]) continue;

      marked[i] = true;
      if(numbers[i] == i + 1) continue;

      int groupCount = 1;
      int startingPosition = i;
      int nextPosition = numbers[i] - 1;

      while(startingPosition != nextPosition)
      {
         marked[nextPosition] = true;
         nextPosition = numbers[nextPosition] - 1;
         groupCount++;
      }

      noOfHits += groupCount;
   }

   printf("Case #%d: %.6f\n", testCaseNumber + 1, noOfHits);
}

int main(int argc, char** argv)
{
   int noOfTestCases = 0;
   scanf("%d", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solveGoroSort(i);
   }
   return 0;
}