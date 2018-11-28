#include <iostream>
#include <string>
#include <fstream>
using namespace std;
char map(char in);
int main(){
	ifstream fin;
	fin.open("A-small-attempt3.in");
	string c;
	ofstream fout;
	fout.open("result.txt");
	string ans="";
	int ex;
	fin >> ex;
	getline(fin,c);
	for(int t=1; t<=ex; t++){
	getline(fin,c);
	for(int k=0; k<c.length(); k++){
	ans+=map(c[k]);
	}
	fout << "Case #";
	fout << t;
	fout <<": ";
	fout << ans;
	fout << "\n";
	ans.clear();
	}
	
	
	
	


return 0;
}

char map(char in){

switch(in){
case ' ':{return ' ';}
		 break;
	case 'a':{ return 'y';}
			 break;
	case 'b':{return 'h';}
			 break;
	case 'c':{ return 'e';}
			  break;
	case 'd':{return 's';}
			 break;
	case 'e':{return 'o';}
			 break;
	case 'f':{return 'c';}
			 break;
	case 'g':{return 'v';}
			 break;
	case 'h':{return 'x';}
			 break;
	case 'i':{return 'd';}
			 break;
	case 'j':{return 'u';}
			 break;
	case 'k':{return 'i';}
			 break;
	case 'l':{return 'g';}
			 break;
	case 'm':{return 'l';}
			 break;
	case 'n':{return 'b';}
			 break;
	case 'o': {return 'k';}
			  break;
	case 'p':{return 'r';}
			 break;
	case 'q':{return 'z';}
			 break;
	case 'r':{return 't';}
			 break;
	case 's':{return 'n';}
			 break;
	case 't':{return 'w';}
			 break;
	case 'u':{return 'j';}
			 break;
	case 'v':{return 'p';}
			 break;
	case 'w':{return 'f';}
			 break;
	case 'x':{return 'm';}
			 break;
	case 'y':{return 'a';}
			 break;
	case 'z':{return 'q';}
			 break;
	
	
	}

}