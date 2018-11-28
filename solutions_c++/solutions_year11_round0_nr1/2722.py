// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct RobotMove 
{
 char color;
 int position;
};

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
    int buttons_N;
    inputFile >> buttons_N;
    
    vector<RobotMove> moves;
    int time = 0; 
    
    int orange = 1;
    int blue = 1;
        
    int orange_gap = 1;
    int blue_gap = 1;
            
    for (int i = 0; i < buttons_N; ++i)
    {
      RobotMove r;
      inputFile >> r.color >> r.position;

      // time for button push
      time +=1;

      if (r.color == 'O')
      {
        int diff = r.position - orange;
        if (diff < 0) diff *= -1;
        
        if ((time - orange_gap) < diff)
        {
          time = diff + orange_gap;
        }
        
        orange_gap = time + 1;
        orange = r.position;
      }
      
      if (r.color == 'B')
      {
        int diff = r.position - blue;
        if (diff < 0) diff *= -1;

        if ((time - blue_gap) < diff)
        {
          time = diff + blue_gap;
        }
        
        blue_gap = time + 1;
        blue = r.position;
      }


      
    }

              
    int answer = time;

    outputFile << "Case #" << caseNumber << ": " << answer << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

