//==Auther: Muhammad Umair
//==Used Software: Visual Studio 2008
//==Creation Date: 14/04/2012
#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

void main()
{	// Declaring variables
	char a[3002];
	char ch;
	int i=0,t,w=0,e;
	ifstream in;
	ofstream out;
	out.open("A-small-attempt2.in.txt");
	in.open("qw.in");
	//out<<"Input"<<endl;
	in>>t; // Inputs counter
	in.get(ch);
	//out<<t;
	//out<<endl;
	// Read the Googlereas from user
	while(w<t)
	{
		in.get(a[i]);
		i++;
		if(a[i-1]=='\n')
		{
			w++;
		}
	}
	//out<<"_______________________________"<<endl<<endl<<"Output"<<endl<<endl;

	// Decodes the googlerese language to normal
	// language
	for(int j=0;j<i;j++)
	{
		if(a[j]=='y')
			a[j]='a';
		else if(a[j]=='n')
			a[j]='b';
		else if(a[j]=='f')
			a[j]='c';
		else if(a[j]=='i')
			a[j]='d';
		else if(a[j]=='c')
			a[j]='e';
		else if(a[j]=='w')
			a[j]='f';
		else if(a[j]=='l')
			a[j]='g';
		else if(a[j]=='b')
			a[j]='h';
		else if(a[j]=='k')
			a[j]='i';
		else if(a[j]=='u')
			a[j]='j';
		else if(a[j]=='o')
			a[j]='k';
		else if(a[j]=='m')
			a[j]='l';
		else if(a[j]=='x')
			a[j]='m';
		else if(a[j]=='s')
			a[j]='n';
		else if(a[j]=='e')
			a[j]='o';
		else if(a[j]=='v')
			a[j]='p';
		else if(a[j]=='z')
			a[j]='q';
		else if(a[j]=='p')
			a[j]='r';
		else if(a[j]=='d')
			a[j]='s';
		else if(a[j]=='r')
			a[j]='t';
		else if(a[j]=='j')
			a[j]='u';
		else if(a[j]=='g')
			a[j]='v';
		else if(a[j]=='t')
			a[j]='w';
		else if(a[j]=='h')
			a[j]='x';
		else if(a[j]=='a')
			a[j]='y';
		else if(a[j]=='q')
			a[j]='z';
		else if(a[j]==' ')
			a[j]=' ';
		else if(a[j]=='\n')
			a[j]='\n';
	}
	e=2; // Counter for case
	out<<"Case #1: ";
	// Shows the decoded language
	for(int q=0;q<i;q++)
	{
		out<<a[q];
		if(a[q]=='\n' && e!=(t+1))
		{
			out<<"Case #"<<e<<": ";
			e++;
		}
		
	}
	out<<endl;
	in.close();
	out.close();
	system("pause");
}