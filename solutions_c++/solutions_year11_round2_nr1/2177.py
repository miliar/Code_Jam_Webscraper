#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  unsigned int nbCases;
  cin >> nbCases;
  for( unsigned int noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      unsigned int nbTeams;
      cin >> nbTeams;
      vector< vector< char > > schedule( nbTeams );
      for( auto &t: schedule )
        {
          t = vector< char >( nbTeams );
          for( auto &x: t )
            cin >> x;
        }

      cout << "Case #" << noCase << ":" << endl;

      vector< double > owp( nbTeams );
      for( unsigned int noTeam = 0 ; noTeam < nbTeams ; noTeam++ )
        {
          double accOpponentWP = 0;
          unsigned int nbOpp = 0;
          for( unsigned int opponent = 0 ; opponent < nbTeams ; opponent++ )
            if( opponent != noTeam && schedule[noTeam][opponent] != '.' )
              {
                nbOpp++;
                unsigned int nbWon = 0;
                unsigned int nbLose = 0;
                for( unsigned int o = 0 ; o < nbTeams ; o++ )
                  if( o != noTeam )
                    switch( schedule[opponent][o] )
                      {
                      case '1': nbWon++; break;
                      case '0': nbLose++; break;
                    }
                accOpponentWP += (double)nbWon / ( nbWon + nbLose );
              }
          owp[noTeam] = accOpponentWP / nbOpp;
        }

      vector< double > oowp( nbTeams );
      for( unsigned int noTeam = 0 ; noTeam < nbTeams ; noTeam++ )
        {
          double accOwp = 0;
          unsigned int nbOpp = 0;
          for( unsigned int o = 0 ; o < nbTeams ; o++ )
            if( o != noTeam && schedule[noTeam][o] != '.' )
              {
                nbOpp++;
                accOwp += owp[o];
              }
          oowp[noTeam] = accOwp / nbOpp;
        }

      for( unsigned int noTeam = 0 ; noTeam < nbTeams ; noTeam++ )
        {
          unsigned nbWon = 0;
          unsigned nbLose = 0;
          for( auto &l: schedule[noTeam] )
            switch( l )
              {
              case '1': nbWon++; break;
              case '0': nbLose++; break;
              }
          double wp = (double)nbWon / ( nbWon + nbLose );

          cout << ( .25 * wp + .5 * owp[noTeam] + .25 * oowp[noTeam] ) << endl;
        }
    }
  return EXIT_SUCCESS;
}
