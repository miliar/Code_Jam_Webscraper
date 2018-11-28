// 2011practicejam1-storecredit.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;



int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const std::string fileName = "input";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    std::string input;

    std::getline(inputFile, input);
    unsigned int numCandies = atoi(input.c_str());

    std::getline(inputFile, input);
    unsigned int c = 0;

    unsigned int xorcandy = 0;
    unsigned int sumcandy = 0;
    unsigned int smallestcandy = 0xffffffff;
    std::string word;

    while ( c < input.size() )
    {
      word = "";
      while ( c < input.size() && input[c] != ' ')
      {
        word += input[c];
        c++;
      }
      c++;
      unsigned int candy = atoi(word.c_str());

      xorcandy ^= candy;
      sumcandy += candy;
      if (candy < smallestcandy )
        smallestcandy = candy;
   }
    

    // Output the results
    if ( xorcandy )
      outputFile << "Case #" << caseNumber << ": NO\n" ;
    else
      outputFile << "Case #" << caseNumber << ": " << sumcandy-smallestcandy << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}
