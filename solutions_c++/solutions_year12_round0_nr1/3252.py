#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(int argc, char** argv)
{ 
 ifstream file;
 file.open(argv[1]);
 if(!file) return 0;
 int N;
 int i=0;
 while(!file.eof()){
	string s;
	getline(file,s);
	if(i==0){
	 N = atoi(&s[0]);
// 	 cout << N << endl;
	}
	if(i!=0 && i<=N)	{
	  cout << "Case #" << i << ": "; 
	  for(int c=0; c<s.size(); c++){
		 	switch(s[c]){
			  case ' ': cout << ' '; break;
			  case 'a': cout << 'y'; break;
			  case 'b': cout << 'h'; break;
			  case 'c': cout << 'e'; break;
			  case 'd': cout << 's'; break;
			  case 'e': cout << 'o'; break;
			  case 'f': cout << 'c'; break;
			  case 'g': cout << 'v'; break;
			  case 'h': cout << 'x'; break;
			  case 'i': cout << 'd'; break;
			  case 'j': cout << 'u'; break;
			  case 'k': cout << 'i'; break;
			  case 'l': cout << 'g'; break;
			  case 'm': cout << 'l'; break;
			  case 'n': cout << 'b'; break;
			  case 'o': cout << 'k'; break;
			  case 'p': cout << 'r'; break;
			  case 'q': cout << 'z'; break;
			  case 'r': cout << 't'; break;
			  case 's': cout << 'n'; break;
			  case 't': cout << 'w'; break;
			  case 'u': cout << 'j'; break;
			  case 'v': cout << 'p'; break;
			  case 'w': cout << 'f'; break;
			  case 'x': cout << 'm'; break;
			  case 'y': cout << 'a'; break;
			  case 'z': cout << 'q'; break;
		 } 
	  }
	  cout << endl;
	}
   
  i++;
 }
 
 return 0;
}
