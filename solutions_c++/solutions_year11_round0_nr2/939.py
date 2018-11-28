#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void solveMagicka(int testCaseNumber)
{
   int noOfPairs;
   scanf("%d", &noOfPairs);

   map<char, map<char, char>> pairs;
   for(int i = 0; i < noOfPairs; i++)
   {
      char base1, base2, combined;
      scanf(" %c", &base1);
      scanf("%c", &base2);
      scanf("%c", &combined);

      pairs[base1][base2] = combined;
      pairs[base2][base1] = combined;
   }

   int noOfOpposingPairs;
   scanf("%d", &noOfOpposingPairs);

   map<char, vector<char>> opposingPairs;
   for(int i = 0; i < noOfOpposingPairs; i++)
   {
      char base1, base2;
      scanf(" %c", &base1);
      scanf("%c", &base2);

      opposingPairs[base1].push_back(base2);
      opposingPairs[base2].push_back(base1);
   }

   int lengthOfString;
   scanf("%d ", &lengthOfString);

   vector<char> result;
   char prev = 0;

   for(int i = 0; i < lengthOfString; i++)
   {
      char ch;
      scanf("%c", &ch);

      if(pairs.find(ch) != pairs.end() && pairs[ch].find(prev) != pairs[ch].end())
      {
         result.pop_back();
         result.push_back(pairs[ch][prev]);
         prev = 0;
      }
      else
      {
         bool oppositeFound = false;
         if(opposingPairs.find(ch) != opposingPairs.end())
         {
            vector<char>& opposites = opposingPairs[ch];
            for(int j = 0; j < opposites.size(); j++)
            {
               if(find(result.begin(), result.end(), opposites[j]) != result.end())
               {
                  result.clear();
                  oppositeFound = true;
                  prev = 0;
                  break;
               }
            }
         }

         if(!oppositeFound)
         {
            result.push_back(ch);
            prev = ch;
         }
      }
   }

   printf("Case #%d: [", testCaseNumber + 1);
   for(int i = 0; i < result.size(); i++)
   {
      printf("%c", result[i]);
      if(i != result.size() - 1)
      {
         printf(", ");
      }
   }
   printf("]\n");
}

int main(int argc, char** argv)
{
   int noOfTestCases = 0;
   scanf("%d", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solveMagicka(i);
   }
   return 0;
}