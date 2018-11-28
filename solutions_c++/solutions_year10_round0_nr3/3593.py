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
  const std::string fileName = "C-small-attempt0";

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
    signed long first_line[3]; 
    int i = 0;
    std::string new_input = input;
    while (( found = new_input.find_first_of(" ")) != std::string::npos)
    {
      input = new_input;
      first_line[i++] =  atoi(input.substr(0, found).c_str());
      new_input = input.substr(found+1, input.size()-1);
    }
    first_line[i] = atoi(new_input.c_str());

    std::getline(inputFile, input);
    new_input = input;
    queue<signed long> groups;
    i = 0;
    while (( found = new_input.find_first_of(" ")) != std::string::npos)
    {
      input = new_input;
      groups.push (atoi(input.substr(0, found).c_str()) );
      new_input = input.substr(found+1, input.size()-1);
    }
    groups.push( atoi(new_input.c_str()) );
    
    signed long output = 0;
    signed long times = 0;
    signed long num_p = 0;
    queue<signed long>done_groups;
    
    while ( times < first_line[0] )
    {
      while ( num_p < first_line[1] )
      { 
        if ( !groups.empty() )
        {
          signed long added_group = groups.front();
          if ( num_p + added_group <= first_line[1] )
          {
            groups.pop();
            num_p += added_group;
            done_groups.push(added_group);
          }
          else
          {
            break;
          }
        }
        else
        {
          break;
        }
      }
      output += num_p;
      num_p=0;
      times++;
      while(!done_groups.empty())
      {
        groups.push(done_groups.front());
        done_groups.pop();
      }
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": " <<  output << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

