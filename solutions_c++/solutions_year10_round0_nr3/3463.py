// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <queue>
#include <iostream>

using namespace std;

int R, K, N;

int money;
int available_seats;

inline int get_num(string input, int& end_ix)
{
  end_ix = input.find(' ', 0);

  string R_s = input.substr(0, end_ix);

  return atoi(R_s.c_str());
}

inline void get_RKN(string input)
{
  int end_ix = 0;
  
  R = get_num(input, end_ix);
  
  input = input.substr(end_ix+1);

  K = get_num(input, end_ix);
  
  input = input.substr(end_ix+1);

  N = get_num(input, end_ix);  
}

inline void get_G(string input, queue<int> & groups)
{
  if(N>0)
  {    
    int end_ix =0;
    
    for(int i=0; i<N; ++i)
    {
      groups.push(get_num(input, end_ix));
      
      input = input.substr(end_ix+1);
    }
  }
}

int this_run;

inline void run_it(queue<int> & groups)
{  
  int this_group = groups.front();
  if(this_group<=available_seats)
  {
    groups.pop();
    
    money +=this_group;
    
    available_seats = available_seats - this_group;
        
    groups.push(this_group);

    if(--this_run>0)
      run_it(groups);
  }
}

inline int get_money(string line1, string line2)
{
  money =0;
  
  queue<int> groups;
  
  get_RKN(line1);
  
  get_G(line2, groups);
  
  
  for(int i=0; i<R; ++i)
  {
    available_seats = K;
    this_run=N;
    run_it(groups);
  }
  
  return money;
}

int _tmain(int argc, _TCHAR* argv[])
{  
  int numCases = 0;
  const std::string fileName = "E:\\CodeJam2010\\Q1_input\\C-small-attempt1";

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case
    std::string line1;
    std::getline(inputFile, line1);
    std::string line2;
    std::getline(inputFile, line2);

    // TODO: Process the inputs to get the answer
    // std::string answer = reverse_words(input);
    int answer = get_money(line1, line2);
  
    // Output the results
    outputFile << "Case #" << caseNumber << ": " << answer << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

