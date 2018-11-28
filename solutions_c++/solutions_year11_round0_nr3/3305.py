#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <set>

#define SUM(a,b) ((a)^(b))

int size(int n)
{
  int ret = 0;
  do { n/=10; ret++; } while(n>0);
  return ret;
}

const char* read_number( const char *p, int &n )
{
  if(!*p)
    return NULL;

  n = atoi(p);
  p += size(n)+1;

  if(!*p)
    return NULL;
  return p;
}

int try_piles( const std::vector<int> &all_candy, const std::set<int> &first_pile )
{
  std::set<int>::const_iterator i;
/*  printf( "first_pile: " );
  for( i=first_pile.begin(); i != first_pile.end(); i++ )
    printf( "%d ", *i );
  printf( "\n" );
*/

  int first_sum=0, second_sum=0, second_true_sum=0;
  for( i=first_pile.begin(); i != first_pile.end(); i++ )
  {
    first_sum = SUM(first_sum, all_candy[(*i)] );
  }

  int j;
  int count = all_candy.size();
  for( j=0; j<count; j++ )
  {
    if( first_pile.find(j) != first_pile.end() )
     continue;
    second_sum = SUM(second_sum, all_candy[j]);
    second_true_sum += all_candy[j];
  }

  //printf( "first_sum: %d, second_sum: %d\n", first_sum, second_sum );
  if( second_sum == first_sum )
    return second_true_sum;

  return -1;
}

int produce_permutations( const std::vector<int> &all_candy, std::set<int> &first_pile, int start, int min )
{
  int bestpile = -1;
  int count = all_candy.size();
  //printf( "start=%d\n", start );
  for( int i=min; i<count; i++ )
  {
     if( first_pile.find(i) != first_pile.end() )
	continue;
     first_pile.insert(i);
     int pilesum = try_piles( all_candy, first_pile );
     if( pilesum > bestpile )
     {
       bestpile = pilesum;
     }
     if( start+1 < count )
       produce_permutations( all_candy, first_pile, start+1, i+1 );
     first_pile.erase(i);
  }

  return bestpile;	
}

void solve( int n, const char *string )
{
  std::vector<int> all_candy;
  const char *p = string;
  int value;
  for( int i=0; i<n; i++ )
  {
    p = read_number( p, value );
    all_candy.push_back( value );
  }

  std::set<int> first_pile;
  int result = produce_permutations( all_candy, first_pile, 0, 0 );

  if( result < 1 )
    printf( "NO" );
  else
    printf( "%d", result );
}

int main(void)
{
  char buf[2048];
  fgets(buf, 2048, stdin);
  int count;
  read_number(buf, count);
  for( int i=0; i<count; i++ )
  {
    int size;
    fgets(buf, 2048, stdin);
    read_number(buf, size);
    fgets(buf, 2048, stdin);
    printf( "Case #%d: ", i+1 );
    solve(size, buf);
    printf( "\n" );
  }

  return 1;
}
