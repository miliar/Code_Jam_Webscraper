#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <map>

using namespace::std;


int main(void){

  int T;
  map <char,char>m;
  m['a'] = 'y';
  m['b'] = 'h';
  m['c'] = 'e';
  m['d'] = 's';
  m['e'] = 'o';

  m['f'] = 'c';
  m['g'] = 'v';
  m['h'] = 'x';

  m['i'] = 'd';
  m['j'] = 'u';
  m['k'] = 'i';
  m['l'] = 'g';
  m['m'] = 'l';
  m['n'] = 'b';
  m['o'] = 'k';
  m['p'] = 'r';
  m['q'] = 'z';
  m['r'] = 't';
  m['s'] = 'n';
  m['t'] = 'w';
  m['u'] = 'j';
  m['v'] = 'p';
  m['w'] = 'f';
  m['x'] = 'm';
  m['y'] = 'a';
  m['z'] = 'q';




  cin >> T;
  cin.ignore();
  int glen;

  for(int i = 1; i <= T; i++)
    {
      string G;
      getline(cin,G);
      glen = G.size();

      for(int j = 0; j < glen; j++)
	{
	  if(G[j] != ' ')
	  G[j]=m[G[j]];
	}
	  cout << "Case #" << i << ":" << " " << G <<endl;

    }



  return 0;
}
