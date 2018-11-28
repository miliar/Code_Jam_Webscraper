#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
  {
  int T;
  ifstream g("A-large.in");
  //ifstream g("1.txt");
  g >> T;
  char deck[4][4];
  vector<int> res(T);
  bool iscomplete = true,
    xwins = false, owins = false,
    xd1wins = false, od1wins = false,
    xd2wins = false, od2wins = false,
    xrwins = false, orwins = false, 
    xcwins = false, ocwins = false, multer;
  int freerow = 0, freecol = 0;
  for(int i = 0; i < T; ++i)
    {
      iscomplete = true,
      xwins = false, owins = false,
      xd1wins = true, od1wins = true,
      xd2wins = true, od2wins = true,
      multer;
      for(int j = 0; j < 4; ++j)
        for(int k = 0; k < 4; ++k)
          {
          g >> deck[j][k];
          if(deck[j][k] == 'T')
            {
            freerow = (j + 1) % 4;
            freecol = (k + 1) % 4;
            }
          }

      for(int j = 0; j < 4; ++j)
        {
          multer = deck[j][j] == deck[freerow][freerow] || deck[j][j] == 'T';
          xd1wins = xd1wins && multer && deck[freerow][freerow] == 'X';
          od1wins = od1wins && multer && deck[freerow][freerow] == 'O';
        
          multer = deck[j][3 - j] == deck[freerow][3 - freerow] || deck[j][3 - j] == 'T';
          xd2wins = xd2wins && multer && deck[freerow][3 - freerow] == 'X';
          od2wins = od2wins && multer && deck[freerow][3 - freerow] == 'O';

          xrwins = true, orwins = true, 
            xcwins = true, ocwins = true;

        for(int k = 0; k < 4; ++k)
          {
          multer = deck[j][k] == deck[j][freecol] || deck[j][k] == 'T';
          xrwins = xrwins && multer && deck[j][freecol] == 'X';
          orwins = orwins && multer && deck[j][freecol] == 'O';

          multer = deck[k][j] == deck[freerow][j] || deck[k][j] == 'T';
          xcwins = xcwins && multer && deck[freerow][j] == 'X';
          ocwins = ocwins && multer && deck[freerow][j] == 'O';

          if(deck[j][k] == '.')
            iscomplete = false;
          }
        xwins = xwins || xrwins || xcwins;
        owins = owins || orwins || ocwins;
        }
      xwins = xwins || xd1wins || xd2wins;
      owins = owins || od1wins || od2wins;
      if(xwins)
        res[i] = 2;
      else if(owins)
        res[i] = 1;
      else if(iscomplete)
        res[i] = 0;
      else
        res[i] = -1;
    }
  ofstream f("output.txt");
  for(int i = 0; i < T; ++i)
    {
    f << "Case #" << i + 1 << ": ";
    if(res[i] == 2)
      f << "X won\n";
    else if(res[i] == 1)
      f << "O won\n";
    else if(res[i] == 0)
      f << "Draw\n";
    else
      f << "Game has not completed\n";
    }
  }