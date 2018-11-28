//code for Saving the Universe problem
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;


bool UDgreater(long elem1, long elem2)
{
   return elem1 > elem2;
}


long MakeCase(FILE *A_file)
{
   if(!A_file)
      return 0;

   long           nNumber  = 0;
   long           nInd     = 0;
   long           nResult  = 0;
   long           nTmp     = 0;
   vector<long>   vecX;
   vector<long>   vecY;

   fscanf(A_file, "%ld", &nNumber);

   for(nInd = 0; nInd < nNumber; ++nInd)
   {
      fscanf(A_file, "%ld", &nTmp);
      vecX.push_back(nTmp);
   }

   for(nInd = 0; nInd < nNumber; ++nInd)
   {
      fscanf(A_file, "%ld", &nTmp);
      vecY.push_back(nTmp);
   }

   sort(vecX.begin(), vecX.end());
   sort(vecY.begin( ), vecY.end( ), greater<long>());

   for(nInd = 0; nInd < nNumber; ++nInd)
      nResult += vecX[nInd] * vecY[nInd];

   return nResult;
};

int main()
{
   long              nCases            = 0;
   long              nCurrentCase      = 0;
   long              nAStratTrain      = 0;
   long              nBStratTrain      = 0;
   FILE             *fileInput         = NULL;
   FILE             *fileOutput        = NULL;

   fileInput = fopen("input.txt", "r");
   if(!fileInput)
      return -1;

   fileOutput = fopen("output.txt", "w");
   if(!fileInput)
      return -1;

   fscanf(fileInput, "%ld", &nCases);
   for(nCurrentCase = 1; nCurrentCase <= nCases; ++nCurrentCase)
   {
      fprintf(fileOutput, "Case #%ld: %ld\n", nCurrentCase, MakeCase(fileInput));
   }
   fclose(fileInput);
   fclose(fileOutput);
   return 0;
}