// CodeJam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;


int get_N(string input)
{
  int end_ix = input.find(' ', 0);
  
  string N_s = input.substr(0, end_ix);
  
  return atoi(N_s.c_str());
}

int get_K(string input)
{
  int end_ix = input.find(' ', 0);
  
  string K_s = input.substr(end_ix+1);

  return atoi(K_s.c_str());
}

vector<bool> chain;

void update_chain()
{
  bool connected = true;  
  
  for(int i=0; connected && i<chain.size(); i++)
  {
    if(connected)
    {
      connected = chain[i];
      chain[i] = !chain[i];
    }
  }
}

bool all_power_on()
{
  for(int i=0; i<chain.size(); i++)
  {
    if(chain[i]==false)
    {
      return false;
    }
  }
  
  return true;
}

bool snapper_on_off(string input_line)
{  
  int N = get_N(input_line);
  int K = get_K(input_line);
  
  chain.clear();
  
  for(int i=0; i<N; i++)
  {
    chain.push_back(false);
  }
  
  for(int jump=0; jump<K; jump++)
  {
    update_chain();
  }
  
  return all_power_on();
}

int _tmain(int argc, _TCHAR* argv[])
{  
  //snapper_on_off("");

  int numCases = 0;
  const std::string fileName1_s = "E:\\CodeJam2010\\Q1_input\\A-small-attempt1";
  const std::string fileName1_l = "E:\\CodeJam2010\\Q1_input\\A-large-practice";
  const std::string fileName2_s = "E:\\CodeJam2010\\Q1_input\\B-small-practice";
  const std::string fileName2_l = "E:\\CodeJam2010\\Q1_input\\B-large-practice";
  const std::string fileName3_s = "E:\\CodeJam2010\\Q1_input\\C-small-practice";
  const std::string fileName3_l = "E:\\CodeJam2010\\Q1_input\\C-large-practice";
  
  std::string fileName = fileName1_s;

  std::ifstream inputFile((fileName + ".in").c_str());
  std::ofstream outputFile((fileName + ".out").c_str());

  std::string temp;
  std::getline(inputFile, temp);
  numCases = atoi(temp.c_str());

  for (int caseNumber = 1; caseNumber <= numCases; ++caseNumber)
  {
    // Read the inputs...May be multiple lines of inputs per case
    std::string input;
    std::getline(inputFile, input);

    // TODO: Process the inputs to get the answer
    // std::string answer = reverse_words(input);

    string answer = (snapper_on_off(input))? "ON" : "OFF";
  
    // Output the results
    outputFile << "Case #" << caseNumber << ": " << answer << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}

