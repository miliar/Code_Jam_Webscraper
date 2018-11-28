#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <memory.h>
#include <set>
#include <map>
#include <vector>
#include <list>


using namespace std;

typedef int byte;

string INPUT_NAME = "domino.in";
string OUTPUT_NAME = "domino.out";

byte dx[4] = {0,-1,1,0};
byte dy[4] = {-1,0,0,1};

int n,m,k;

short int height[100][100];
byte sinkX[100][100];
byte sinkY[100][100];
char name[100][100];


void dfs(byte x, byte y)
{
    if (sinkX[y][x] != -1)
	return;

    short int lowest = 20000;
    for (int i = 0; i < 4; i++)
    {
	byte cx = x + dx[i];
	byte cy = y + dy[i];
	
	if (cx >= 0 && cx < m && cy >= 0 && cy < n)
	{
	     lowest = min(lowest, height[cy][cx]);
	}
    }
    cout << x << ' ' << y << ' ' << lowest << '\n';
	
	
    sinkX[y][x] = x;
    sinkY[y][x] = y;
    for (int i = 0; i < 4; i++)
    {
	byte cx = x + dx[i];
	byte cy = y + dy[i];
	if (cx >= 0 && cx < m && cy >= 0 && cy < n && lowest == height[cy][cx])
	{
	    cout << x << ' ' << y << ' ' << cx << ' ' << cy << '\n';	    
	    dfs(cx, cy);
	    sinkX[y][x] = sinkX[cy][cx];
	    sinkY[y][x] = sinkY[cy][cx];
	    return;
	}
    }
}

void clean()
{
    for (int i = 0; i < n; i++)
	for (int j = 0; j < m; j++)
	{
	    name[i][j] = 0;
	    sinkX[i][j] = sinkY[i][j] = -1;
	}
}


    
int main(int argn, char** args)
{
  string ainput;
  string aoutput;
  if (argn > 1 && strcmp(args[1],"HOME") == 0)
    {
      ainput = "input.txt";
      aoutput = "output.txt";
    }
  else
    {
      ainput = INPUT_NAME;
      aoutput = OUTPUT_NAME;
    }
  ifstream fin(ainput.c_str());
  ofstream fout(aoutput.c_str());

  fin >> k;
  for (int kk = 0; kk < k; kk++)
  {
      fin >> n >> m;
      for (int i = 0; i < n; i++)
	  for (int j = 0; j < m; j++)
	      fin >> height[i][j];
      clean();
      fout << "Case :" << kk + 1 << '\n';
      char let = 'a';
      for (int i = 0; i < n; i++)
      {
	  for (int j = 0; j < m; j++)
	  {
	      if (sinkX[i][j] == -1)
	   	  dfs(j,i);
	      int x = sinkX[i][j];
	      int y = sinkY[i][j];
	      if (name[y][x] == 0)
		  name[y][x] = let++;
	      fout << name[y][x] << ' ';
	  }
	  fout << '\n';
      }
  }
  return 0;
}
