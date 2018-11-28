// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const std::string fileName = "A-small-attempt0";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case
    std::string input;
    size_t found;
    
    std::getline(inputFile, input);
    unsigned long N; 
    unsigned long K;
    int i = 0;
    std::string new_input = input;
    while (( found = new_input.find_first_of(" ")) != std::string::npos)
    {
      input = new_input;
      N =  atoi(input.substr(0, found).c_str());
      new_input = input.substr(found+1, input.size()-1);
    }
    K = atoi(new_input.c_str());
    
    struct snapper
    {
      bool has_power;
      bool is_on;
    };
    vector<snapper> snappers;
    for ( unsigned long i = 0; i < N; i++ )
    {
      snapper a_snapper;
      if ( i == 0 )
      {
        a_snapper.has_power = true;
      }
      else
      {
        a_snapper.has_power = false;
      }
      a_snapper.is_on = false;
      snappers.push_back(a_snapper);
    }

    for ( unsigned long snap_finger = 0; snap_finger < K; snap_finger++ )
    {
      for ( unsigned long ix = 0; ix < snappers.size(); ix++ )
      {
        if ( snappers[ix].has_power )
        {
          snappers[ix].is_on  = !snappers[ix].is_on;
        }
      }
      for ( unsigned long ix = 1; ix < snappers.size(); ix++ )
      {
        if ( snappers[ix-1].has_power && snappers[ix-1].is_on )
        {
          snappers[ix].has_power  = true;
        }
        else
        {
          snappers[ix].has_power  = false;
        }
      }
    }
    
    std::string output = snappers[N-1].has_power && snappers[N-1].is_on ? "ON" : "OFF";
    // Output the results
    outputFile << "Case #" << caseNumber << ": " <<  output << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

