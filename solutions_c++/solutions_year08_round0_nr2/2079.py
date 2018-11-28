// 
// File:  train.cc
// Author: Luis Carlos de Miranda Santos Junior
//
// Created on 17 de Julho de 2008, 13:27
//

#include <stdlib.h>
#include <stdio.h>
#include <set.h>
using namespace std;
typedef struct TTime_tag{
   int iHour, iMinute, iStatus;
} TTime;

struct ltTime
{
   bool operator()(const TTime st1, const TTime st2) const
   {
      if( st1.iHour == st2.iHour )
      {
         if( st1.iMinute == st2.iMinute )
            return st1.iStatus > st2.iStatus;
         else
            return st1.iMinute < st2.iMinute;
      }
      else         
         return st1.iHour < st2.iHour;
   }
};

typedef multiset<TTime, ltTime> TTimeList;

TTime sumT( TTime st, int iT )
{
   st.iMinute = st.iMinute + iT;
   if( st.iMinute >= 60 )
   {
      st.iHour++;
      st.iMinute = st.iMinute - 60;
   }
   return(st);
}

int getTrains( TTimeList* timeList )
{
   TTimeList::iterator it;
   int nMax = 0;
   int nTrains = 0;
   
   for( it = timeList->begin(); it != timeList->end(); it++ )
   {
      if( it->iStatus == 0 )
      {
         nTrains++;
         if( nTrains > nMax )
         {
            nMax = nTrains;
         }
      }
      else if( it->iStatus == 1 )
      {
         nTrains--;        
      }        
    printf("it %2d:%2d   status:%d\n", it->iHour, it->iMinute, it->iStatus);

   }
   if( nMax > 0 )
      return nMax;
   else
      return 0;
   
}

int main(int argc, char** argv)
{
   FILE* pFileIn;
   FILE* pFileOut;
   int iT, iA, iB, nA, nB;
//   int iHour, iMinute;
   int iCase, nCase;
   TTime stD, stA;
   TTimeList listA, listB;
           
   pFileIn = fopen("B-large.in","r+");
   pFileOut = fopen("B-large.out","w+");
   
   fscanf( pFileIn, "%d\n", &iCase );
   
   stD.iStatus = 0;
   stA.iStatus = 1;
           
   for( nCase = 0; nCase < iCase; nCase++ )
   {
      printf("--> for case\n");
      fflush(stdout);
      fscanf( pFileIn, "%d\n", &iT );
      fscanf( pFileIn, "%d %d\n", &iA, &iB );
      listA.clear();
      listB.clear();
      
      for( nA= 0; nA< iA; nA++ )
      {
      printf("--> for nA\n");
      fflush(stdout);
         fscanf( pFileIn, "%d:%d %d:%d\n", &stD.iHour, &stD.iMinute,
                                           &stA.iHour, &stA.iMinute );
         stA = sumT( stA, iT );
//         printf("A: %d:%d   %d:%d\n", stD.iHour, stD.iMinute,
  //                                         stA.iHour, stA.iMinute );
         listA.insert( stD );
         listB.insert( stA );
      }
         
      for( nB= 0; nB< iB; nB++ )
      {
         fscanf( pFileIn, "%d:%d %d:%d\n", &stD.iHour, &stD.iMinute,
                                           &stA.iHour, &stA.iMinute );
         stA = sumT( stA, iT );
//         printf("b: %d:%d   %d:%d\n", stD.iHour, stD.iMinute,
  //                                         stA.iHour, stA.iMinute );
         listB.insert( stD );
         listA.insert( stA );
      }
//-----------------------process
      printf("list A\n");
      nA = getTrains( &listA );
      printf("list B\n");
      nB = getTrains( &listB );
      fprintf( pFileOut, "Case #%d: %d %d\n", nCase+1, nA, nB );
   }
   fclose( pFileIn );
   fclose( pFileOut );
    return (EXIT_SUCCESS);
}

