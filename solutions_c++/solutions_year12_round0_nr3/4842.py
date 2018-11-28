#include <iostream>
#include <vector>
#include <map>

using namespace std;

map< unsigned, vector< unsigned > >mapper;

unsigned numberOfCycles( const unsigned& A, const unsigned& B, const unsigned& numOfDigits )
{
  unsigned kount( 0 );
  unsigned tempA = A;
  unsigned temp = tempA;
  do {
    unsigned remainder = ( tempA % 10 ) * numOfDigits;
    tempA = remainder + ( tempA / 10 );
    if( remainder == 0 ) continue;
    if( ( tempA <= B ) && ( tempA != A ) && ( temp < tempA ) ) {
      map< unsigned, vector< unsigned > >::iterator iter = mapper.find( temp );
      if( iter != mapper.end() ) {
        vector< unsigned > vect = iter->second;
        unsigned k = 0;
        for( ; k < vect.size(); ++k ) {
          if( vect[ k ] == tempA ) break;
        }
        if( k >= vect.size() ) {
          ++kount;
          iter->second.push_back( tempA );
        }
      }else{
        vector< unsigned > vect( 1 );
        vect[ 0 ] = tempA;
        mapper[ temp ] = vect;

        vect[ 0 ] = temp;
        mapper[ tempA ] = vect;
        ++kount;
      }
    }     
  }while( tempA != A );
  return kount;
}

unsigned getNumOfDigits( const unsigned& number )
{
  unsigned k( 10 );
  for( unsigned tempNum = number; ; k *= 10 )
    if( tempNum / k == 0 ) break;
  return k/10;
}

unsigned computeCycles( const unsigned& A, const unsigned& B )
{
  unsigned kount( 0 );
  unsigned numberOfDigits( getNumOfDigits( A ) );
  for( unsigned k = A; k <= B; ++k ) {
    kount += numberOfCycles( k, B, numberOfDigits );
  }
  return kount;
}

int main()
{
  unsigned numOfTestCases;
  cin >> numOfTestCases;
  vector< unsigned > finalResults;
  for( unsigned k = 0; k < numOfTestCases; ++k ) {
    unsigned A,B;
    cin >> A;
    cin >> B;
    mapper.clear();
    finalResults.push_back( computeCycles( A, B ) );
  }

  for( unsigned k = 0; k < finalResults.size(); ++k )
    cout<<"Case #"<<k + 1<<": "<<finalResults[ k ]<<endl;
  cout<<"\n\n";
  return 0;
}