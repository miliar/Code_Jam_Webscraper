#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;


int getMinTime( const vector< int >& arrOrange
              , const vector< int >& arrBlue
              , const string& sequence 
              )
{
  int finalTimeTaken( 0 );
  int stepO = 1;
  int stepB = 1;
  int indexO = 0;
  int indexB = 0;

  for( unsigned k = 0; k < sequence.length(); ++k ) {
    bool needsToBreak( false );
    for(;;) {
      if( indexO < arrOrange.size() ) {
        if( stepO == arrOrange[ indexO ] ) {
          if( sequence[ k ] == 'O' ) {
            ++indexO;
            needsToBreak = true;
          }
        }
        else {
          if( stepO < arrOrange[ indexO ] )
            ++stepO;
          else
            --stepO;
        }
      }//indexO < arrOrange.size()
      if( indexB < arrBlue.size() ) {
        if( stepB == arrBlue[ indexB ] ) {
          if( sequence[ k ] == 'B' ) {
            ++indexB;
            needsToBreak = true;
          }
        }
        else {
          if( stepB < arrBlue[ indexB ] )
            ++stepB;
          else
            --stepB;
        }
      }//indexB < arrBlue.size()
      ++finalTimeTaken;
      if( needsToBreak ) 
        break;
    }//for(;;)
  }//for( unsigned k = sequence )
  return finalTimeTaken;
}

int main()
{
  vector< int > vectFinal;
  int numOfTestCase( 0 );
  scanf( "%d", &numOfTestCase );
  for( int j = 0; j < numOfTestCase; ++j ) {
    //variables for calculations !
    vector< int > arrOrange;
    vector< int > arrBlue;
    string sequence("");

    int numOfSteps( 0 );
    scanf( "%d", &numOfSteps );
    for( int k = 0; k < numOfSteps; ++k ) {
      char space;
      scanf( "%c", &space );
      char person;
      scanf( "%c", &person );
      scanf( "%c", &space );
      int step;
      scanf( "%d", &step );
      if( person == 'O' )
        arrOrange.push_back( step );
      else 
        arrBlue.push_back( step );
      sequence += person;
    }
    int finalTime = getMinTime( arrOrange, arrBlue, sequence ); 
    vectFinal.push_back( finalTime );
  }
  for( int j = 0; j < numOfTestCase; ++j ) {
    cout<<"Case #"<<j+1<<": "<<vectFinal[j]<<endl;
  }
  return 0;
}