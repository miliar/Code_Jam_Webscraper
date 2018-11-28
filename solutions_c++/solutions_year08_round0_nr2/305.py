//code for Saving the Universe problem
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

struct STrain
{
   long     m_nStartTime;
   long     m_nEndTime;
   bool     m_bToStationB;
   bool     m_bUsed;

   STrain(long A_nStartTime, long A_nEndTime, bool A_bToStationB)
   {
      m_nStartTime = A_nStartTime;
      m_nEndTime = A_nEndTime;
      m_bToStationB = A_bToStationB;
      m_bUsed = false;
   };
};

bool TrainSort(STrain elem1, STrain elem2)
{
   return elem1.m_nStartTime < elem2.m_nStartTime;
}

void MakeCase(FILE *A_file, long &A_nAStratTrain, long &A_nBStratTrain)
{
   if(!A_file)
      return;
   vector<STrain>    vecTrains;

   long              nTimeDelay           = 0;
   long              nTrainsFromA         = 0;
   long              nTrainsFromB         = 0;
   long              nQueryNumber         = 0;
   long              nStartTime           = 0;
   long              nEndTime             = 0;
   long              nCurrentTime         = 0;
   long              nToManagedTrains     = 0;
   long              ind                  = 0;
   bool              bToStationB          = false;//where should go the train we look for
   char              chEL;
   char              chH1;
   char              chH2;
   char              chM1;
   char              chM2;

   fscanf(A_file, "%ld%c", &nTimeDelay, &chEL);
   fscanf(A_file, "%ld%ld%c", &nTrainsFromA, &nTrainsFromB, &chEL);
   for(ind = 0; ind < nTrainsFromA; ++ind)
   {
      fscanf(A_file, "%c%c%c%c%c%c", &chH1, &chH2, &chEL, &chM1, &chM2, &chEL);
      nStartTime = ((long)(chH1 - '0') * 10 + (long)(chH2 - '0')) * 60 + (long)(chM1 - '0') * 10 + (long)(chM2 - '0');
      fscanf(A_file, "%c%c%c%c%c%c", &chH1, &chH2, &chEL, &chM1, &chM2, &chEL);
      nEndTime = ((long)(chH1 - '0') * 10 + (long)(chH2 - '0')) * 60 + (long)(chM1 - '0') * 10 + (long)(chM2 - '0');
      STrain      train(nStartTime, nEndTime, true);
      vecTrains.push_back(train);
   }

   for(ind = 0; ind < nTrainsFromB; ++ind)
   {
      fscanf(A_file, "%c%c%c%c%c%c", &chH1, &chH2, &chEL, &chM1, &chM2, &chEL);
      nStartTime = ((long)(chH1 - '0') * 10 + (long)(chH2 - '0')) * 60 + (long)(chM1 - '0') * 10 + (long)(chM2 - '0');
      fscanf(A_file, "%c%c%c%c%c%c", &chH1, &chH2, &chEL, &chM1, &chM2, &chEL);
      nEndTime = ((long)(chH1 - '0') * 10 + (long)(chH2 - '0')) * 60 + (long)(chM1 - '0') * 10 + (long)(chM2 - '0');
      STrain      train(nStartTime, nEndTime, false);
      vecTrains.push_back(train);
   }

   A_nAStratTrain = 0;
   A_nBStratTrain = 0;

   sort(vecTrains.begin(), vecTrains.end(), TrainSort);

   nToManagedTrains = nTrainsFromA + nTrainsFromB;
   while(nToManagedTrains)
   {
      ind = 0;
      //search for first free train
      while(vecTrains[ind].m_bUsed)
         ++ind;
      if(vecTrains[ind].m_bToStationB)
         ++A_nAStratTrain;
      else
         ++A_nBStratTrain;
      bToStationB = !vecTrains[ind].m_bToStationB;//next should go oposite
      nCurrentTime = vecTrains[ind].m_nEndTime + nTimeDelay;
      vecTrains[ind].m_bUsed = true;
      --nToManagedTrains;
      ++ind;
      for(; ind < nTrainsFromA + nTrainsFromB; ++ind)
      {
         if(!vecTrains[ind].m_bUsed && vecTrains[ind].m_bToStationB == bToStationB && vecTrains[ind].m_nStartTime >= nCurrentTime)
         {
            bToStationB = !bToStationB;
            nCurrentTime = vecTrains[ind].m_nEndTime + nTimeDelay;
            vecTrains[ind].m_bUsed = true;
            --nToManagedTrains;
         }
      }
   }
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
      MakeCase(fileInput, nAStratTrain, nBStratTrain);
      fprintf(fileOutput, "Case #%ld: %ld %ld\n", nCurrentCase, nAStratTrain, nBStratTrain);
   }
   fclose(fileInput);
   fclose(fileOutput);
   return 0;
}