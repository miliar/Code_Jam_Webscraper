/* 
 * File:   src.cxx
 * Author: mechanic
 */

#ifndef SRC
#define	SRC

#include <iostream>
#include <cstdlib>
#include <cstring>
#include "inClass.cxx"
#include "outClass.cxx"
using namespace std;

char casesZ(char*);
char trnaslate(char);

char* a_in;
unsigned len;

void Speak(char ini[20]){
  void in_read(char in[20]);
  in_read(ini);
  inClass inf = inClass(a_in, len);
  for(char ch = 1; ch <= casesZ(inf.text[0]); ch++){
    for(char chh = 0; chh < strlen(inf.text[ch]); chh++){
      inf.text[ch][chh] = trnaslate(inf.text[ch][chh]);
    }
  }
  outClass outf = outClass(inf.text, casesZ(inf.text[0]));
  free(a_in);
}
void in_read(char in[20]){
  char dir[] = "/Googlerese/";
  len = strlen(dir) + 20;
  a_in = (char*)malloc(len);
  if(a_in==NULL){
    cout << "Error!!! No memory is allocated.";
    exit(0);
  }
  else{
    for(int i = 0; i <= len; i++) a_in[i] = dir[i];
    for(int i = 0; i < 20; i++) a_in[i + len - 20] = in[i];
  }
}

char trnaslate(char ch){
  switch(ch){
  case 'a': return'y';break;
  case 'b': return'h';break;
  case 'c': return'e';break;
  case 'd': return's';break;
  case 'e': return'o';break;
  case 'f': return'c';break;
  case 'g': return'v';break;
  case 'h': return'x';break;
  case 'i': return'd';break;
  case 'j': return'u';break;
  case 'k': return'i';break;
  case 'l': return'g';break;
  case 'm': return'l';break;
  case 'n': return'b';break;
  case 'o': return'k';break;
  case 'p': return'r';break;
  case 'q': return'z';break;
  case 'r': return't';break;
  case 's': return'n';break;
  case 't': return'w';break;
  case 'u': return'j';break;
  case 'v': return'p';break;
  case 'w': return'f';break;
  case 'x': return'm';break;
  case 'y': return'a';break;
  case 'z': return'q';break;
  case ' ': return' ';break;
  }
}

char casesZ(char* in){
  char caseS = 0;
  char digit = 1;
  int end = strlen(in);
  for(int i = end - 1; i >= 0; i--){
    caseS += (in[i] - 0x30)*digit;
    digit*=10;
  }
  return caseS;
}

#endif	/* SRC */
