// usage: botTrust <input file>



#include <fstream>

#include <stdlib.h>

#include <string>
#include <vector>
#include <sstream>
#include <iterator>



int main( int argc, char* argv[] ) {

  // the timer results; these values will written out as the final result
  std::vector< int > results;

  // the length of a particular sequence
  int seqLength = 0;

  // the timer for each sequence; will be stored in results
  int timer = 0;

  // the current position of each robot; defaults to 1
  int posB = 1;
  int posO = 1;
 
  // the buttons to be hit by orange robot
  std::vector<int> orangeData(1,0);
  // the sequence order for those buttons
  std::vector<int> orangeLoc(1,0);

  // same, but for blue robot
  std::vector<int> blueData(1,0);
  std::vector<int> blueLoc(1,0);
  

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
        
        // tokenize the line 
        std::istringstream iss( line );
        std::vector<std::string> tokens;
        copy(std::istream_iterator<std::string>(iss), 
          std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string> >(tokens));

        // obtain the sequence length
        seqLength = atoi(tokens[0].c_str());

        posB = 1;
        posO = 1;
        timer = 0;

        // now parse the rest of the row and read it into the orange and blue data
        // fill these vectors in reverse so the later sequence values are in the front
        for( int i = tokens.size() - 1; i > 0; i-- ) {  
          if( tokens[i] == "O" ) {
            orangeData.push_back( atoi( tokens[i + 1].c_str() ) );
            orangeLoc.push_back( i/2 );
          }
          else if( tokens[i] == "B" ) {
            blueData.push_back( atoi( tokens[i + 1].c_str() ) );
            blueLoc.push_back( i/2 );
          }
        }

        // move the bots until a solution is found
        int numActions = 0;
        while( numActions < seqLength ) {
          // can either robot push a button? only one can push; move the other robot accordingly
      
          // orange can push
          if( orangeData.back() == posO && orangeLoc.back() == numActions ) {
            orangeData.pop_back();
            orangeLoc.pop_back();
            numActions++;  

            // now move blue; 3 cases: move forwards, move back, or stay
            if( blueData.back() > posB && blueData.back() <= 100 ) {
              posB++;
            }
            else if( blueData.back() < posB && blueData.back() >= 1 ) {
              posB--;
            }
          }

          // blue can push
          else if( blueData.back() == posB && blueLoc.back() == numActions ) {
            blueData.pop_back();
            blueLoc.pop_back();
            numActions++;  

            // now move orange
            if( orangeData.back() > posO && orangeData.back() <= 100 ) {
              posO++;
            }
            else if( orangeData.back() < posO && orangeData.back() >= 1 ) {
              posO--;
            }
          }

          // move both; no pushing
          else {
           if( blueData.back() > posB && blueData.back() <= 100 ) {
              posB++;
            }
            else if( blueData.back() < posB && blueData.back() >= 1 ) {
              posB--;
            }

            if( orangeData.back() > posO && orangeData.back() <= 100 ) {
              posO++;
            }
            else if( orangeData.back() < posO && orangeData.back() >= 1 ) {
              posO--;
            }
          }

          // advance the timer
          timer++;
        }
        results.push_back( timer );
      }
    }
  fileInput.close();
  }

  // write out the data file
  std::ofstream outputFile( "output.txt" );
  for(int i = 0; i < results.size(); i++) {
    outputFile << "Case #" << i+1 << ": " << results[i] << std::endl;
  }

  outputFile.close();
}
