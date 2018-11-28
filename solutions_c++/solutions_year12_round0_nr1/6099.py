#include<iostream>
#include<fstream>

using namespace std;

char getSub(char c){
	switch(c){
		case 'y':
			return 'a';
			break;
		case 'n':
			return 'b';
			break;
		case 'f':
			return 'c';
			break;
		case 'i':
			return 'd';
			break;
		case 'c':
			return 'e';
			break;
		case 'w':
			return 'f';
			break;
		case 'l':
			return 'g';
			break;
		case 'b':
			return 'h';
			break;
		case 'k':
			return 'i';
			break;
		case 'u':
			return 'j';
			break;
		case 'o':
			return 'k';
			break;
		case 'm':
			return 'l';
			break;
		case 'x':
			return 'm';
			break;
		case 's':
			return 'n';
			break;
		case 'e':
			return 'o';
			break;
		case 'v':
			return 'p';
			break;
		case 'z':
			return 'q';
			break;
		case 'p':
			return 'r';
			break;
		case 'd':
			return 's';
			break;
		case 'r':
			return 't';
			break;
		case 'j':
			return 'u';
			break;
		case 'g':
			return 'v';
			break;
		case 't':
			return 'w';
			break;
		case 'h':
			return 'x';
			break;
		case 'a':
			return 'y';
			break;
		case 'q':
			return 'z';
			break;
		default:
			return c;
			break;
			
	}
	
}

 int main(){
 	//char sub[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
 	
	
 	ifstream fin ("data.in");
 	ofstream fout ("data.out");
 	
 	int N;
 	fin >> N;
 	for(int i=0;i<=N;i++){
 		string str;
 		getline(fin,str);
 		if(str.size() > 0){
	 		fout << "Case #" << i << ": ";	
	 		for(int i=0;i<str.size();i++){
	 			char c = getSub(str[i]);
	 			fout << c; 
			}
			fout << endl;	
		}
 	}

 	
 }

