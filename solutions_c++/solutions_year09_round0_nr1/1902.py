
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


unsigned long ulGetBitPattern( const char c )
{
  unsigned long ul = 1;
  for ( int i='a'; i < c; i++ ) ul <<= 1;
  return ul;
}


int _tmain(int argc, _TCHAR* argv[])
{
  int L,D,N;
  int nCount;
  char c;
  bool bMatch;
  ifstream input;
  ofstream output;
  unsigned long *aDictionary; //assume long to have at least 32 bits
  unsigned long *aTestCase;   //same as above

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> L >> D >> N; 

  aDictionary = new unsigned long[L*D]; 
  aTestCase   = new unsigned long[L];

  //read dictionary
  for ( int i=0; i < D; i++ )
  {
    for ( int j=0; j < L; j++ )
    {
      input >> c;
      aDictionary[ i*L + j ] = ulGetBitPattern( c );
    }
  }

  //read test cases
  for ( int i=0; i < N; i++ )
  {
    for ( int j=0; j < L; j++ )
    {
      input >> c;
      if ( c != '(' )
      {
        aTestCase[j] = ulGetBitPattern( c );
      }
      else
      {
        aTestCase[j] = 0;
        input >> c;
        while ( c != ')' )
        {
          aTestCase[j] |= ulGetBitPattern( c );
          input >> c;
        }
      }
    }
    nCount=0;
    for ( int k=0; k < D; k++ )
    {
      bMatch = true;
      for ( int j=0; j < L; j++ )
      {
        if ( !(aTestCase[j] & aDictionary[k*L + j]) ) 
        {
          bMatch = false;
          break;
        }
      }
      if ( bMatch ) nCount++;
    }
    output << "Case #" << i+1 << ": " << nCount << endl;  
  }
  input.close();
  output.close();


  delete [] aDictionary;
  delete [] aTestCase;
	return 0;
}

