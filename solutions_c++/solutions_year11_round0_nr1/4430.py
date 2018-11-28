// CodeJam2011.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const string fileName = "A-small";

  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());
    
  string temp;
  getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case
    string input;
    getline(inputFile, input);

    istringstream datastream (input, istringstream::in);

    int N;
    datastream >> N;

    int current_time = 0;
    int pos_o = 1;
    int pos_b = 1;
    int time_o = 0;
    int time_b = 0;

    char next_robot;
    int next_button;
    int time_to_button;
    int dist_to_button;

    for ( int i = 0; i < N; ++i )
    {
      datastream >> next_robot;
      datastream >> next_button;
      if ( next_robot == 'O' )
      {
        dist_to_button = abs( next_button - pos_o );
        time_to_button = dist_to_button - (current_time - time_o) + 1;
        time_to_button <= 1 ? ++current_time : current_time += time_to_button;
        pos_o = next_button;
        time_o = current_time;         
      }
      else
      {
        dist_to_button = abs( next_button - pos_b );
        time_to_button = dist_to_button - (current_time - time_b) + 1;
        time_to_button <= 1 ? ++current_time : current_time += time_to_button;
        pos_b = next_button;
        time_b = current_time;         
      }
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": " << current_time << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

