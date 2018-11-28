#include <iostream>
#include <fstream>
using namespace std;

char transform (char a) {
	if (a=='y') return 'a';
	else if (a=='n') return 'b';
	else if (a=='f') return 'c';
	else if (a=='i') return 'd';
	else if (a=='c') return 'e';
	else if (a=='w') return 'f';
	else if (a=='l') return 'g';
	else if (a=='b') return 'h';
	else if (a=='k') return 'i';
	else if (a=='u') return 'j';
	else if (a=='o') return 'k';
	else if (a=='m') return 'l';
	else if (a=='x') return 'm';
	else if (a=='s') return 'n';
	else if (a=='e') return 'o';
	else if (a=='v') return 'p';
	else if (a=='z') return 'q';
	else if (a=='p') return 'r';
	else if (a=='d') return 's';
	else if (a=='r') return 't';
	else if (a=='j') return 'u';
	else if (a=='g') return 'v';
	else if (a=='t') return 'w';
	else if (a=='h') return 'x';
	else if (a=='a') return 'y';
	else if (a=='q') return 'z';
	else return a;
}

int main () {
	ifstream fin ("speak.in");
	ofstream fout ("speak.out");
	
	int T;
	fin>>T;
	char * in;
	for (int k=1;k<=T+1;k++) {
		in=new char [100];
		fin.getline (in,101);
		if (k==1) continue;
		fout<<"Case #"<<k-1<<": ";
		for (int w=0;in[w]!='\0';w++) {
			fout<<transform(in[w]);
		}
		fout<<'\n';
		delete [] in;
	}
	return 0;
}