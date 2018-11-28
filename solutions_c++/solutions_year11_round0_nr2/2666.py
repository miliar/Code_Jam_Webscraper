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



struct mycombiner 
{
  char ch1;
  char ch2;
  char result;
};

struct mykiller
{
  char ch1;
  char ch2;
  bool ch1_active;
  bool ch2_active;
};

bool combo_match( struct mycombiner combo, char ch1, char ch2)
{
  if ( combo.ch1 == ch1 && combo.ch2 == ch2 )
    return true;

  if ( combo.ch1 == ch2 && combo.ch2 == ch1 )
    return true;
  
  return false;
}

bool killer_match( struct mykiller k, char ch)
{
  if ( k.ch1 == ch && k.ch2_active )
    return true;

  if ( k.ch2 == ch &&  k.ch1_active )
    return true;

  return false;
}


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
    unsigned int numCombines = atoi(input.c_str());
    vector<struct mycombiner> combos;
    std::string word;

    unsigned int c = 0;
    while ( input[c] != ' ')
    {
      word += input[c];
      c++;
    }
    c++;

    while ( combos.size() < numCombines )
    {
      struct mycombiner combo;

      combo.ch1 = input[c++];
      combo.ch2 = input[c++];
      combo.result = input[c++];
      c++;

      combos.push_back(combo);
    }
    
    vector<struct mykiller> killers;
    unsigned int numKillers = atoi(input.c_str()+c);

    while ( input[c] != ' ')
    {
      word += input[c];
      c++;
    }
    c++;

    while ( killers.size() < numKillers )
    {
      struct mykiller k;

      k.ch1 = input[c++];
      k.ch2 = input[c++];
      k.ch1_active = false;
      k.ch2_active = false;
      c++;

      killers.push_back(k);
    }

    vector<char> init_elements;
    unsigned int num_init_elements = atoi(input.c_str()+c);

    while ( input[c] != ' ')
    {
      word += input[c];
      c++;
    }
    c++;

    while ( init_elements.size() <  num_init_elements)
    {
      init_elements.push_back(input[c++]);
    }

    string result = "";

    for ( unsigned int init_element_ix=0; init_element_ix < num_init_elements ; init_element_ix++ )
    {
      // look for combo
      bool element_processed = false;
      // look for active killer
      if (!element_processed ) {
        for ( unsigned int ix = 0 ; ix < killers.size() ; ix++ )
        {
          if ( killer_match( killers[ix], init_elements[init_element_ix]))
          {
            result = "";
            killers[ix].ch1_active = false;
            killers[ix].ch2_active = false;
            element_processed = true;
          }
        }
      }
      if (!element_processed ) {
      for ( unsigned int ix = 0 ; ix < combos.size() ; ix++ )
      {
        if ( init_element_ix+1 < init_elements.size())
        {
          if ( combo_match( combos[ix], init_elements[init_element_ix+1], init_elements[init_element_ix]))
          {
            result.push_back( combos[ix].result );
            init_element_ix++;
            element_processed = true;
          }
        }
      }
      }

      // look for killer to activate
      if ( !element_processed) {
        for ( unsigned int ix = 0 ; ix < killers.size() ; ix++ )
        {
          if ( killers[ix].ch1 ==  init_elements[init_element_ix] && !killers[ix].ch1_active)
          {
            killers[ix].ch1_active = true;  
          }
          if ( killers[ix].ch2 ==  init_elements[init_element_ix] && !killers[ix].ch2_active)
          {
            killers[ix].ch2_active = true;  
          }
        }
      }

      if ( !element_processed )
      {
        result.push_back( init_elements[init_element_ix] );
      }

    }


    // Output the results
    outputFile << "Case #" << caseNumber << ": [" ;
    
    if ( result.size() )
      outputFile << result[0];
    for ( unsigned int cix =1 ; cix < result.size() ; ++cix )
    {
      outputFile << ", "  ;
      outputFile << result[cix]; 
    }
    outputFile << "]\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}
