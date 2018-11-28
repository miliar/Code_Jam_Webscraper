#include<stdio.h>
#include<stdlib.h>
#include<cstring>
#include<string>
#include<iostream>

using namespace std;

const int MAX = 256;
char translator[MAX];
int number;
string str;
char* word;
char* translated;

int main(){
  translator[(int) ' '] = ' ';
  translator[(int) 'a'] = 'y';
  translator[(int) 'b'] = 'h';
  translator[(int) 'c'] = 'e';
  translator[(int) 'd'] = 's';
  translator[(int) 'e'] = 'o';
  translator[(int) 'f'] = 'c';
  translator[(int) 'g'] = 'v';
  translator[(int) 'h'] = 'x';
  translator[(int) 'i'] = 'd';
  translator[(int) 'j'] = 'u';
  translator[(int) 'k'] = 'i';
  translator[(int) 'l'] = 'g';
  translator[(int) 'm'] = 'l';
  translator[(int) 'n'] = 'b';
  translator[(int) 'o'] = 'k';
  translator[(int) 'p'] = 'r';
  translator[(int) 'q'] = 'z';
  translator[(int) 'r'] = 't';
  translator[(int) 's'] = 'n';
  translator[(int) 't'] = 'w';
  translator[(int) 'u'] = 'j';
  translator[(int) 'v'] = 'p';
  translator[(int) 'w'] = 'f';
  translator[(int) 'x'] = 'm';
  translator[(int) 'y'] = 'a';
  translator[(int) 'z'] = 'q';
  scanf("%d\n", &number);
  for(int i=0; i<number; ++i){
    getline(cin, str);
    word = new char [str.size()+1];
    strcpy(word, str.c_str());
    translated = new char [str.size()+1];
    int length = (int) str.length();
    for(int j=0; j<length; ++j){
      translated[j] = translator[(int) word[j]];
    }
    printf("Case #%d: %s\n",i+1 ,translated);
  }
  return 0;
}
