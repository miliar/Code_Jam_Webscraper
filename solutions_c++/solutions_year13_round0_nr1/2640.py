#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

#define PI M_PI

double dist(int x, int y)
{
  return sqrt(x*x+y*y);
}

int main()
{
  ifstream input;
  string line;
  char *tstr;
  int T;

  int grid[4][4];
  
  int i, j;
  int won;
  int zeros;
  int lleft;
  int bleft;
  
  int hh, vv;
  int d1, d2;

  //input.open("sample.in");
  input.open("A-large.in");

  getline(input, line);

  T = atoi(line.c_str()); /* 1 <= T <= 1000 */

  for(int run=1; run<=T; run++)
  {
	zeros = 0;

    for(i=0; i<4; i++)
    {
      getline(input, line);

      tstr = (char *)line.c_str();
      for(j=0; j<4; j++)
      {
        // Rudimentary copy!
        // grid[i][j] = tstr[j];
            
        switch(tstr[j])
        {
			case 'T': grid[i][j] = 30; break;
			case 'X': grid[i][j] = 5;  break;
			case 'O': grid[i][j] = 6;  break;
			case '.': grid[i][j] = 0;  
  		              zeros++;         break;
	    }
      }
    }
    
    getline(input, line);

	won = 0;
    
    for(i=0; i<4; i++)
    {
		hh=0; vv=0; won=0;
		for(j=0; j<4; j++)
		{
			hh += grid[i][j];
			vv += grid[j][i];
		}
		if((hh == 20) || (hh == 45) || (vv == 20) || (vv == 45))
		{
			cout << "Case #" << run << ": X won" <<endl;
			won = 1;
			break;
		}
		else if((hh == 24) || (hh == 48) || (vv == 24) || (vv == 48))
		{
			cout << "Case #" << run << ": O won" <<endl;
			won = 1;
			break;
		}
	}
	if(won==0)
	{
		d1=0; d2=0;
		for(i=0; i<4; i++)
		{
			d1+=grid[i][i];
			d2+=grid[i][3-i];
		}
		if((d1 == 20) || (d1 == 45) || (d2 == 20) || (d2 == 45))
		{
			cout << "Case #" << run << ": X won" <<endl;
			won = 1;
		}
		else if((d2 == 24) || (d2 == 48) || (d1 == 24) || (d1 == 48))
		{
			cout << "Case #" << run << ": O won" <<endl;
			won = 1;
		}
	}
	if(won==0)
	{
		if(zeros>0)
		{
			cout << "Case #" << run << ": Game has not completed" <<endl;
		}
		else
		{
			cout << "Case #" << run << ": Draw" <<endl;
		}
	}
  }
  return 0;
}
