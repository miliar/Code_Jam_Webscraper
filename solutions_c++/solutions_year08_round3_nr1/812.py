#include <string.h>
#include <iostream>
#include <assert.h>


using namespace std;

int P,K,L;
int freq[ 1000 ];

int maxFreq() {
  int maxKey = 0;
  int max = freq[ maxKey ];
  for ( int i = 0; i < L; ++i ) {
    if ( freq[ i ] > max ) {
      maxKey = i;
      max = freq[ maxKey ];
    }
  }
  if ( 0 == max )
    return -1;
  else
    return maxKey;
}


int pressesNeeded() {
  int retval = 0;
  int key = 1;
  int presses = 1;
  int max = maxFreq();

  while ( max != -1 ) {
    retval += presses * freq[ max ];
    freq[ max ] = 0;
    if ( ! ( key++ % K ) ) ++presses;
    max = maxFreq();
  }

  return retval;
}

int main () {
  int numberOfCases, caseNumber = 0;

  scanf( "%i", &numberOfCases );


  while ( numberOfCases >= ++caseNumber ) {
    scanf( "\n%i %i %i\n", &P, &K, &L );
    int tmp;
    for ( int i = 0; i < L; ++i ) {
      cin >> tmp;
      freq[ i ] = tmp;
    }

    tmp = pressesNeeded();

    printf( "Case #%i: %i\n", caseNumber, tmp );

  }

  return 0;
}


    //cin >> f >> R >> t >> r >> g;
    //scanf( "%lf %lf %lf %lf %lf\n", &f,&R,&t,&r,&g );
    //printf( "%lf %lf %lf %lf %lf\n", f,R,t,r,g );

