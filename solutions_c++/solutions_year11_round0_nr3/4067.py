// CodeJam2011.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const string fileName = "C-small";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());
    
  string temp;
  getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case

    getline(inputFile, temp);
    int sizeArray = atoi(temp.c_str());

    string input;
    getline(inputFile, input);

    istringstream datastream (input, istringstream::in);
    long total_tries = 1 << sizeArray;
    vector<int> candies;

    for (int i = 0; i < sizeArray; ++i )
    {
      int value;
      datastream >> value;
      candies.push_back(value);
    }

    int max_value = 0;
    for ( int i = 1; i < total_tries - 1; ++i )
    {
      int total_patrick =0;
      int total_sean = 0;
      int real_patrick = 0;
      int real_sean = 0;

      for ( int j = 0; j < sizeArray; ++j )
      {
        if ( ( ( 1<<j ) & i ) !=0 )
        {
          real_sean += candies[j];
          total_sean = total_sean ^ candies[j];
        }
        else
        {
          real_patrick += candies[j];
          total_patrick = total_patrick ^ candies[j];
        }
      }
      if ( total_patrick == total_sean )
      {
        if ( real_patrick > max_value )
          max_value = real_patrick;
        if ( real_sean > max_value )
          max_value = real_sean;
      }
    }

    // Output the results
    if ( max_value == 0 )
      outputFile << "Case #" << caseNumber << ": " << "NO" << "\n";
    else
      outputFile << "Case #" << caseNumber << ": " << max_value << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

