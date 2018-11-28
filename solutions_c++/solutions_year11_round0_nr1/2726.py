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
  //xconst string fileName = "A-small-attempt0";
  const string fileName = "A-large";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());

  inputFile >> numCases;

  for( int caseNumber = 1; caseNumber <= numCases; ++caseNumber )
  {
    // Read the inputs...May be multiple lines of inputs per case
    int num_pushes = 0;
    int o_pos = 1;
    int o_last_action = 0;
    int b_pos = 1;
    int b_last_action = 0;
    int elapsed_time = 0;
    char robot;
    int button = 0;
    
    inputFile >> num_pushes;
    
    for( int ix = 0; ix < num_pushes; ++ix )
    {
      inputFile >> robot;
      inputFile >> button;
      
      if( robot == 'O' )
      {
        int travel_time = abs( button - o_pos );  
        
        if( travel_time + o_last_action > elapsed_time )
        {
          elapsed_time = travel_time + 1 + o_last_action; 
          o_last_action = elapsed_time;
        }
        else
        {
          elapsed_time++;
        }
        
        o_last_action = elapsed_time;
        o_pos = button;
      }
      else
      {
        int travel_time = abs( button - b_pos );  
        
        if( travel_time + b_last_action > elapsed_time )
        {
          elapsed_time = travel_time + 1 + b_last_action; 
        }
        else
        {
          elapsed_time++;
        }
        
        b_last_action = elapsed_time;
        b_pos = button;
      }
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": " << elapsed_time << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

