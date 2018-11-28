#include <iostream>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

char look[] = "welcome to code jam";
char line[600];
unsigned int results1[600], results2[600];

void doit(unsigned int n)
{
  cin.getline(line, 599);
  int i, at, c;
  unsigned int *cur, *tmp, *prev;

  cur = results1;
  prev = results2;

  for(i=0; i < strlen(line); i++)
  {
    prev[i] = (line[i] == look[0]) ? 1 : 0;
  }
  
  for(at=1;at < strlen(look); at++)
  {
    c = 0;
    for(i=0; i < strlen(line); i++)
    {
      if(line[i] == look[at])
        cur[i] = c;
      else
        cur[i]= 0;
      if(line[i] == look[at-1])
      {
        c += prev[i];
        c = c % 10000;
      }
    }
    tmp = prev;
    prev = cur;
    cur = tmp;
  }
  c = 0;
  for(i = 0; i < strlen(line); i++)
  {
    c += prev[i];
    c = c % 10000;
  }
  cout << "Case #" << n << ": ";
  if(c < 1000) cout << 0;
  if(c < 100) cout << 0;
  if(c < 10) cout << 0;
  cout << c << endl;
}

int main()
{
  unsigned int n, i;
  cin >> n;
  cin.ignore();

  for(i=0;i<n;i++)
  {
    doit(i+1);
  }

  return 0;
}
