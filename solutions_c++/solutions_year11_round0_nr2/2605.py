// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <map>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const std::string fileName = "B-small-attempt0";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    int combine_C;
    int oppose_D;
    
    map<string,string> combinations;
        
    inputFile >> combine_C;
    for (int i = 0; i < combine_C; ++i)
    {
      string combine;
      
      inputFile >> combine;
      
      string key = combine.substr(0, 2);
      string val = combine.substr(2 ,1);

      //string key = ;
      
      combinations[key] = val;
    }

    inputFile >> oppose_D;
    for (int i = 0; i < oppose_D; ++i)
    {
      string combine;

      inputFile >> combine;

      string key = combine.substr(0, 1);
      string val = combine.substr(1 ,1);

      combinations[key] = val;
      combinations[val] = key;
    }

    int casts;
    string cast_sequence;
    inputFile >> casts >> cast_sequence;

    std::string answer;

    for (int i = 0; i < casts; ++i)
    {
      char c = cast_sequence.at(i);
      answer.append(1, c);
      
      if (answer.length() > 1)    
      {
        string key = answer.substr(answer.length()-2,  2);
        map<string,string>::const_iterator iter = combinations.find(key);
        if (iter != combinations.end())
        {
          string val = iter->second;
          answer.erase(answer.length()-2);
          answer.append(val);
        }
        else
        {
          char c0 = key.at(0);
          char c1 = key.at(1);
          key[0] = c1;
          key[1] = c0;
          
          map<string,string>::const_iterator iter = combinations.find(key);
          if (iter != combinations.end())
          {
            string val = iter->second;
            answer.erase(answer.length()-2);
            answer.append(val);
          }
          else
          {
            string k = string(1, c);
            map<string,string>::const_iterator iter = combinations.find(k);
            if (iter != combinations.end())
            {
              if (string::npos != answer.find_last_of(iter->second, answer.length()-2))
              {
                answer = "";
              }
            }
          }
        }
      }
      
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": [";
    
    if (answer != "")
    {
      outputFile << answer.at(0);
      for (int i = 1; i < answer.length(); ++i)
      {
        outputFile << ", " << answer.at(i);
      }
    }
        
    outputFile << "]\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

