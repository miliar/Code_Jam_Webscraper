// CodeJam2011.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class QuestionA
{
  private:
    bool possible;
    map<int, int> minNumWon;
  public:
    QuestionA()
    {
    }

    void process(int maxNum, int todayPercent, int totalPercent)
    {
      possible = do_percents_work(todayPercent, totalPercent) && is_wins_possible(todayPercent, maxNum);
    }

    bool do_percents_work(int today, int total)
    {
      if( today == 0)
      {
        return total < 100;
      }
      else if( today == 100 )
      {
        return total > 0;
      }
      else
      {
        return total < 100 && total > 0;
      }
    }

    bool is_wins_possible(int percent, int MaxNum)
    {
      auto iter = minNumWon.find(percent);
      if(iter != minNumWon.end())
      {
        return iter->second <= MaxNum;
      }
      else
      {
        for(int i = 1 ; i <= MaxNum ; i ++)
        {
          if((i * percent % 100) == 0)
          {
            minNumWon.insert(pair<int, int>(percent, i));
            return true;
          }
        }
      }
    }

    string print()
    {
      if(possible)
      {
        return "Possible";
      }
      else
      {
        return "Broken";
      }
    }
};

int _tmain(int argc, _TCHAR* argv[])
{
  int numCases = 0;
  const string fileName = "..\\data\\A-small-attempt1";
  int N, Pd, Pg;
  QuestionA* answer;
  
  ifstream inputFile((fileName + ".in").c_str());
  ofstream outputFile((fileName + ".out").c_str());
    
  string temp;
  getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    answer = new QuestionA();
    // Read the inputs...May be multiple lines of inputs per case
    inputFile >> skipws >> N >> Pd >> Pg ;

    answer->process(N, Pd, Pg);

    // Output the results
    outputFile << "Case #" << caseNumber << ": " << answer->print() << endl;
    delete answer;
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

