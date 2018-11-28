// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const std::string fileName = "C-large";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    int numbers;
   
    inputFile >> numbers;
    
    int total = 0;
    int min = 20000000;
    int xor = 0;
    
    for (int i=0; i < numbers; ++i)
    {
      int num;
      inputFile >> num;
      
      total += num;
      xor ^= num;
      
      min = (num < min) ? num : min;
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": ";

    if (xor != 0)
    {
      outputFile << "NO";
    }
    else
    {
      outputFile << (total - min);
    }
    
    outputFile << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

