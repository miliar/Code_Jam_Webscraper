#include <iostream>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

unsigned int map[200][200], h, w;
unsigned int doms[200][200];
char sinks[200][200];

unsigned int owner(unsigned int i, unsigned int j)
{
  unsigned int min = map[i][j];
  unsigned int who=0;
  if(i > 0 && map[i-1][j] < min)
  {
    who = 4; // NORTH
    min = map[i-1][j];
  }
  if(j > 0 && map[i][j-1] < min)
  {
    who = 3; // WEST
    min = map[i][j-1];
  }
  if(j < w-1 && map[i][j+1] < min)
  {
    who = 2; // EAST
    min = map[i][j+1];
  }
  
  if(i < h-1 && map[i+1][j] < min)
  {
    who=1; // SOUTH
    min = map[i+1][j];
  }
  
  return who;
}


void flood(unsigned int i, unsigned int j, char s)
{
  sinks[i][j] = s;
  if(i > 0  && (doms[i-1][j] == 1 || doms[i][j] == 4) && sinks[i-1][j] == ' ')
    flood(i-1, j, s);
  if(i < h-1 &&  (doms[i+1][j] == 4 || doms[i][j] == 1) && sinks[i+1][j] == ' ')
    flood(i+1, j, s);
  if(j > 0 && (doms[i][j-1] == 2 || doms[i][j] == 3) && sinks[i][j-1] == ' ')
    flood(i, j-1, s);
  if(j < w-1 && (doms[i][j+1] == 3 || doms[i][j] == 2) && sinks[i][j+1] == ' ')
    flood(i, j+1, s);
}

void doit(unsigned int n)
{
  unsigned int i, j;
  cin >> h >> w;
  for(i=0;i<h;i++)
  {
    for(j=0;j<w; j++)
    {
      cin >> map[i][j];
    }
  }
  for(i=0;i<h;i++)
  {
    for(j=0;j<w; j++)
    {
      doms[i][j] = owner(i, j);
      sinks[i][j] = ' ';
    }
  }
  char cur = 'a';
  for(i=0;i<h;i++)
  {
    for(j=0;j<w; j++)
    {
      if(sinks[i][j] == ' ')
      {
        flood(i, j, cur);
        cur++;
      }
    }
  }
  cout << "Case #" << n << ":" << endl;
  for(i=0;i<h;i++)
  {
    for(j=0;j<w; j++)
    {
      if(j>0) cout << ' ';
      cout << sinks[i][j];
    }
    cout << endl;
  }

}

int main()
{
  unsigned int n, i;
  cin >> n;

  for(i=0;i<n;i++)
  {
    doit(i+1);
  }

  return 0;
}
