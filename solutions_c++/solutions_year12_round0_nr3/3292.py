// CalculatePairs.cpp
// by Mike Lunderville

#include <vector> // For the use of vectors.
#include <iostream> // Needed for input/output.
#include <fstream> // Needed to input/output to files.
using namespace std;

bool isPair( const int &num1, const int &num2 );

int main( int argc, char *argv[] )
{ 
     int i, j, k;
     int min, max;
     int cases;
     int numPairs;

     ifstream fileIn;
     ofstream fileOut;

     fileIn.open( argv[1] );
     fileOut.open( "OutputFile.txt" );
     
     fileIn >> cases;

     for ( i = 0; i < cases; ++i ) {
	  numPairs = 0;
	  fileIn >> min;
	  fileIn >> max;
	  
	  for ( j = min; j < max; ++j ) {
	       for ( k = j+1; k <= max; ++k ) {
		    if ( isPair( j, k ) )
			 ++numPairs;
	       }
	  }
	  
	  fileOut << "Case #" << i+1 << ": " << numPairs << endl;
     }

     fileIn.close();
     fileOut.close();

     return 0;
}
     
bool isPair( const int &num1, const int &num2 )
{
     int i;
     unsigned int j;
     unsigned int element1 = 0, element2 = 0;
     unsigned int offset;
     bool pair;
     
     vector < int > first;
     vector < int > second;

     for ( i = num1; i > 0; i /= 10 )
	  first.push_back( i % 10 );
     for ( i = num2; i > 0; i /= 10 )
	  second.push_back( i % 10 );
	 

     for ( offset = 1; offset < first.size(); ++offset ) {
	  element1 = 0;
	  element2 = element1 + offset;
	  pair = true;
	  
	  for ( j = 0; j < first.size(); ++j, ++element1, ++element2 ){
	       if ( element2 >= first.size() )
		    element2 = 0;
	       if ( first.at(element1) != second.at(element2) )
		    pair = false;
	  }
	  if ( pair )
	       return true;
     }
     
     return false;
}
