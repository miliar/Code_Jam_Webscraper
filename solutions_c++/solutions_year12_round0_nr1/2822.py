#include <iostream>

#include <vector>
#include <cstdio> 

#define REP(i, to) for(int i=0; i<to; i++)
typedef long long int LLI;

using namespace std; 

char D[256];

int main()
{
  D[' ']=' ';
  D['a']='y';
  D['b']='h';
  D['c']='e';
  D['d']='s';
  D['e']='o';
  D['f']='c';
  D['g']='v';
  D['h']='x';
  D['i']='d';
  D['j']='u';
  D['k']='i';
  D['l']='g';
  D['m']='l';
  D['n']='b';
  D['o']='k';//kq
  D['p']='r';
  D['q']='z';
  D['r']='t';
  D['s']='n';
  D['t']='w';
  D['u']='j';
  D['v']='p';
  D['w']='f';
  D['x']='m';
  D['y']='a';
  D['z']='q';//kq

  int N;
  string s;
  cin >> N;
  getline(cin, s);
  REP(i, N) {
    getline(cin, s); 
    REP(j, s.size()) s[j] = D[s[j]];
    cout << "Case #" << i + 1 << ": " << s << endl;
  }

	return 0;
}
