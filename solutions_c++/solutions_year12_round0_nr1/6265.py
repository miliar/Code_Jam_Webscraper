#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

int T;
char Line[150],Map[30]={"yhesocvxduiglbkrztnwjpfmaq"};

ifstream fin("A.in");
ofstream fout("A.out");

int main(){
	fin>>T;
	fin.get();
	for(int i=1;i<=T;i++){
		fin.get(Line,150);
		fin.get();
		fout<<"Case #"<<i<<": ";
		for(int i=0;i<strlen(Line);i++){
			if(Line[i]>='a' && Line[i]<='z')
				fout<<Map[int(Line[i]-'a')];
			else
				fout<<Line[i];
		}
		fout<<"\n";
	}
	fout.close();
	fin.close();
	return 0;
}