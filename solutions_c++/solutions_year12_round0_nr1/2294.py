#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
#include<iostream>

using namespace std;

int SIZE = 0;
char* translate(char*);
int main(int argc, char** argv){
  if(argc != 2){
    cerr<<"Invalid input provided"<<endl;
    return -1;
  }
  char in_string[101];
  ifstream in(argv[1]);
  in>>SIZE;
  in.getline(in_string,1);
  for(int i=1; i<=SIZE; i++){
    in.getline(in_string, 101);
    printf("Case #%d: %s\n", i, translate(in_string));
  }     
}

char* translate(char* s){
  for(int i=0; i< strlen(s); i++){
    switch (s[i]){
    case 'a': s[i]='y'; break;
    case 98: s[i]='h';break;
    case 99: s[i]='e';break;
    case 100: s[i]='s';break;
    case 101: s[i]='o';break;
    case 102: s[i]='c';break;
    case 103: s[i]='v';break;
    case 104: s[i]='x';break;
    case 105: s[i]='d';break;
    case 106: s[i]='u';break;
    case 107: s[i]='i';break;
    case 108: s[i]='g';break;
    case 109: s[i]='l';break;
    case 110: s[i]='b';break;
    case 111: s[i]='k';break;
    case 112: s[i]='r';break;
    case 113: s[i]='z';break;
    case 114: s[i]='t';break;
    case 115: s[i]='n';break;
    case 116: s[i]='w';break;
    case 117: s[i]='j';break;
    case 118: s[i]='p';break;
    case 119: s[i]='f';break;
    case 120: s[i]='m';break;
    case 121: s[i]='a';break;
    case 122: s[i]='q';break;
    default: break;
    }
  }
    return s;
}
