#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

#define X 0
#define O 1

#define R 0
#define C 1
#define D 2

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);
  map<int, string> status;

  status[0] = "Game has not completed";
  status[1] = "X won";
  status[2] = "O won";
  status[3] = "Draw";
  if (inFile.good())
  {
    int nCases;
    string strLine;
    inFile >> nCases;
    for (int n = 0; n < nCases; n++)
    {
      bool bFoundDot = false;
      int nResult = 0, result[2][3][4];
      getline(inFile, strLine);
      for (int i = 0; i < 4; i++)
      {
        result[0][0][i] = result[0][1][i] = result[0][2][i] = result[1][0][i] = result[1][1][i] = result[1][2][i] = 0;
      }
      for (int r = 0; r < 4; r++)
      {
        getline(inFile, strLine);
        if (nResult == 0)
        {
          for (int c = 0; c < 4; c++)
          {
            if (strLine[c] == '.')
            {
              bFoundDot = true;
            }
            else
            {
              if (strLine[c] == 'X' || strLine[c] == 'T')
              {
                if (++result[X][R][r] == 4 || ++result[X][C][c] == 4 || (r == c && ++result[X][D][0] == 4) || (r + c == 3 && ++result[X][D][1] == 4))
                {
                  nResult = X + 1;
                }
              }
              if (strLine[c] == 'O' || strLine[c] == 'T')
              {
                if (++result[O][R][r] == 4 || ++result[O][C][c] == 4 || (r == c && ++result[O][D][0] == 4) || (r + c == 3 && ++result[O][D][1] == 4))
                {
                  nResult = O + 1;
                }
              }
            }
          }
        }
      }
      cout << "Case #" << (n + 1) << ": " << ((nResult == 0)?((bFoundDot)?status[0]:status[3]):status[nResult]) << endl;
    }
  }
  status.clear();
  inFile.close();

  return 0;
}
