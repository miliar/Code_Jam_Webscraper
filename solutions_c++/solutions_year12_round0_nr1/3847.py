#include <iostream>
#include <fstream>

using namespace std;

void Prob1() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T,t,i;
	char str[128];

	fin >> T;
	fin.getline(str,128);
	t=1;

	while(T--) {
		fin.getline(str,128);
		
		fout << "Case #" << t++ << ": ";
		for(i=0;i<strlen(str);i++) {
				 if(str[i]=='y') fout << "a";
			else if(str[i]=='n') fout << "b";
			else if(str[i]=='f') fout << "c";
			else if(str[i]=='i') fout << "d";
			else if(str[i]=='c') fout << "e";
			else if(str[i]=='w') fout << "f";
			else if(str[i]=='l') fout << "g";
			else if(str[i]=='b') fout << "h";
			else if(str[i]=='k') fout << "i";
			else if(str[i]=='u') fout << "j";
			else if(str[i]=='o') fout << "k";
			else if(str[i]=='m') fout << "l";
			else if(str[i]=='x') fout << "m";
			else if(str[i]=='s') fout << "n";
			else if(str[i]=='e') fout << "o";
			else if(str[i]=='v') fout << "p";
			else if(str[i]=='z') fout << "q";
			else if(str[i]=='p') fout << "r";
			else if(str[i]=='d') fout << "s";
			else if(str[i]=='r') fout << "t";
			else if(str[i]=='j') fout << "u";
			else if(str[i]=='g') fout << "v";
			else if(str[i]=='t') fout << "w";
			else if(str[i]=='h') fout << "x";
			else if(str[i]=='a') fout << "y";
			else if(str[i]=='q') fout << "z";
			else fout << str[i];
		}
		
		if(T) fout << endl;
	}


	fin.close();
	fout.close();
}


int main()
{
	Prob1();
	system("pause");
	return 0;
}