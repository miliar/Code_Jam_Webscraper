#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main(){
int n;

ifstream ifs;
ifs.open("a.txt");
ifs>>n;
string s[n+1];
for(int i=0; i<n+1; i++){
getline(ifs, s[i]);
}
ifs.close();

ofstream ofs;
ofs.open("answer.txt");

char alphabet;
for(int i=0; i<n+1; i++){
if(i!=0){	
	ofs<<"Case #"<<i<<": ";
	
	for(int j=0; j<s[i].size(); j++){
		alphabet=s[i][j];

	switch (alphabet) {
	case 'a': {ofs<<'y'; break;}
	case 'b': {ofs<<'h'; break;}
	case 'c': {ofs<<'e'; break;}
	case 'd': {ofs<<'s'; break;}
	case 'e': {ofs<<'o'; break;}
	case 'f': {ofs<<'c'; break;}
	case 'g': {ofs<<'v'; break;}
	case 'h': {ofs<<'x'; break;}
	case 'i': {ofs<<'d'; break;}
	case 'j': {ofs<<'u'; break;}
	case 'k': {ofs<<'i'; break;}
	case 'l': {ofs<<'g'; break;}
	case 'm': {ofs<<'l'; break;}
	case 'n': {ofs<<'b'; break;}
	case 'o': {ofs<<'k'; break;}
	case 'p': {ofs<<'r'; break;}
	case 'q': {ofs<<'z'; break;}
	case 'r': {ofs<<'t'; break;}
	case 's': {ofs<<'n'; break;}
	case 't': {ofs<<'w'; break;}
	case 'u': {ofs<<'j'; break;}
	case 'v': {ofs<<'p'; break;}
	case 'w': {ofs<<'f'; break;}
	case 'x': {ofs<<'m'; break;}
	case 'y': {ofs<<'a'; break;}
	case 'z': {ofs<<'q'; break;}
	case 32 : {ofs<<" "; break;}

		  }
	}ofs<<endl;
}
}
ofs.close();
return 0;}
