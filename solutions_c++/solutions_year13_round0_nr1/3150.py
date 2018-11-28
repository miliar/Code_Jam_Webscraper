//Google Code Jam 2013
//Problem A
//Nishanth Koganti

#include <stdio.h>
#include <memory.h>
#include <string.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
int checksum(int sum)
{
  switch(sum)
    {
    case 0:
      return -1;
      break;
    case 1:
      return -1;
      break;
    case 7:
      return 1;
      break;
    case 8:
      return 1;
      break;
    default:
      return 0;
    }
}

string checkresult(int result, int nc)
{
  if(result < 0)
    return "O won";
  else if(result > 0)
    return "X won";
  else if(result == 0 && nc == 1)
    return "Game has not completed";
  else if(result == 0 && nc == 0)
    return "Draw";
  else
    return "Sorry";
}

int main(int argc, char** argv)
{
  string line,str;
  stringstream ss;
  ifstream input;
  ofstream output;
  input.open(argv[1]);
  output.open(argv[2]);

  int T;
  int i,j;
  char c;
  int grid[4][4];
  int sum[4];
  int result,nc;

  if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(int t = 0; t < T; t++)
	{
	  for(i = 0; i < 4; i++)
	    {
	      for(j = 0; j < 4; j++)
		{
		  grid[i][j] = 0;
		}
	    }

	  nc = 0;
	  for(i = 0; i < 4; i++)
	    {
	      getline(input,line);
	      ss << line;
	      for(j = 0; j < 4; j++)
		{
		  ss >> c;
		  if(c == '.')
		    {
		      grid[i][j] = 10;
		      nc = 1;
		    }
		  else if(c == 'O')
		    grid[i][j] = 0;
		  else if(c == 'X')
		    grid[i][j] = 2;
		  else if(c == 'T')
		    grid[i][j] = 1;
		}
	      ss.clear();
	    }
	  getline(input,line);

	  result = 0;
	  sum[2] = 0;
	  sum[3] = 0;
	  for(i = 0; i < 4; i++)
	    {
	      sum[0] = 0;
	      sum[1] = 0;
	      for(j = 0; j < 4; j++)
		{
		  sum[0] = sum[0] + grid[i][j];
		  sum[1] = sum[1] + grid[j][i];
		}
	      sum[2] = sum[2] + grid[i][i];
	      sum[3] = sum[3] + grid[3-i][i];
	      result = result + checksum(sum[0]);
	      result = result + checksum(sum[1]);
	    }
	  result = result + checksum(sum[2]);
	  result = result + checksum(sum[3]);
	  str = checkresult(result,nc);
	  output << "Case #" << t+1 << ": " << str << endl;
	}
      input.close();
      output.close();
    }
  
  else
    cout << "Unable to open file";

  return 0;
}
