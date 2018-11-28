#include <iostream>

using namespace std;

const int MAX_N = 1000;

long long group[ MAX_N * 2 ];     // group sizes (cyclic)
int groupsFrom[ MAX_N ];          // how many groups fit into one train (starting from i-th group)
long long fareFrom[ MAX_N ];      // train fare (starting from i-th group)
long long sums[ MAX_N ][ MAX_N ]; // group segment sums: sums[start][len] (up to k)
int cycleRuns[ MAX_N ];           // cyclic semigroup construction: runs
long long cycleFare[ MAX_N ];     // cyclic semigroup construction: total fare

int main ()
{
  int T, N, i, j, m;
  int R;
  long long k, fare;

  cin >> T;
  for ( i = 0; i++ < T; )
  {
    cin >> R >> k >> N;
    for ( j = 0; j < N; j++ )
    {
      cin >> group[ j ];
      group[ j + N ] =
      sums[ j ][ 1 ] = group[ j ];
      groupsFrom[ j ] = N;
      fareFrom[ j ] = group[ j ];
    }

    for ( m = 2; m <= N; m++ )
      for ( j = 0; j < N; j++ )  // segment starting at j-th group, length = m groups
      {
        if ( (sums[ j ][ m ] = sums[ j ][ m - 1 ] + group[ j + m - 1 ]) > k ) // train capacity overflow
        {
          sums[ j ][ m ] = k + 1;
          if ( m - 1 < groupsFrom[ j ] )
          {
            groupsFrom[ j ] = m - 1;
            fareFrom[ j ] = sums[ j ][ m - 1 ];
          }
        }
        else
          if ( m == N )
          {
            groupsFrom[ j ] = m;
            fareFrom[ j ] = sums[ j ][ m ];
          }
      }

    memset( cycleRuns, 0, sizeof(cycleRuns) );
    fare = 0;
    j = 0;                       // starting group index
    long long cycleTotal = 0;
    int cycleR = 0;

    while ( R > 0 )              // looking for cyclic semigroup
    {
      cycleFare[ j ] = fare;
      cycleRuns[ j ] = R;
      fare += fareFrom[ j ];
      j += groupsFrom[ j ];
      if ( j >= N ) j -= N;
      R--;
      if ( cycleRuns[ j ] )      // cycle found!
      {
        cycleR = cycleRuns[ j ] - R;
        cycleTotal = fare - cycleFare[ j ];
        break;
      }
    }

    if ( R > 0 )
    {
      int cycles = R / cycleR;
      fare += cycles * cycleTotal;
      R -= cycles * cycleR;

      while ( R > 0 )
      {
        fare += fareFrom[ j ];
        j += groupsFrom[ j ];
        if ( j >= N ) j -= N;
        R--;
      }
    }

    cout << "Case #" << i << ": " << fare << endl;
  }

  return 0;
}
