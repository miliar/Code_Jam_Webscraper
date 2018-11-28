#include <iostream>
#include <string>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <map>

using namespace std;

string transformStr(string in_str){
  map<char,char> alphabet;
  map<char,char>::iterator it;
  alphabet['a']='y';
  alphabet['b']='h';
  alphabet['c']='e';
  alphabet['d']='s';	
  alphabet['e']='o';
  alphabet['f']='c';
  alphabet['g']='v';
  alphabet['h']='x';	
  alphabet['i']='d';
  alphabet['j']='u';
  alphabet['k']='i';
  alphabet['l']='g';	
  alphabet['m']='l';
  alphabet['n']='b';
  alphabet['o']='k';
  alphabet['p']='r';
  alphabet['q']='z';	
  alphabet['r']='t';
  alphabet['s']='n';
  alphabet['t']='w';
  alphabet['u']='j';	
  alphabet['v']='p';
  alphabet['w']='f';
  alphabet['x']='m';
  alphabet['y']='a';	
  alphabet['z']='q';	
  
  int len=in_str.length();
  string out_str="";
  for (int i=0;i<len;i++){
	  if (!isalpha(in_str[i])){
		  out_str+=in_str[i];
	  }
	  else {
		  char c =tolower(in_str[i]);
		  out_str += alphabet.find(c)->second;
      }
   }
  
  return out_str;
}

int main () {
	
  char case_nr[256];
  cin>>case_nr;
  int k=atoi(case_nr);
  string getToNextLine;
  getline (cin,getToNextLine);
  
  for (int i=0;i<k;i++){
	  string in_str;
	  getline (cin,in_str);
	  string out_str=transformStr(in_str);
	  cout<<"Case #"<<i+1<<": "<<out_str<<"\n";
	}
	
  return 0;
}
