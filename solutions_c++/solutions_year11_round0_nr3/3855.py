#include <iostream>
#include <vector>

using namespace std;

unsigned long evaluateSum( int bitmask[16], int candies[16], int maxCandies )
{
  unsigned long seanCandies( 0 );
  unsigned long seanActaulVal( 0 );
  unsigned long patrickCandies( 0 );
  //0 -> Sean, 1 -> Patrick
  for( int i = 0; i < maxCandies; ++i ) {
    if( bitmask[i] == 0 ) {
      seanCandies ^= candies[i];
      seanActaulVal += candies[i];
    }
    else {
      patrickCandies ^= candies[i];
    }
  }
  if( seanCandies == patrickCandies )
    return seanActaulVal;
  return 0;
}


unsigned long simulateBits( int bitmask[16],int candies[16], int maxCandies )
{
  unsigned long maxForSean( 0 );
  int m = maxCandies - 1;
  for(;;) {
    for( ; m >= 0 && bitmask[m] != 0; --m )
      bitmask[m] = 0;
    if( m < 0 ) break;
    bitmask[m] = 1;
    int temp = evaluateSum( bitmask, candies, maxCandies );
    maxForSean = ( temp > maxForSean ) ? temp : maxForSean;
    m = maxCandies - 1;
  }
  return maxForSean;
}

int main()
{

  vector< int > vectRes;
  int numOfTestCases( 0 );
  scanf( "%d", &numOfTestCases );

  for( int i = 0; i < numOfTestCases; ++i ) {
    int numOfInputs( 0 );
    scanf( "%d", &numOfInputs );
    int bitmask[16];
    int candies[16];
    memset( bitmask, 0, sizeof( bitmask ) );
    memset( candies, 0, sizeof( candies ) );

    for( int j = 0; j < numOfInputs; ++j ) {
      int candy( 0 );
      scanf( "%d", &candy );
      candies[j] = candy;

      char space( 0 );
      scanf( "%c", &space );
    }
    unsigned long finalRes = simulateBits( bitmask, candies, numOfInputs );
    vectRes.push_back( finalRes );
  }//for( i = numOfTestCases )
  for( unsigned k = 0; k < vectRes.size(); ++k ) {
    if( vectRes[k] != 0 )
      cout<<"Case #"<<k+1<<": "<<vectRes[k]<<endl;
    else
      cout<<"Case #"<<k+1<<": "<<"NO"<<endl;
  }

  return 0;
}