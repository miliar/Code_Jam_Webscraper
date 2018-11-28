// CodeJam-20090913-1.cpp : Defines the entry point for the console application.
//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <map>
using namespace std;

int main(int argc, char *argv[])
{
   FILE
      *fpi = fopen("A-small.in", "r"),
      *fpo = fopen("A-small.out", "w");

   int
      T,
      nMinBase,
      nCurrVal;

   __int64
      nMinSec;

   char
      szLine[80],
      *pCurr;

   fscanf(fpi, "%d", &T);

   for (int i = 0; i < T; i++)
   {
      map<char, int>
         mapSymbolPositions,
         mapSymbolValues;

      fscanf(fpi, "%s", szLine);

      pCurr = szLine;
      while (*pCurr)
      {
         if (mapSymbolPositions.find(*pCurr) == mapSymbolPositions.end())
            mapSymbolPositions[*pCurr] = pCurr - szLine;

         pCurr++;
      }

      nMinBase = mapSymbolPositions.size();
      if (nMinBase == 1)
         nMinBase = 2;

      mapSymbolValues[*szLine] = 1;

      nCurrVal = 0;
      for (int j = 1, len = strlen(szLine); j < len; j++)
      {
         for (map<char, int>::const_iterator iter = mapSymbolPositions.begin(); iter != mapSymbolPositions.end(); iter++)
            if (iter->second == j)
            {
               mapSymbolValues[iter->first] = nCurrVal;
               nCurrVal = nCurrVal ? nCurrVal + 1 : 2;
               break;
            }
      }

      nMinSec = 0;
      pCurr = szLine;
      while (*pCurr)
      {
         nMinSec *= nMinBase;

         map<char, int>::const_iterator
            iter = mapSymbolValues.find(*pCurr);

         nMinSec += iter->second;
         pCurr++;
      }

      fprintf(fpo, "Case #%d: %d\n", i + 1, nMinSec);
   }

	return 0;
}
