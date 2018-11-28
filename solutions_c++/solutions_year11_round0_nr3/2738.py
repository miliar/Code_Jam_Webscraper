#include <stdio.h>
#include <tchar.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  //const string fileName = "A-test";
  const string fileName = "C-large";
  //const string fileName = "A-large";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());

  inputFile >> numCases;

  for( int caseNumber = 1; caseNumber <= numCases; ++caseNumber )
  {
    // Read the inputs...May be multiple lines of inputs per case
    int n = 0;
    int c = 0;
    bool cry = false;
    int pile_value = 0;
    int pile_xor = 0;
    int min_value = -1;
    vector<int> pile;
    
    inputFile >> n;
    
    for( int ix = 0; ix < n; ++ix )
    {
      inputFile >> c;
      pile_xor = pile_xor ^ c;
      pile_value += c;
      if( min_value < 0 )
      {
        min_value = c;
      }
      else
      {
        min_value = min( min_value, c );
      }
    }
    
    cry = pile_xor > 0;

    if( cry )
    {
      // Output the results
      outputFile << "Case #" << caseNumber << ": NO\n";
    }
    else
    {
      outputFile << "Case #" << caseNumber << ": " << ( pile_value - min_value )  << "\n";
    }
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

