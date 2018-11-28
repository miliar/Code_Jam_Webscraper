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

typedef struct {
   bool orange;
   int location;
} move;

int sign( int num ) {
   if( num > 0 )
      return 1;
   if( num < 0 )
      return -1;
   return 0;
}

int main() {
	ofstream fout ( "large-input.out" );
	ifstream fin ( "large-input.in" );

	assert( fout != NULL );
	assert( fin != NULL );

   int numCases;
   fin >> numCases;

   int orangeLoc = 0;
   int blueLoc = 0;

   for( int i = 0; i < numCases; i++ )
   {
      int numButtons;
      fin >> numButtons;

      move moves[numButtons + 5];

      int orangeMoves[numButtons + 5];
      int numOrangeMoves = 0;

      int blueMoves[numButtons + 5];
      int numBlueMoves = 0;

      for( int j = 0; j < numButtons; j++ )
      {
         char type;
         int location;

         fin >> type >> location;

         if( type == 'O' )
         {
            orangeMoves[numOrangeMoves] = location;
            numOrangeMoves++;

            moves[j].orange = true;
         }
         else
         {
            blueMoves[numBlueMoves] = location;
            numBlueMoves++;

            moves[j].orange = false;
         }

         moves[j].location = location;
      }

      int orangeIndex = 0;
      int blueIndex = 0;

      int orangeLocation = 1;
      int blueLocation = 1;

      int seconds = 0;
      for( int j = 0; j < numButtons; j++ )
      {
         move next = moves[j];
         
         if( next.orange )
         {
            // add one for pushing the button
            int time = abs( next.location - orangeLocation ) + 1;

            if( blueIndex < numBlueMoves )
            {
               int nextBlueLocation = blueMoves[blueIndex];

               int distance = abs( nextBlueLocation - blueLocation );
               int direction = sign( nextBlueLocation - blueLocation );

               if( distance != 0 )
               {
                  if( distance < time )
                     blueLocation = nextBlueLocation;
                  else
                     blueLocation += time * direction;
               }
            }

            orangeLocation = next.location;
            seconds += time;
            orangeIndex++;
         }
         else
         {
            // add one for pushing the button
            int time = abs( next.location - blueLocation ) + 1;

            if( orangeIndex < numOrangeMoves )
            {
               int nextOrangeLocation = orangeMoves[orangeIndex];

               int distance = abs( nextOrangeLocation - orangeLocation );
               int direction = sign( nextOrangeLocation - orangeLocation );

               if( distance != 0 )
               {
                  if( distance < time )
                     orangeLocation = nextOrangeLocation;
                  else
                     orangeLocation += time * direction;
               }
            }

            blueLocation = next.location;
            seconds += time;
            blueIndex++;
         }
         
#if DEBUG
         cout << "Seconds for case #" << i + 1 << ": " << seconds << '\n';
#endif
      }

      fout << "Case #" << i + 1 << ": " << seconds << '\n';
   }
	
	return 0;
}

