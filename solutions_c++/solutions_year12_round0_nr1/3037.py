// gcj_1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
  map<char, char> mapping;
  mapping.insert( pair<char,char>('y', 'a') );
  mapping.insert( pair<char,char>('n', 'b') );
  mapping.insert( pair<char,char>('f', 'c') );
  mapping.insert( pair<char,char>('i', 'd') );
  mapping.insert( pair<char,char>('c', 'e') );
  mapping.insert( pair<char,char>('w', 'f') );
  mapping.insert( pair<char,char>('l', 'g') );
  mapping.insert( pair<char,char>('b', 'h') );
  mapping.insert( pair<char,char>('k', 'i') );
  mapping.insert( pair<char,char>('u', 'j') );
  mapping.insert( pair<char,char>('o', 'k') );
  mapping.insert( pair<char,char>('m', 'l') );
  mapping.insert( pair<char,char>('x', 'm') );
  mapping.insert( pair<char,char>('s', 'n') );
  mapping.insert( pair<char,char>('e', 'o') );
  mapping.insert( pair<char,char>('v', 'p') );
  mapping.insert( pair<char,char>('z', 'q') );
  mapping.insert( pair<char,char>('p', 'r') );
  mapping.insert( pair<char,char>('d', 's') );
  mapping.insert( pair<char,char>('r', 't') );
  mapping.insert( pair<char,char>('j', 'u') );
  mapping.insert( pair<char,char>('g', 'v') );
  mapping.insert( pair<char,char>('t', 'w') );
  mapping.insert( pair<char,char>('h', 'x') );
  mapping.insert( pair<char,char>('a', 'y') );
  mapping.insert( pair<char,char>('q', 'z') );
  int t;
  
  

  ifstream in("A-small-attempt0.in");
  ofstream out("output.txt");
  in>>t;
  int c=t;
  while(t--){
    string str;
    getline(in, str);
    if(str.length() < 1){
      t++;
      continue;
    }
    for(int i=0;i<str.length();i++){
      if(str[i] == ' ')continue;
      str[i] = mapping[str[i]];
    }
    out<<"Case #"<<c-t<<": "<<str<<endl;
  }

	return 0;
}

