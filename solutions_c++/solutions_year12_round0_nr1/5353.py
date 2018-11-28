#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
void fun(char str[150])
{
	for(int i=0;str[i];i++)
	{
		switch(str[i])
		{
		case 'y':
			str[i]='a';
			break;
		case 'n':
			str[i]='b';
			break;
		case 'f':
			str[i]='c';
			break;
		case 'i':
			str[i]='d';
			break;
		case 'c':
			str[i]='e';
			break;
		case 'w':
			str[i]='f';
			break;
		case 'l':
			str[i]='g';
			break;
		case 'b':
			str[i]='h';
			break;
		case 'k':
			str[i]='i';
			break;
		case 'u':
			str[i]='j';
			break;
		case 'o':
			str[i]='k';
			break;
		case 'm':
			str[i]='l';
			break;
		case 'x':
			str[i]='m';
			break;
		case 's':
			str[i]='n';
			break;
		case 'e':
			str[i]='o';
			break;
		case 'v':
			str[i]='p';
			break;
		case 'z':
			str[i]='q';
			break;
		case 'p':
			str[i]='r';
			break;
		case 'd':
			str[i]='s';
			break;
		case 'r':
			str[i]='t';
			break;
		case 'j':
			str[i]='u';
			break;
		case 'g':
			str[i]='v';
			break;
		case 't':
			str[i]='w';
			break;
		case 'h':
			str[i]='x';
			break;
		case 'a':
			str[i]='y';
			break;
		case 'q':
			str[i]='z';
			break;
		}
	}
}
void main()
{

	int N;
	char str[30][101];
	char str2[100];
	ifstream ifile;
	ofstream ofile;
	ifile.open("A-small-attempt1.in",ios::in);
	ofile.open("output.out",ios::out);
	ifile>>N;
	ifile.getline(str2,100);
	for(int i=0;i<N;i++)
	{
		ifile.getline(str[i],101);
		cout<<str[i]<<endl;
		fun(str[i]);
		cout<<str[i]<<endl;
		ofile<<"Case #"<<i+1<<": "<<str[i]<<endl;
	}
	
	ifile.close();
	ofile.close();
	getch();
}