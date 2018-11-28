#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
                     //  a    b    c    d    e    f    g    h    i    j    k    l    m
  const char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 
                        'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
                     //  n    o    p    q    r    s    t    u    v    w    x    y    z
  char *cline;

  ifstream input;
  string line;
  int n;

  input.open("A-small-attempt1.in");

  getline(input, line);

  n = atoi(line.c_str());

  for(int i=0; i<n; i++)
  {
    getline(input, line);
    cline = (char *)line.c_str();
    for(int j=0; j<100; j++)
    {
      if(cline[j] == 0)
        break;
      if(cline[j] != ' ')
        cline[j] = map[cline[j]-97];
    }
    printf("Case #%d: %s\n", i+1, cline);
    //cout << "Case #" << i+1 << ": " << gs.ans << endl;
  }
  return 0;
}
