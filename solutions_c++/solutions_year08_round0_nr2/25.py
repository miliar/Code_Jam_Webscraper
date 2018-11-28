/** OK, 17.7.2008 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

const unsigned MAX_TRIPS   = 100;

struct Trip
{
  int dep, arr;
};

Trip trip[2][MAX_TRIPS+1];            // two lists of trips, each one sorted by the departure time
int trips[2];                         // number of trips
int trains[2];                        // trains needed
int turnaround;

bool readInstance ( void )
{
  if ( scanf( "%d %d %d\n", &turnaround, trips, trips+1 ) != 3 )
    return false;

  int hFrom, mFrom, hTo, mTo, i, j, k, l, dep;
  for ( i = 0; i < 2; i++ )
  {
    for ( j = 0; j < trips[i]; j++ )
    {
      if ( scanf( "%d:%d %d:%d\n", &hFrom, &mFrom, &hTo, &mTo ) != 4 )
        return false;

      trip[i][j].dep = dep = hFrom * 60 + mFrom;

      for ( k = 0; trip[i][k].dep < dep; k++ ) ;
      if ( k < j )
        for ( l = j; l > k; l-- )
          trip[i][l] = trip[i][l-1];
      trip[i][k].dep = dep;
      trip[i][k].arr = hTo * 60 + mTo + turnaround;
    }
    trip[i][trips[i]].dep = 48*60;
  }

  return true;
}

void solveInstance ( int order )
{
  trains[0] = trains[1] = 0;
  int n[2];
  int station, time;

  while ( trips[0] || trips[1] )
  {                               // use another train
    station = (trip[0][0].dep < trip[1][0].dep) ? 0 : 1;
    trains[station]++;
    n[0] = n[1] = 0;
    do
    {                             // resolve one trip => remove trip[station][n[station]]
      time = trip[station][n[station]].arr;
      memmove( &trip[station][n[station]], &trip[station][n[station]+1], sizeof(Trip)*(trips[station]-n[station]) );
      trips[station]--;
        // we'll arrive at destination:
      station = 1 - station;
      while ( trip[station][n[station]].dep < time ) n[station]++;
    }
    while ( n[station] < trips[station] );
  }

  printf( "Case #%d: %d %d\n", order, trains[0], trains[1] );
  fflush( stdout );
}

int main ( void )
{
  int n;
  if ( scanf( "%d", &n ) != 1 ||
       n < 1 ) return 1;

  for ( int i = 0; i++ < n; )
  {
    if ( !readInstance() ) return 1;
    solveInstance( i );
  }

  return 0;
}
