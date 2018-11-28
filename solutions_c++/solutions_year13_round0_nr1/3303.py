// CodeJam_TicTacToeTomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;
//typedef vector<char> CharArray;
typedef vector<string> TwoDimensionalCharArray;

struct GameStatus
{
   enum status
   {
      xPlayerWon,
      oPlayerWon,
      draw,
      gameHasNotCompleted,
      undefined
   };
};

string GameStatusStrs[4] = {"X won", "O won", "Draw", "Game has not completed"};

void toUpper(string& str)
{
   transform(str.begin(), str.end(),str.begin(), ::toupper);
}

GameStatus::status checkGameStatus(const TwoDimensionalCharArray& arr)
{
   bool hasEmptySquares = false;
   for (int i = 0; i < 4; ++i)
   {
      bool xWonHorizontal = true;
      bool xWonVertical = true;
      bool oWonHorizontal = true;
      bool oWonVertical = true;
      for (int j = 0; j < 4; ++j)
      {
         xWonHorizontal &= arr[i][j] == 'X' || arr[i][j] == 'T';
         xWonVertical &= arr[j][i] == 'X' || arr[j][i] == 'T';
         oWonHorizontal &= arr[i][j] == 'O' || arr[i][j] == 'T';
         oWonVertical &= arr[j][i] == 'O' || arr[j][i] == 'T';
         hasEmptySquares |= arr[i][j] == '.';
      }
      if (xWonHorizontal || xWonVertical)
         return GameStatus::xPlayerWon;
      if (oWonHorizontal || oWonVertical)
         return GameStatus::oPlayerWon;
   }

   bool xWon = true;
   bool oWon = true;
   for (int i = 0; i < 4; ++i)
   {
      xWon &= arr[i][i] == 'X' || arr[i][i] == 'T';
      oWon &= arr[i][i] == 'O' || arr[i][i] == 'T';
   }
   if (xWon)
      return GameStatus::xPlayerWon;
   if (oWon)
      return GameStatus::oPlayerWon;

   xWon = true;
   oWon = true;
   for (int i = 0; i < 4; ++i)
   {
      xWon &= arr[i][3 - i] == 'X' || arr[i][3-i] == 'T';
      oWon &= arr[i][3 - i] == 'O' || arr[i][3-i] == 'T';
   }
   if (xWon)
      return GameStatus::xPlayerWon;
   if (oWon)
      return GameStatus::oPlayerWon;

   if (hasEmptySquares)
      return GameStatus::gameHasNotCompleted;

   return GameStatus::draw;
}

string processTestCase(const TwoDimensionalCharArray& arr)
{
   return GameStatusStrs[checkGameStatus(arr)];
}

int _tmain(int argc, _TCHAR* argv[])
{
   if (argc != 3)
   {
      std::cerr << "Usage: CodeJam_TicTacToeTomek inputFileName outputFileName";
      return -1;
   }
   fstream inputFile(argv[1], fstream::in);
   fstream outputFile(argv[2], fstream::out);

   std::string line;
   getline(inputFile, line);
   int testCasesQty = atoi( line.c_str() );
   int testCasesProcessed = 0;
   while (true)
   {
      TwoDimensionalCharArray testCase;
      for (int i = 0; i < 4; ++i)
      {
         getline(inputFile, line);
         toUpper(line);
         testCase.push_back(line);
      }
      // skip empty line.
      getline(inputFile, line);

      outputFile << "Case #" << ++testCasesProcessed << ": " << processTestCase(testCase);
      if (testCasesProcessed == testCasesQty)
         break;
      else
         outputFile  << '\n';
   }
   return 0;
}

