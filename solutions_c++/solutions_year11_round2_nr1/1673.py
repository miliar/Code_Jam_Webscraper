#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <iterator>
#include <string>
#include <map>
using namespace std;

struct STeam
{
   STeam()
      : wins( 0.0 )
      , loses( 0.0 )
      , WP( 0.0f )
      , OWP( 0.0f )
      , OOWP( 0.0f )
   {}

   vector<int> opponents;
   vector<bool> result;
   double wins;
   double loses;
   double WP;
   double OWP;
   double OOWP;
};

void DoTestCase( int caseNum )
{
   vector< STeam > mTeams;
   vector< vector< int > > mResults;

   int numTeams;
   cin >> numTeams;

   mTeams.resize( numTeams );
   mResults.resize( numTeams, vector<int>( numTeams, 0 ) );

   for ( int t = 0; t < numTeams; ++t )
   {
      for ( int o = 0; o < numTeams; ++o )
      {
         char c;
         cin >> c;
         if ( t < o )
         {
            if ( c == '1' )
            {
               mTeams[t].wins++;
               mTeams[o].loses++;
               mTeams[t].opponents.push_back( o );
               mTeams[t].result.push_back( true );
               mTeams[o].opponents.push_back( t );
               mTeams[o].result.push_back( false );
            }
            else if ( c == '0' )
            {
               mTeams[o].wins++;
               mTeams[t].loses++;
               mTeams[o].opponents.push_back( t );
               mTeams[o].result.push_back( true );
               mTeams[t].opponents.push_back( o );
               mTeams[t].result.push_back( false );
            }
         }
      }
   }

   for ( int i = 0; i < mTeams.size(); ++i )
   {
      mTeams[i].WP = mTeams[i].wins / ( mTeams[i].wins + mTeams[i].loses );
   }

   for ( int i = 0; i < mTeams.size(); ++i )
   {
      //cout << i << " OWP" << endl;
      double owp = 0.0;
      for ( int o = 0; o < mTeams[i].opponents.size(); ++o )
      {
         int opponent = mTeams[i].opponents[o];
         double adjustedWins = mTeams[opponent].wins - (( mTeams[i].result[o] ) ? 0.0 : 1.0);
         double games = ( mTeams[opponent].wins + mTeams[opponent].loses - 1.0 );
         double adjustedWP = adjustedWins / games;

         //cout << "opponent " << opponent << " wins: " << adjustedWins << " WP: " << adjustedWP << endl;
         owp += adjustedWP;
      }

      mTeams[i].OWP = owp  / (double)mTeams[i].opponents.size();
   }

   for ( int i = 0; i < mTeams.size(); ++i )
   {
      double oowp = 0.0;
      for ( int o = 0; o < mTeams[i].opponents.size(); ++o )
      {
         int opponent = mTeams[i].opponents[o];
         oowp += mTeams[opponent].OWP;
      }

      mTeams[i].OOWP = oowp  / (double)mTeams[i].opponents.size();
   }

   cout << "Case #" << caseNum << ":" << endl;
   for ( int i = 0; i < mTeams.size(); ++i )
   {
      //cout << " WP: " << mTeams[i].WP << " OWP: " << mTeams[i].OWP << " OOWP: " << mTeams[i].OOWP << endl;
      double RPI = 0.25 * mTeams[i].WP + 0.50 * mTeams[i].OWP + 0.25 * mTeams[i].OOWP;
      printf( "%0.12f\n", RPI );
   }

   // Output result here
}

int main(int argc, char* argv[])
{
   int numTestCases = 0;
   cin >> numTestCases;

   for ( int i = 0; i < numTestCases; ++i )
   {
      DoTestCase( i + 1 );
   }

   cin >> numTestCases;
	return 0;
}
