#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

int main(int argc, char **args)
{
  if (argc == 1)
    return -1;

  string fileName = args[1];
  ifstream input(fileName.c_str());
  ofstream output((fileName.substr(0, fileName.find('.')) + ".out").c_str());

  int numCases;
  input >> numCases;
  for (int caseNum = 0; caseNum < numCases; ++ caseNum)
  {
    int tableSize, sequence;
    input >> tableSize;
    input >> sequence;

    vector<vector<char> > table(tableSize, vector<char>(tableSize, '.'));
    for (int row = 0; row < tableSize; ++row)
    {
      for (int col = 0; col < tableSize; ++col)
        input >> table[row][col];

      int rightMost = tableSize - 1;
      while (rightMost > 0 && table[row][rightMost] != '.')
        --rightMost;
      if (rightMost > 0)
      {
        for (int i = rightMost; --i >= 0;)
        {
          if (table[row][i] != '.')
          {
            table[row][rightMost--] = table[row][i];
            table[row][i] = '.';
          }
        }
      }
    }

    bool red = false, blue = false;
    int redR, redC, blueR, blueC;
    for (int i = tableSize; --i >= 0;)
    {
      redR = redC = blueR = blueC = 0;
      for (int j = tableSize; --j >= 0;)
      {
        if (table[i][j] == '.')
          continue;

        if (j - (sequence - 1) >= 0)
        {
          int x = 0;
          while (x < sequence - 1 && table[i][j] == table[i][j - x - 1]) ++x;
          if (x == sequence - 1)
          {
            if (table[i][j] == 'R')
              red = true;
            else if (table[i][j] == 'B')
              blue = true;
          }
        }

        if (i - (sequence - 1) >= 0)
        {
          int x = 0;
          while (x < sequence - 1 && table[i][j] == table[i - x - 1][j]) ++x;
          if (x == sequence - 1)
          {
            if (table[i][j] == 'R')
              red = true;
            else if (table[i][j] == 'B')
              blue = true;
          }
        }

        if (j - (sequence - 1) >= 0 && i - (sequence - 1) >= 0)
        {
          int x = 0;
          while (x < sequence - 1 && table[i][j] == table[i - x - 1][j - x - 1]) ++x;
          if (x == sequence - 1)
          {
            if (table[i][j] == 'R')
              red = true;
            else if (table[i][j] == 'B')
              blue = true;
          }
        }

        if (j + (sequence - 1) < tableSize && i - (sequence - 1) >= 0)
        {
          int x = 0;
          while (x < sequence - 1 && table[i][j] == table[i - x - 1][j + x + 1]) ++x;
          if (x == sequence - 1)
          {
            if (table[i][j] == 'R')
              red = true;
            else if (table[i][j] == 'B')
              blue = true;
          }
        }

        if (red && blue)
          break;
        /*if (!red)
        {
          if (table[i][j] == 'R')
          {
            if (++redR >= sequence)
            {
              red = true;
              if (blue)
                break;
            }
          }
          else
            redR = 0;

          if (table[j][i] == 'R')
          {
            if (++redC >= sequence)
            {
              red = true;
              if (blue)
                break;
            }
          }
          else
            redC = 0;
        }
        if (!blue)
        {
          if (table[i][j] == 'B')
          {
            if (++blueR >= sequence)
            {
              blue = true;
              if (red)
                break;
            }
          }
          else
            blueR = 0;

          if (table[j][i] == 'B')
          {
            if (++blueC >= sequence)
            {
              blue = true;
              if (red)
                break;
            }
          }
          else
            blueC = 0;
        }*/
      }
    }

    string result;
    if (red && blue)
      result = "Both";
    else if (!red && !blue)
      result = "Neither";
    else if (blue)
      result = "Blue";
    else
      result = "Red";

    stringstream caseResult;
    caseResult << "Case #" << caseNum + 1 << ": " << result;
    output << caseResult.str() << endl;
    cout << caseResult.str() << endl;
  }
  
  return 0;
}
