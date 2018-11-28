// DriverProgram.cpp
// by Mike Lunderville

#include <vector> // For the use of vectors.
#include <iostream> // Needed for input/output.
#include <fstream> // Needed to input/output to files.
using namespace std;

int calculateMax( const vector < int > &scores, const int &surprises,
		  const int &highScore );

int main( int argc, char *argv[] )
{ 
     int i, j;
     int cases;
     int contestants, surprises, highScore;
     int result;

     ifstream fileIn;
     ofstream fileOut;

     fileIn.open( argv[1] );
     fileOut.open( "OutputFile.txt" );
     
     fileIn >> cases;
     
     for ( i = 0; i < cases; ++i ) {
	  fileIn >> contestants;
	  fileIn >> surprises;
	  fileIn >> highScore;

	  vector < int > scores(contestants);

	  for ( j = 0; j < contestants; ++j )
	       fileIn >> scores.at(j);

	  result = calculateMax( scores, surprises, highScore );

	  fileOut << "Case #" << i+1 << ": " << result << endl;
     }

     fileIn.close();
     fileOut.close();

     return 0;
}
     
int calculateMax( const vector < int > &scores, const int &surprises,
		  const int &highScore )
{
     unsigned int i;
     int numSurprised = 0;
     int result = 0;
     int surprisingScore, acceptableScore;

     if ( highScore == 0 || highScore == 1 ) {
	  surprisingScore = acceptableScore = highScore;	  
     }
     else {
	  surprisingScore = 3*highScore - 4;
	  acceptableScore = surprisingScore + 2;
     }

     for ( i = 0; i < scores.size(); ++i ) {	  
	  if ( scores.at(i) >= acceptableScore ) {
	       ++result;
	  }	  	  
	  else if ( scores.at(i) >= surprisingScore 
		    && numSurprised < surprises ) {
	       ++result;
	       ++numSurprised;
	  }	  
     }

     return result;
}
