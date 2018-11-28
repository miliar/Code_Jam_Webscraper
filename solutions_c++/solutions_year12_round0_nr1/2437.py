#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	ofstream fout("out.txt");
	ifstream fin("file1.in");
	int t,i;
	char a[101],b[101];
	fin>>t;
	fin.ignore(1);
	int x=1;
	while(t--){
		fin.getline(a,101);
		i=0;
		while(a[i]!='\0'){
			if(a[i]=='a')
				b[i]='y';
			else if(a[i]=='b')
				b[i]='h';
			else if(a[i]=='c')
				b[i]='e';
			else if(a[i]=='d')
				b[i]='s';
			else if(a[i]=='e')
				b[i]='o';
			else if(a[i]=='f')
				b[i]='c';
			else if(a[i]=='g')
				b[i]='v';
			else if(a[i]=='h')
				b[i]='x';			
			else if(a[i]=='i')
				b[i]='d';
			else if(a[i]=='j')
				b[i]='u';
			else if(a[i]=='k')
				b[i]='i';
			else if(a[i]=='l')
				b[i]='g';	
			else if(a[i]=='m')
				b[i]='l';
			else if(a[i]=='n')
				b[i]='b';
			else if(a[i]=='o')
				b[i]='k';
			else if(a[i]=='p')
				b[i]='r';
			else if(a[i]=='q')
				b[i]='z';
			else if(a[i]=='r')
				b[i]='t';
			else if(a[i]=='s')
				b[i]='n';
			else if(a[i]=='t')
				b[i]='w';
			else if(a[i]=='u')
				b[i]='j';
			else if(a[i]=='v')
				b[i]='p';
			else if(a[i]=='w')
				b[i]='f';
			else if(a[i]=='x')
				b[i]='m';
			else if(a[i]=='y')
				b[i]='a';
			else if(a[i]=='z')
				b[i]='q';
			else b[i]=a[i];
			i++;
		}
		b[i]='\0';
		fout<<"Case #"<<x<<": "<<b;
		fout<<endl;
		x++;
	}
	return 0 ;
}
