#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <stack>
#include <iterator>
#include <string>
#include <map>
#include <math.h>
using namespace std;

struct vec2i
{
   vec2i( int _x, int _y ) : x( _x ) , y( _y ) {}

   int x;
   int y;
};

int GCD(int x,int y)
{
if(y==0) // base case, the programs stops if y reaches 0.
return x; //it returns the GCD
else
return GCD(y,x%y); //if y doesn't reach 0 then recursion continues
}

struct SVine
{
   SVine( int index, double attachHeight )
      : mIdx( index )
      , mAttach( attachHeight )
   {
   }

   int mIdx;
   double mAttach;
};

void DoTestCase( int caseNum )
{
   cout << "Case #" << caseNum << ": ";

   int numVines;
   cin >> numVines;

   vector<double> dist( numVines, 0.0 );
   vector<double> length( numVines, 0.0 );

   for (int i = 0; i < numVines; ++i)
   {
      cin >> dist[i] >> length[i];
   }

   double totalDist;
   cin >> totalDist;

   // Figure out which vines we can reach and just move forward with that
   stack<SVine> vineAttachments;
   vineAttachments.push( SVine( 0, dist[0] ) );

   bool success = false;
   while (!success && !vineAttachments.empty())
   {
      SVine vine = vineAttachments.top();
      vineAttachments.pop();

      // From where we are can we reach the end?
      double distToEnd = totalDist - dist[vine.mIdx] ;
      if ( distToEnd <= vine.mAttach )
      {
         success = true;
         break;
      }

      // Guess we can't figure out which vines we can attach to
      int vineIdx = vine.mIdx;
      double currentDist = dist[vineIdx];
      double maxDist = vine.mAttach;
      for (int i = vineIdx + 1; i < numVines; ++i)
      {
         double distToVine = dist[i] - currentDist;
         if ( distToVine <= maxDist )
         {
            vineAttachments.push( SVine( i, min( distToVine, length[i] ) ) );
         }
      }
   }

   cout << ((success) ? "YES" : "NO") << endl;
}

int main(int argc, char* argv[])
{
   int numTestCases = 0;
   cin >> numTestCases;

   for ( int i = 0; i < numTestCases; ++i )
   {
      DoTestCase( i + 1 );
   }

	return 0;
}
