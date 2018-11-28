#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<cstdlib>
#include<fstream>
using namespace std;
int main(){

	ofstream fout ("googlecodejamq1.txt");
    	ifstream fin ("A-small-attempt0.in");
	int testcase;
	fin>>testcase;
	char s[200];char outStr[201];
	int printCounter=1;
	int count[8];int c;int i,j;int temp;
	j=1;
	fin.ignore(1);
	while(testcase--){

		
		fin.getline(s,201);
		//fin.ignore(1);
		for(i=0;s[i]!='\0';i++){
			if(s[i]=='a')
				outStr[i]='y';
			else if(s[i]=='b')
				outStr[i]='h';
			else if(s[i]=='c')
				outStr[i]='e';
			else if(s[i]=='d')
				outStr[i]='s';
			else if(s[i]=='e')
				outStr[i]='o';
			else if(s[i]=='f')
				outStr[i]='c';
			else if(s[i]=='g')
				outStr[i]='v';
			else if(s[i]=='h')
				outStr[i]='x';
			else if(s[i]=='i')
				outStr[i]='d';
			else if(s[i]=='j')
				outStr[i]='u';
			else if(s[i]=='k')
				outStr[i]='i';
			else if(s[i]=='l')
				outStr[i]='g';
			else if(s[i]=='m')
				outStr[i]='l';
			else if(s[i]=='n')
				outStr[i]='b';
			else if(s[i]=='o')
				outStr[i]='k';
			else if(s[i]=='p')
				outStr[i]='r';
			else if(s[i]=='q')
				outStr[i]='z';
			else if(s[i]=='r')
				outStr[i]='t';
			else if(s[i]=='s')
				outStr[i]='n';
			else if(s[i]=='t')
				outStr[i]='w';
			else if(s[i]=='u')
				outStr[i]='j';
			else if(s[i]=='v')
				outStr[i]='p';
			else if(s[i]=='w')
				outStr[i]='f';
			else if(s[i]=='x')
				outStr[i]='m';
			else if(s[i]=='y')
				outStr[i]='a';
			else if(s[i]=='z')
				outStr[i]='q';
			else
				outStr[i]=s[i];
		}
		outStr[i]='\0';
		fout<<"Case #"<<j<<": ";
		fout<<outStr<<endl;
		j++;
	
	}
	return 0;
 
} 
