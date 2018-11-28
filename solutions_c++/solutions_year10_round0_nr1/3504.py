// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const std::string fileName = "A-large";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case
    int devices_N;
    int snaps_K;

    inputFile >> devices_N >> snaps_K;
    
    //create mask
    int mask = (1 << devices_N) - 1;
    
    std::string answer = "OFF";
    if ((snaps_K & mask) == mask)
    {
      answer = "ON";
    }

    outputFile << "Case #" << caseNumber << ": " << answer << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

