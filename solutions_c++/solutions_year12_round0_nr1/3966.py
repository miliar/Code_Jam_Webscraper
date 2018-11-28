#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>

using namespace std;

int main()
{
  int t;
  cin>>t;
  string cadena;
  map <char,char> m;
  map <char,char>:: iterator i;
  getline(cin,cadena);

m['e'] = 'o';
m['j'] = 'u';
m['p'] = 'r';
m['m'] = 'l';
m['y'] = 'a';
m['s'] = 'n';
m['l'] = 'g';
m['j'] = 'u';
m['y'] = 'a';
m['l'] = 'g';
m['c'] = 'e';
m['k'] = 'i';
m['d'] = 's';
m[' '] = ' ';
m['k'] = 'i';
m['x'] = 'm';
m['v'] = 'p';
m['e'] = 'o';
m['d'] = 's';
m['d'] = 's';
m['k'] = 'i';
m['n'] = 'b';
m['m'] = 'l';
m['c'] = 'e';
m['r'] = 't';
m['e'] = 'o';
m['j'] = 'u';
m['s'] = 'n';
m['i'] = 'd';
m['c'] = 'e';
m['p'] = 'r';
m['d'] = 's';
m['r'] = 't';
m['y'] = 'a';
m['s'] = 'n';
m['i'] = 'd';
m['r'] = 't';
m['b'] = 'h';
m['c'] = 'e';
m['p'] = 'r';
m['c'] = 'e';
m['y'] = 'a';
m['p'] = 'r';
m['c'] = 'e';
m['r'] = 't';
m['t'] = 'w';
m['c'] = 'e';
m['s'] = 'n';
m['r'] = 't';
m['a'] = 'y';
m['d'] = 's';
m['k'] = 'i';
m['h'] = 'x';
m['w'] = 'f';
m['y'] = 'a';
m['f'] = 'c';
m['r'] = 't';
m['e'] = 'o';
m['p'] = 'r';
m['k'] = 'i';
m['y'] = 'a';
m['m'] = 'l';
m[' '] = ' ';
m['v'] = 'p';
m['e'] = 'o';
m['d'] = 's';
m['d'] = 's';
m['k'] = 'i';
m['n'] = 'b';
m['k'] = 'i';
m['m'] = 'l';
m['k'] = 'i';
m['r'] = 't';
m['k'] = 'i';
m['c'] = 'e';
m['d'] = 's';
m['d'] = 's';
m['e'] = 'o';
m['k'] = 'i';
m['r'] = 't';
m['k'] = 'i';
m['d'] = 's';
m['e'] = 'o';
m['o'] = 'k';
m['y'] = 'a';
m['a'] = 'y';
m['k'] = 'i';
m['w'] = 'f';
m['a'] = 'y';
m['e'] = 'o';
m['j'] = 'u';
m['t'] = 'w';
m['y'] = 'a';
m['s'] = 'n';
m['r'] = 't';
m['r'] = 't';
m['e'] = 'o';
m['u'] = 'j';
m['j'] = 'u';
m['d'] = 's';
m['r'] = 't';
m['l'] = 'g';
m['k'] = 'i';
m['g'] = 'v';
m['c'] = 'e';
m['j'] = 'u';
m['v'] = 'p';
m['q'] = 'z';
m['z'] = 'q';
  for(int c=0;c<t;c++)
  {
      getline(cin,cadena);


  for(int c=0;c<cadena.size();c++)
  {
      if(cadena.at(c)!=' ')
      cadena.at(c)=m[cadena.at(c)];

  }
  cout<<"Case #"<<c+1<<": "<<cadena<<endl;
  cadena.clear();


  }




}
