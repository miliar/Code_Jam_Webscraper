/** OK, 17.7.2008 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

const unsigned MAX_NAME    = 128;
const unsigned MAX_ENGINES = 100;
const unsigned MAX_QUERIES = 1024;

char names[MAX_ENGINES][MAX_NAME];      // engine names
int  seq[MAX_ENGINES][MAX_QUERIES];     // length of the longest suitable sequence ending at the index
int  engines;
int  queries;

bool readInstance ( void )
{
  if ( scanf( "%d\n", &engines ) != 1 )
    return false;

  for ( int i = 0; i < engines; i++ )
    if ( !gets( names[i] ) ) return false;

  if ( scanf( "%d\n", &queries ) != 1 )
    return false;

  memset( seq, 0, sizeof( seq ) );
  return true;
}

void solveInstance ( int order )
{
  int i, j;
  char name[MAX_NAME];
  for ( i = 0; i < queries; i++ )
  {
    if ( !gets( name ) ) return;
    for ( j = 0; j < engines; j++ )
      if ( strcmp( name, names[j] ) )
        seq[j][i+1] = ++seq[j][i];
      else
        seq[j][i] = 0;
  }

  i = queries - 1;
  int switches = -1;
  while ( i >= 0 )
  {
    int longest = seq[0][i];
    for ( j = 1; j < engines; j++ )
      if ( seq[j][i] > longest )
        longest = seq[j][i];
    // now skip the longest sequence:
    i -= longest;
    switches++;
  }

  if ( queries < 2 ) switches = 0;

  printf( "Case #%d: %d\n", order, switches );
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
