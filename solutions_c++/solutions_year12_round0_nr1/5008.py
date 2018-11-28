#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

char translator [255];
void set_translations(){
  translator[' '] = ' ';
  translator['a'] = 'y';
  translator['b'] = 'h';
  translator['c'] = 'e';
  translator['d'] = 's';
  translator['e'] = 'o';
  translator['f'] = 'c';
  translator['g'] = 'v';
  translator['h'] = 'x';
  translator['i'] = 'd';
  translator['j'] = 'u';
  translator['k'] = 'i';
  translator['l'] = 'g';
  translator['m'] = 'l';
  translator['n'] = 'b';
  translator['o'] = 'k';
  translator['p'] = 'r';
  translator['q'] = 'z';
  translator['r'] = 't';
  translator['s'] = 'n';
  translator['t'] = 'w';
  translator['u'] = 'j';
  translator['v'] = 'p';
  translator['w'] = 'f';
  translator['x'] = 'm';
  translator['y'] = 'a';
  translator['z'] = 'q';
}
int main( void ){
  memset(translator,0,255);
  set_translations();
  int num_samples = 0;
  cin >> num_samples;

  char junk [10]; //finish the current line
  cin.getline(junk, 10);

  for(int i = 0; i < num_samples; i++){
    char garbled [2048];
    char english [2048];
    memset(garbled,0,2048);
    memset(english,0,2048);
    cin.getline(garbled, 2048);
    for(int j = 0; j < strlen(garbled); j++){
      english[j] = translator[garbled[j]];
    }
    cout << "Case #" << (i+1) << ": " << english << endl;
  }
}
