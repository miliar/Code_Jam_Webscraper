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
/*
bool mycomp( const int& d1, const int& d2 )
{
  return d1 < d2;
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
    // Read the inputs...May be multiple lines of inputs per case
    std::string input;
    std::getline(inputFile, temp);
    int numCredits = atoi(temp.c_str());

    std::getline(inputFile, temp);
    int numItems = atoi(temp.c_str());


    std::getline(inputFile, input);
    std::map<int, vector<int>> pricemap;
    std::vector<int> prices;

    std::string word;
    int itemcd = 0;

    for ( unsigned int c = 0 ; c < input.length() ; ++c )
    {
      if ( input[c] == ' ')
      {
        int price = atoi(word.c_str());
        pricemap[price].push_back( itemcd );
        prices.push_back( price );
        itemcd++;
        word = "";
      }
      else
      {
        word += input[c];
      }
    }

    int price = atoi(word.c_str());
    pricemap[price].push_back( itemcd );
    prices.push_back( price );
    itemcd++;

    int itemOne = -1;
    int itemTwo = -1;

    for ( int ix=0; ix < numItems; ix++ )
    {
      int otherprice = numCredits - prices[ix];
      if ( pricemap.count( otherprice ) > 0 )
      {
        bool ok = true;

        if ( otherprice == prices[ix] )
          ok = pricemap[otherprice].size() > 1;
        
        if ( ok )
        {
          itemOne = ix;
          itemTwo = pricemap[otherprice][0];  

          if ( itemOne == itemTwo )
            itemTwo = pricemap[otherprice][1];  

          break;
        }
      }
    }

    // Output the results
    outputFile << "Case #" << caseNumber << ": " << itemOne+1 << " " << itemTwo+1 << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}
*/


bool mycomp( const int& d1, const int& d2 )
{
  return d1 < d2;
}

struct destination 
{
  bool orange;
  int  door;
};
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
    unsigned int numItems = atoi(input.c_str());
    vector<struct destination> dests;
    vector<int> odests;
    vector<int> bdests;

    std::string word;

    unsigned int c = 0;
    while ( input[c] != ' ')
    {
      word += input[c];
      c++;
    }
    c++;
    while ( dests.size() < numItems )
    {
      struct destination dest;

      dest.orange = input[c] == 'O';
      c += 2;

      word = "";
      while ( c < input.size() && input[c] != ' ')
      {
        word += input[c];
        c++;
      }
      c++;
      dest.door = atoi(word.c_str());

      dests.push_back( dest );
      if ( dest.orange)
        odests.push_back( dest.door );
      else
        bdests.push_back( dest.door );
    }

    odests.push_back( 1 );
    bdests.push_back( 1 );

    int orange_locn = 1;
    int blue_locn = 1;
    int num_moves = 0;
    unsigned int next_orange_dest_ix = 0;
    unsigned int next_blue_dest_ix = 0;

    for ( unsigned int destnum = 0 ; destnum < dests.size() ;  )
    {
      if ( dests[destnum].orange && orange_locn == dests[destnum].door )
      {
        if ( bdests[next_blue_dest_ix] > blue_locn )
        {
          blue_locn++;
        }
        else if ( bdests[next_blue_dest_ix] < blue_locn )
        {
          blue_locn--;
        }
        num_moves++;
        next_orange_dest_ix++;
        destnum++;
      }

      else if ( !dests[destnum].orange && blue_locn == dests[destnum].door )
      {
        if ( odests[next_orange_dest_ix] > orange_locn )
        {
          orange_locn++;
        }
        else if ( odests[next_orange_dest_ix] < orange_locn )
        {
          orange_locn--;
        }
        num_moves++;
        next_blue_dest_ix++;
        destnum++;
      }

      else
      {
        if ( odests[next_orange_dest_ix] > orange_locn )
        {
          orange_locn++;
        }
        else if ( odests[next_orange_dest_ix] < orange_locn )
        {
          orange_locn--;
        }
        if ( bdests[next_blue_dest_ix] > blue_locn )
        {
          blue_locn++;
        }
        else if ( bdests[next_blue_dest_ix] < blue_locn )
        {
          blue_locn--;
        }
        num_moves++;
      }
    }


    // Output the results
    outputFile << "Case #" << caseNumber << ": " << num_moves << "\n";
  }

  // Close the streams
  inputFile.close();
  outputFile.close();

  return 0;
}
