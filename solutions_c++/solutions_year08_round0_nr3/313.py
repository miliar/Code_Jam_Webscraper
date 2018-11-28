//code for Saving the Universe problem
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

#define PI 3.14159265

double CalculateArcArea(double A_nX1, double A_nY1, double A_nX2, double A_nY2, double A_nR)//(X1, Y1) is  Top Left and (X2, Y2) is Left Bottom
{
   double         nHalfTriangelBase = 0;
   double         nTriangelHight    = 0;
   double         nTriangleArea     = 0;
   double         nArcArea          = 0;
   double         nArc              = 0;

   nHalfTriangelBase = sqrt((A_nX1 - A_nX2) * (A_nX1 - A_nX2) + (A_nY1 - A_nY2) * (A_nY1 - A_nY2)) / 2;
   nTriangelHight = sqrt(A_nR * A_nR + nHalfTriangelBase * nHalfTriangelBase);

   nTriangleArea = nHalfTriangelBase * nTriangelHight;

   nArcArea = asin(nHalfTriangelBase / A_nR) * A_nR * A_nR;

   return nTriangleArea - nArcArea;
}

double MakeCase(FILE *A_file)
{
   if(!A_file)
      return 0;
   //double X2 = 0; means that X2 = X * X
   double            nFlyR                = 0;
   double            nRacquetR            = 0;
   double            nRacquetT            = 0;
   double            nStringR             = 0;
   double            nStringSpace         = 0;
   double            nEndTime             = 0;
   double            nMissSpace           = 0;
   double            nStringHitR          = 0;
   double            nPracticeR           = 0;
   double            nFullMissArea        = 0;
   double            nFullMissSize        = 0;
   double            nPracticeR2          = 0;
   double            nPossibleSpaceInTheLine = 0;
   double            nPossibleSpaceInTheTopLine = 0;
   double            nCurrentHigh         = 0;
   double            nProbablity          = 1;
   double            nEdgeArea            = 0;
   double            nTotalEdgeArea       = 0;
   double            nLeftEdgePos         = 0;
   double            nRightEdgeHigh       = 0;
   double            nLeftEdgeHigh        = 0;
   long              nNumFullMissArea      = 0;

   fscanf(A_file, "%lf%lf%lf%lf%lf", &nFlyR, &nRacquetR, &nRacquetT, &nStringR, &nStringSpace);

   nMissSpace = nStringSpace - (2 * nFlyR);
   if(nMissSpace <= 0)
      return 1;

   nPracticeR = nRacquetR - nRacquetT;
   nStringHitR = nStringR + nFlyR;
   nFullMissArea = nMissSpace * nMissSpace;

   nFullMissSize = 2 * nStringHitR + nMissSpace;
   nPracticeR2 = nPracticeR * nPracticeR;

   nCurrentHigh = nStringHitR;
   while(nCurrentHigh < nPracticeR)
   {
      nPossibleSpaceInTheLine = sqrt(nPracticeR2 - nCurrentHigh * nCurrentHigh);
      nLeftEdgePos = 0;
      while(nLeftEdgePos + nFullMissSize <= nPossibleSpaceInTheLine)
      {
         nLeftEdgePos += nFullMissSize;
         ++nNumFullMissArea;
      }
      nLeftEdgePos += nStringHitR;
      if(nLeftEdgePos < nPossibleSpaceInTheLine)
      {
         nPossibleSpaceInTheTopLine = sqrt(nPracticeR2 - (nCurrentHigh + nMissSpace) * (nCurrentHigh + nMissSpace));
         if(nLeftEdgePos + nMissSpace <= nPossibleSpaceInTheLine)//|_|
         {
            if(nLeftEdgePos + nMissSpace <= nPossibleSpaceInTheTopLine)//full square case
               ++nNumFullMissArea;
            else
            {
               nRightEdgeHigh = sqrt(nPracticeR2 - (nLeftEdgePos + nMissSpace) * (nLeftEdgePos + nMissSpace)) - nCurrentHigh;
               if(nLeftEdgePos <= nPossibleSpaceInTheTopLine)//|_| and something on the top     A
               {
                  nEdgeArea += nRightEdgeHigh * nMissSpace;
                  nEdgeArea += (nMissSpace - nRightEdgeHigh) * (nMissSpace + nPossibleSpaceInTheTopLine - nLeftEdgePos) / 2;
                  nEdgeArea += CalculateArcArea(nPossibleSpaceInTheTopLine, nCurrentHigh + nMissSpace, nLeftEdgePos + nMissSpace, nCurrentHigh + nRightEdgeHigh, nPracticeR);
               }
               else//only |_| B
               {
                  nLeftEdgeHigh = sqrt(nPracticeR2 - nLeftEdgePos * nLeftEdgePos) - nCurrentHigh;
                  nEdgeArea += nMissSpace * (nLeftEdgeHigh + nRightEdgeHigh) / 2;
                  nEdgeArea += CalculateArcArea(nLeftEdgePos, nCurrentHigh + nLeftEdgeHigh, nLeftEdgePos + nMissSpace, nCurrentHigh + nRightEdgeHigh, nPracticeR);
               }
            }
         }
         else//|_
         {
            if(nLeftEdgePos <= nPossibleSpaceInTheTopLine)//|_ and something on the top     C
            {
               nEdgeArea += nMissSpace * (nPossibleSpaceInTheLine - nLeftEdgePos + nPossibleSpaceInTheTopLine - nLeftEdgePos) / 2;
               nEdgeArea += CalculateArcArea(nPossibleSpaceInTheTopLine, nCurrentHigh + nMissSpace, nPossibleSpaceInTheLine, nCurrentHigh, nPracticeR);
            }
            else//only |_ D
            {
               nLeftEdgeHigh = sqrt(nPracticeR2 - nLeftEdgePos * nLeftEdgePos) - nCurrentHigh;
               nEdgeArea += nLeftEdgeHigh * (nPossibleSpaceInTheLine - nLeftEdgeHigh) / 2;
               nEdgeArea += CalculateArcArea(nLeftEdgePos, nCurrentHigh + nLeftEdgeHigh, nPossibleSpaceInTheLine, nCurrentHigh, nPracticeR);
            }
         }
      }
      nCurrentHigh += nFullMissSize;
   }

   nProbablity -= (nEdgeArea + nNumFullMissArea * nFullMissArea) * 4 / (PI * nRacquetR * nRacquetR);

   return nProbablity;
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
      fprintf(fileOutput, "Case #%ld: %f\n", nCurrentCase, MakeCase(fileInput));
   }
   fclose(fileInput);
   fclose(fileOutput);
   return 0;
}