///////////////////////////////////////////////////////////////////////////////////////////////////
//
// Problem: Tic-Tac-Toe-Tomek
//
//Case #1: X won
//Case #2: O won
//Case #3: Game has not completed
//Case #4: Draw
//
///////////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;

char board[4][4];
            // XXXT
            // ....
            // OO..
            // ....

string CalculateResult()
{
   int resRow[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
   int iPass = 0;
   
   while (iPass < 4) {
      char firstCharR = board[iPass][iPass]; // used for comparison in Row
      char firstCharC = board[iPass][iPass]; // used for comparison in Col

      // Skip checking matches if first character is '.'
      if (firstCharR == '.') {
         ++iPass;
         continue;
      }

      // Check the row matches
      for (int iCtr = 1; iCtr < 4; ++iCtr) {
         int iCol = (iPass + iCtr) % 4;
         char nextChar = board[iPass][iCol];

         if (nextChar == '.') {
            break;
         }

         if (firstCharR == 'T') {
            firstCharR = nextChar;
            continue;
         }

         if (nextChar != firstCharR && nextChar != 'T') {
            resRow[iPass] = 0;
            break;
         } else {
            if (iCtr == 3) {
               if (firstCharR == 'X')
                  return "X won";
               else
                  return "O won";
            }
         }
      }

      // Check the col matches
      for (int iCtr = 1; iCtr < 4; ++iCtr) {
         int iRow = (iPass + iCtr) % 4;
         char nextChar = board[iRow][iPass];

         if (nextChar == '.') {
            break;
         }

         if (firstCharC == 'T') {
            firstCharC = nextChar;
            continue;
         }

         if (nextChar != firstCharC && nextChar != 'T') {
            resRow[iPass+4] = 0;
            break;
         } else {
            if (iCtr == 3) {
               if (firstCharC == 'X')
                  return "X won";
               else
                  return "O won";            }
         }
      }

      ++iPass;
   }

   // CheckFirstDiagPass();
   char firstChar = board[0][0];

   // Skip checking matches if first character is '.', continue otherwise
   if (firstChar != '.') {
      for (int iCtr = 1; iCtr < 4; ++iCtr) {
         char nextChar = board[iCtr][iCtr];

         if (nextChar == '.') {
            break;
         }

         if (firstChar == 'T') {
            firstChar = nextChar;
            continue;
         }

         if (nextChar != firstChar && nextChar != 'T') {
            resRow[8] = 0;
            break;
         } else {
            if (iCtr == 3) {
               if (firstChar == 'X')
                  return "X won";
               else
                  return "O won";
            }
         }
      }
   }

   //CheckSecondDiagPass();
   firstChar = board[0][3];

   // Skip checking matches if first character is '.', continue otherwise
   if (firstChar != '.') {
      for (int iCtr = 1; iCtr < 4; ++iCtr) {
         char nextChar = board[iCtr][3 - iCtr];

         if (nextChar == '.') {
            break;
         }

         if (firstChar == 'T') {
            firstChar = nextChar;
            continue;
         }

         if (nextChar != firstChar && nextChar != 'T') {
            resRow[9] = 0;
            break;
         } else {
            if (iCtr == 3) {
               if (firstChar == 'X')
                  return "X won";
               else
                  return "O won";
            }
         }
      }
   }

   int i = 0;
   string strResult = "Draw";
   for (; i < 10; ++i) {
      if (resRow[i] != 0) {
         strResult = "Game has not completed";
         break;
      }
   }

   return strResult;
}

int main()
{
   string l_inFileName = "./A-small-attempt0.in";
   string l_outFileName = "./A-small-attempt0.out";
   ifstream l_inFilesStream;
   ofstream l_outFileStream;

   l_inFilesStream.open(l_inFileName.c_str());
   l_outFileStream.open(l_outFileName.c_str());

   if (l_inFilesStream && l_outFileStream)
   {
      if (!l_inFilesStream.eof())
      {
         string l_strNumTestCases;
         int l_numTestCases = -1;

         getline(l_inFilesStream, l_strNumTestCases);

         l_numTestCases = atoi(l_strNumTestCases.c_str());

         // Run each test case
         for (int l_itest = 0; l_itest < l_numTestCases; ++l_itest)
         {
            // XXXT
            // ....
            // OO..
            // ....

            for (int r = 0; r < 4; ++r) {
               string strLineRead;
               getline(l_inFilesStream, strLineRead);

               for (int c = 0; c < 4; ++c) {
                  board[r][c] = strLineRead[c];
               }
            }

            string strResult = CalculateResult();

            l_outFileStream << "Case #" << (l_itest+1) << ": " << strResult << endl;
            cout << "Case #" << (l_itest+1) << ": " << strResult << endl;

            getline(l_inFilesStream, string());
         }
      }
      else
      {
         cout << "File is empty" << endl;
      }
   }
   else
   {
      if (!l_inFilesStream)
         cout << "Input file couldn't be opened" << endl;
      else
         cout << "Output file couldn't be opened" << endl;

      return -1;
   }

   return 0;
}
