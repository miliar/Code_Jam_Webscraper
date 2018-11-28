#include <signal.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
#include <stdarg.h>

#include <limits>
#include <ostream>
#include <istream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>
#include <numeric> 
#include <memory>

std::set<std::string> XWinPatterns;
std::set<std::string> OWinPatterns;

void SetupWinPatterns()
{
     XWinPatterns.insert(std::string("XXXX"));
     XWinPatterns.insert(std::string("XXXT"));
     XWinPatterns.insert(std::string("XXTX"));
     XWinPatterns.insert(std::string("XTXX"));
     XWinPatterns.insert(std::string("TXXX"));

     OWinPatterns.insert(std::string("OOOO"));
     OWinPatterns.insert(std::string("OOOT"));
     OWinPatterns.insert(std::string("OOTO"));
     OWinPatterns.insert(std::string("OTOO"));
     OWinPatterns.insert(std::string("TOOO"));
}


bool WinnerLine(const std::string& l, const std::set<std::string>& p)
{
     return p.find(l) != p.end();
}

bool XLine(const std::string& l)
{
     return WinnerLine(l, XWinPatterns);
}

bool OLine(const std::string& l)
{
     return WinnerLine(l, OWinPatterns);
}


typedef enum {XWON = 0, OWON = 1, DRAW = 2, INCOMPLETE = 3} RESULT;

void result(RESULT r, int Case)
{
     printf("Case #%d: ", Case);
     switch (r)
     {
     case XWON:
	  printf("X won\n");
	  break;
     case OWON:
	  printf("O won\n");
	  break;
     case DRAW:
	  printf("Draw\n");
	  break;
     case INCOMPLETE:
	  printf("Game has not completed\n");
	  break;	  
     }
}



void ProcessInput(int CaseNumber)
{
     std::string Lines[5];
     bool HasEmpty = false;

     RESULT r = INCOMPLETE;

     for (int i = 0; i < 5; i++)
     {
	  std::string& l = Lines[i];
	  std::getline(std::cin, l);
	  if (l.find_first_of('.') != std::string::npos)
	  {
	       HasEmpty = true;
	  }
	  if (OLine(l)) r = OWON;
	  if (XLine(l)) r = XWON;
     }
     if (r == OWON || r == XWON)
     {
	  result(r, CaseNumber);
	  return;
     }
     
     std::string diag = "    ";
     diag[0] = Lines[0][0];
     diag[1] = Lines[1][1];
     diag[2] = Lines[2][2];
     diag[3] = Lines[3][3];

     if (OLine(diag))
     {
	  result(OWON, CaseNumber);
	  return;
     }

     if (XLine(diag))
     {
	  result(XWON, CaseNumber);
	  return;
     }

     diag[0] = Lines[0][3];
     diag[1] = Lines[1][2];
     diag[2] = Lines[2][1];
     diag[3] = Lines[3][0];
     

     if (OLine(diag))
     {
	  result(OWON, CaseNumber);
	  return;
     }

     if (XLine(diag))
     {
	  result(XWON, CaseNumber);
	  return;
     }

     std::string vert = "    ";     
     for (int i = 0; i < 4; i++)
     {
	  vert[0] = Lines[0][i];
	  vert[1] = Lines[1][i];
	  vert[2] = Lines[2][i];
	  vert[3] = Lines[3][i];
	  if (OLine(vert))
	  {
	       result(OWON, CaseNumber);
	       return;
	  }
	  
	  if (XLine(vert))
	  {
	       result(XWON, CaseNumber);
	       return;
	  }
     }

     
     if (!HasEmpty)
     {
	  result(DRAW, CaseNumber);
	  return;
     }
     result(INCOMPLETE, CaseNumber);
}


int main()
{
     SetupWinPatterns();
     int Cases;
     std::cin >> Cases;
     getchar();
     for (int i = 1; i <= Cases; i++)
	  ProcessInput(i);
     return 0;
}
