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
#include <math.h>

using namespace std;

ifstream fin( "a-large.in" );
ofstream fout( "large-answer.out" );

#define in fin
#define cout fout
#define pf printf

#define g(name) 	in >> name
#define gi(name)	int name;		   g(name)
#define gl(name)	long name;		   g(name)
#define gll(name) long long name;   g(name)
#define gd(name)	double name; 	   g(name)
#define gc(name)	char name;		   g(name)
#define gb(name)	bool name;		   g(name)
#define gs(name)  string name;      g(name)

#define fri(var, a, b)		for( int var = a; var < b; var++ )
#define frd(var, a, b) 	   for( int var = a; var > b; var-- )

int main()
{
   gi(numTrials);

   fri(t, 0, numTrials)
   {
      gi(numTeams);
      int data[numTeams][numTeams];

      fri(i, 0, numTeams)
      {
         fri(j, 0, numTeams)
         {
            gc(ch);
            if(ch == '.')
               data[i][j] = -1;
            else
               data[i][j] = ch - '0';
            // cout << data[i][j] << ' ';
         }
         // cout << '\n';
      }

      float wp[numTeams];

      fri(i, 0, numTeams)
      {
         int numGames = 0;
         int won = 0;

         fri(j, 0, numTeams)
         {
            if( data[i][j] >= 0 )
               numGames++;
            if( data[i][j] == 1 )
               won++;
         }

         wp[i] = (float) won / numGames;
         // cout << "WP: " << wp[i] << '\n';
      }

      float owp[numTeams];

      fri(i, 0, numTeams)
      {
         float curOwp = 0;
         int num = 0;

         fri(j, 0, numTeams)
         {
            // only opponents
            if( j == i || data[i][j] == -1 )
               continue;

            int numGames = 0;
            int won = 0;

            fri(k, 0, numTeams)
            {
               if( k == i )
                  continue;

               if( data[j][k] >= 0 )
                  numGames++;
               if( data[j][k] == 1 )
                  won++;
            }

            assert( won <= numGames );

            float wp = (float) won / numGames;
            curOwp += wp;
            num++;
            // printf( "W: %d, NG: %d, WP: %.2f CO: %.2f\n", won, numGames, wp, curOwp );
         }

         owp[i] = curOwp / num;
         // cout << "OWP: " << owp[i] << '\n';
      }

      float oowp[numTeams];

      fri(i, 0, numTeams)
      {
         float curOowp = 0;
         int num = 0;

         fri(j, 0, numTeams)
         {
            if( j == i || data[i][j] == -1 )
               continue;
            curOowp += owp[j];
            num++;
         }

         // printf( "OOWP: %.2f\n", curOowp );
         oowp[i] = curOowp / num;
      }

      cout << "Case #" << t + 1 << ":\n";
      cout.precision(8);
      fri(i, 0, numTeams)
         cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << '\n';
   }

   return 0;
}

