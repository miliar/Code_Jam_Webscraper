// usage: candy <input file>

#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <limits.h>

int main( int argc, char* argv[] ) {

  std::vector< long > results;

  std::vector< int > binaryVals;

   // read in the data
  std::string line;
  std::ifstream fileInput;
  fileInput.open( argv[1] );
  if( fileInput.is_open() ) {    
    if( fileInput.good() ) {
      // read the initial line
      getline( fileInput, line );
 
      // now read the subsequent lines
      while( getline( fileInput, line ) ) {
        binaryVals.resize( atoi( line.c_str() ) );
        getline( fileInput, line );
  
        // tokenize the line 
        std::istringstream iss( line );
        std::vector<std::string> tokens;
        copy(std::istream_iterator<std::string>(iss), 
          std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string> >(tokens));

        for(int i = 0; i < binaryVals.size(); i++) {
          binaryVals[i] = atoi( tokens[i].c_str() ); 
        }
     
        int xordVal = 0;
        for(int i = 0; i < binaryVals.size(); i++) {
          xordVal ^= binaryVals[i];
        }
        if( xordVal != 0 ) {
          results.push_back( 0 );
        }
        else {
          int sum = 0;
          int smallestVal = INT_MAX;
          for( int i = 0; i < binaryVals.size(); i++ ) {
            sum += binaryVals[i];
            if( binaryVals[i] < smallestVal ) {
              smallestVal = binaryVals[i];
            }
          }
          sum = sum - smallestVal;
          results.push_back( sum );
        }
      }
    }
  fileInput.close();
  }

  std::ofstream outputFile( "output.txt" );
  for(int i = 0; i < results.size(); i++) {
    outputFile << "Case #" << i+1 << ": ";
    if( results[i] == 0 ) {
      outputFile << "NO" << std::endl;
    }
    else {       
      outputFile << results[i] << std::endl;
    }
  }

}
