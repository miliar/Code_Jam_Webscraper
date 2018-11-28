// Translate.cpp
// by Mike Lunderville

#include <string> // Needed for use of strings.
#include <iostream> // Needed for input/output.
#include <fstream> // Needed to input/output to files.
using namespace std;

void translate( char &input );

int main( int argc, char *argv[] )
{ 
     int i;
     unsigned int j;
     string line;
     int cases;

     ifstream fileIn;
     ofstream fileOut;

     fileIn.open( argv[1] );
     fileOut.open( "OutputFile.txt" );

     // Input number of cases.
     fileIn >> cases;

     // Skip the rest of the first line.
     getline( fileIn, line );

     for ( i = 0; i < cases; ++i ) {
	  getline( fileIn, line );
	  for ( j = 0; j < line.length(); ++j )
	       translate( line.at(j) );
	  fileOut << "Case #" << i+1 << ": ";
	  fileOut << line << endl;
     }

     fileIn.close();
     fileOut.close();

     return 0;
}
     
void translate( char &input )
{
     switch ( input ) {
     case 'a':
	  input = 'y';
	  break;
     case 'b':
	  input = 'h';
	  break;
     case 'c':
	  input = 'e';
	  break;
     case 'd':
	  input = 's';
	  break;
     case 'e':
	  input = 'o';
	  break;
     case 'f':
	  input = 'c';
	  break;
     case 'g':
	  input = 'v';
	  break;
     case 'h':
	  input = 'x';
	  break;
     case 'i':
	  input = 'd';
	  break;
     case 'j':
	  input = 'u';
	  break;
     case 'k':
	  input = 'i';
	  break;
     case 'l':
	  input = 'g';
	  break;
     case 'm':
	  input = 'l';
	  break;
     case 'n':
	  input = 'b';
	  break;
     case 'o':
	  input = 'k';
	  break;
     case 'p':
	  input = 'r';
	  break;
     case 'q':
	  input = 'z';
	  break;
     case 'r':
	  input = 't';
	  break;
     case 's':
	  input = 'n';
	  break;
     case 't':
	  input = 'w';
	  break;
     case 'u':
	  input = 'j';
	  break;
     case 'v':
	  input = 'p';
	  break;
     case 'w':
	  input = 'f';
	  break;
     case 'x':
	  input = 'm';
	  break;
     case 'y':
	  input = 'a';
	  break;
     case 'z':
	  input = 'q';
	  break;
     }
}
