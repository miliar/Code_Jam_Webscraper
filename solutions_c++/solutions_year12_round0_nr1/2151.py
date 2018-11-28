#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <map>

using namespace std;


int main (int argc, char * argv[]) {
  map<char,char> googlemap;
  
  googlemap['a'] = 'y';
  googlemap['b'] = 'h';
  googlemap['c'] = 'e';
  googlemap['d'] = 's';
  googlemap['e'] = 'o';
  googlemap['f'] = 'c';
  googlemap['g'] = 'v';
  googlemap['h'] = 'x';
  googlemap['i'] = 'd';
  googlemap['j'] = 'u';
  googlemap['k'] = 'i';
  googlemap['l'] = 'g';
  googlemap['m'] = 'l';
  googlemap['n'] = 'b';
  googlemap['o'] = 'k';
  googlemap['p'] = 'r';
  googlemap['q'] = 'z';
  googlemap['r'] = 't';
  googlemap['s'] = 'n';
  googlemap['t'] = 'w';
  googlemap['u'] = 'j';
  googlemap['v'] = 'p';
  googlemap['w'] = 'f';
  googlemap['x'] = 'm';
  googlemap['y'] = 'a';
  googlemap['z'] = 'q';
  googlemap[' '] = ' ';


  int testcases;
  cin >> testcases;

  for(int i=1; i<=testcases; ++i){

    string message;
    string orig_message;
    getline(cin,orig_message);

    if (orig_message.length() == 0){
      i--;
      continue;
    }

    for(int j=0; j < orig_message.length(); ++j)
      message += googlemap[orig_message[j]];

    cout << "Case #" << i << ": " << message << endl;

  }
}
