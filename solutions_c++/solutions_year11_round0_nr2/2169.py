#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <functional>

using namespace std;

#define DEBUG false

#if !DEBUG
   #define cout fout
#endif

struct Combination {
   char other;
   char result;

   Combination( char other, char result )
      : other(other)
      , result(result)
   {
      // nothing to do
   }
};

int main() {
	ofstream fout ( "large-input.out" );
	ifstream fin ( "large-input.in" );

	assert( fout != NULL );
	assert( fin != NULL );

   int numCases;
   fin >> numCases;

   for( int i = 0; i < numCases; i++ )
   {
      int numCombine, numOppose;
      fin >> numCombine;

      // size greater than highest value of a char
      #define SIZE 200
      vector<Combination> combinations[ SIZE ];

      for( int j = 0; j < numCombine; j++ )
      {
         char element, other;
         char result;

         fin >> element >> other;
         fin >> result;

         combinations[element].push_back( Combination( other, result ) );
         combinations[other].push_back( Combination( element, result ) );
      }

      fin >> numOppose;
      vector<char> oppositions[ SIZE ];

      for( int j = 0; j < numOppose; j++ )
      {
         char element, other;
         fin >> element >> other;

         oppositions[element].push_back( other );
         oppositions[other].push_back( element );
      }

      int numInvoke;
      fin >> numInvoke;

      vector<char> elementList;
      int elementLookup[ SIZE ]; // used for oppositions

      for( int j = 0; j < SIZE; j++ )
         elementLookup[j] = 0;

      for( int j = 0; j < numInvoke; j++ )
      {
         char element;
         fin >> element;

         bool invokedElement = false;
         if( elementList.size() > 0 )
         {
            char lastElement = elementList.back();
            vector<Combination> combinationList = combinations[ element ];

            for( unsigned int k = 0; k < combinationList.size(); k++ )
            {
               Combination combination = combinationList.at( k );

               if( combination.other == lastElement )
               {
                  elementList.pop_back();
                  elementList.push_back( combination.result );

                  elementLookup[ lastElement ]--;
                  elementLookup[ combination.result ]++;
                  
                  invokedElement = true;
                  break;
               }
            }
         }

         if( !invokedElement )
         {
            elementList.push_back( element );
            elementLookup[ element ]++;
         }

         // list of oppositions for the newly added element
         vector<char> oppositionList = oppositions[ elementList.back() ];

         for( unsigned int k = 0; k < oppositionList.size(); k++ )
         {
            char opposition = oppositionList.at( k );

            // if opposition is in the element list
            if( elementLookup[ opposition ] )
            {
               elementList.clear();

               for( int i = 0; i < SIZE; i++ )
                  elementLookup[i] = 0;
            }
         }

      }

      cout << "Case #" << i + 1 << ": [";

      // may not have elements remaining in the list
      if( elementList.size() > 0 )
      {
         for( unsigned int j = 0; j < elementList.size() - 1; j++ )
            cout << elementList.at( j ) << ", ";
         cout << elementList.back();
      }

      cout << "]\n";
   }
	
	return 0;
}

