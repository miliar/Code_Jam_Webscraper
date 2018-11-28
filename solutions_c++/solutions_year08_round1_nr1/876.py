// 
// File:   p1.cc
// Author: ladraozinho
//
// Created on 25 de Julho de 2008, 21:05
//

#include <stdlib.h>

//
// 
//
#include <stdlib.h>
#include <stdio.h>
#include <set.h>
using namespace std;

struct ltint
{
   bool operator()(const long st1, const long st2) const
   {
         return st1 < st2;
   }
};

struct mtint
{
   bool operator()(const long st1, const long st2) const
   {
         return st1 > st2;
   }
};

typedef multiset<long, ltint> TIntLT;
typedef multiset<long, mtint> TIntMT;



int main(int argc, char** argv)
{
   FILE* pFileIn;
   FILE* pFileOut;

   long iCase, nCase;
   long iElem, nElem;
   TIntLT listA;
   TIntMT listB;
   long v, vetorial;
   TIntLT::iterator itA;
   TIntMT::iterator itB;
   
   
   pFileIn = fopen("A-small.in","r+");
   pFileOut = fopen("A-small.out","w+");
   
   fscanf( pFileIn, "%d\n", &iCase );
   
           
   for( nCase = 0; nCase < iCase; nCase++ )
   {
      fflush(stdout);
      fscanf( pFileIn, "%d\n", &iElem );
      listA.clear();
      listB.clear();
      
      for( nElem = 0; nElem < iElem-1; nElem++ )
      {
         fscanf( pFileIn, "%d ", &v );
         listA.insert( v );
      }
      fscanf( pFileIn, "%d\n", &v );
      listA.insert( v );

      for( nElem = 0; nElem < iElem-1; nElem++ )
      {
         fscanf( pFileIn, "%d ", &v );
         listB.insert( v );
      }
      fscanf( pFileIn, "%d\n", &v );
      listB.insert( v );
      
//-----------------------process
      vetorial = 0;
      for( itA = listA.begin(), itB = listB.begin(); itA != listA.end(); itA++, itB++ )
      {
         vetorial = vetorial + ((*itA) * (*itB)); 
      }
      
      fprintf( pFileOut, "Case #%d: %d\n", nCase+1, vetorial );
   }
   fclose( pFileIn );
   fclose( pFileOut );
    return (EXIT_SUCCESS);
}
