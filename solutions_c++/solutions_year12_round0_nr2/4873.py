#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

void getScores(int ti, int &highestScoreIfNormal, int &highestScoreIfSurprising)
{
   int avg = ti / 3;

   if(ti % 3 == 0)
   {
      highestScoreIfNormal = avg;
      highestScoreIfSurprising = avg + 1;
   }
   else if(ti % 3 == 1)
   {
      highestScoreIfNormal = avg + 1;
      highestScoreIfSurprising = avg + 1;
   }
   else if(ti % 3 == 2)
   {
      highestScoreIfNormal = avg + 1;
      highestScoreIfSurprising = avg + 2;
   }

   if(highestScoreIfSurprising > ti)
   {
      highestScoreIfSurprising = ti;
   }

   if(highestScoreIfNormal > 10)
   {
      highestScoreIfNormal = 10;
   }
   if(highestScoreIfSurprising > 10)
   {
      highestScoreIfSurprising = 10;
   }
}

void solve(int testCaseNumber)
{
   int n;
   scanf("%d ", &n);
   int s;
   scanf("%d ", &s);
   int p;
   scanf("%d ", &p);
   int y = 0;

   for(int i = 0, ti; i < n; i++)
   {
      scanf("%d", &ti);

      int highestScoreIfNormal, highestScoreIfSurprising;
      getScores(ti, highestScoreIfNormal, highestScoreIfSurprising);

      if(highestScoreIfNormal >= p)
      {
         y++;
      }
      else if(s > 0 && highestScoreIfSurprising >= p)
      {
         y++;
         s--;
      }
   }

   printf("Case #%d: %d\n", testCaseNumber + 1, y);
}

int main(int argc, char** argv)
{
   int noOfTestCases = 0;
   scanf("%d\n", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solve(i);
   }
   return 0;
}