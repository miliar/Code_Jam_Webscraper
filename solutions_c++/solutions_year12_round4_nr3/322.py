#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
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

void DoTestCase( int caseNum )
{
   cout << "Case #" << caseNum << ": ";

   int numPeaks;
   cin >> numPeaks;

   vector<int> highestPeaks( numPeaks - 1, 0 );
   vector<long long> peakHeights( numPeaks, 0 );

   for(int i = 0; i < numPeaks - 1; ++i)
   {
      int highest;
      cin >> highest;

      highestPeaks[i] = highest - 1;
   }

   long long const maxHeight = 1000000000;
   bool satisfied = false;
   bool failure = false;

   while ( !satisfied && !failure )
   {
      satisfied = true;
      for (int i = numPeaks - 2; i >= 0; --i)
      {
         int highestPeakIdx = i + 1;
         double height = (double)peakHeights[i];
         double maxSlope = (peakHeights[i + 1] - height);

         for (int x = 2; i + x < numPeaks; ++x)
         {
            double heightAtIndex = height + maxSlope * x;
            if ( peakHeights[x + i] > (long long)heightAtIndex )
            {
               highestPeakIdx = x + i;
               maxSlope = (double)(peakHeights[i + x] - height) / (double)x;
            }
         }
         
         // We have a problem... need to adjust the peaks now
         if ( highestPeakIdx != highestPeaks[i] )
         {
            int adjustedPeakIdx = highestPeaks[i];
            long long minHeight = (long long)ceil( ( height + maxSlope * (adjustedPeakIdx - i) ) + 0.000001 );

            if ( minHeight <= peakHeights[adjustedPeakIdx] )
            {
               failure = true;
            }

            peakHeights[adjustedPeakIdx] = minHeight;

            if ( peakHeights[adjustedPeakIdx] > maxHeight )
            {
               failure = true;
            }

            satisfied = false;
            break;
         }
      }
   }

   if ( !failure )
   {
      for (int i = 0; i < numPeaks; ++i)
      {
         cout << peakHeights[i] << " ";
      }
      cout << endl;
   }
   else
   {
      cout << "Impossible" << endl;
   }
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
