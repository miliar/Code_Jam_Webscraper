#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
char dec(char input)
{
//cout<<input;
if(input=='a')
	return 'y';
if(input=='b')
	return 'h';
if(input=='c')
	return 'e';
if(input=='d')
	return 's';
if(input=='e')
	return 'o';
if(input=='f')
	return 'c';
if(input=='g')
	return 'v';
if(input=='h')
	return 'x';
if(input=='i')
	return 'd';
if(input=='j')
	return 'u';
if(input=='k')
	return 'i';
if(input=='l')
	return 'g';
if(input=='m')
	return 'l';
if(input=='n')
	return 'b';
if(input=='o')
	return 'k';
if(input=='p')
	return 'r';
if(input=='q')
	return 'z';
if(input=='r')
	return 't';
if(input=='s')
	return 'n';
if(input=='t')
	return 'w';
if(input=='u')
	return 'j';
if(input=='v')
	return 'p';
if(input=='w')
	return 'f';
if(input=='x')
	return 'm';
if(input=='y')
	return 'a';
if(input=='z')
	return 'q';
else
	return '1';

}

int main()
{
 char ch,ch1='y';
 int i=1,lines=0;
 ifstream infile ("input.in");
 ofstream outfile;
 outfile.open ("out.txt");
 infile>>lines;
 ch=infile.get();
 while(lines>0)
 {
	fflush(stdin);
	ch=infile.get();
	outfile<<"Case #"<<i<<": ";
 	while (ch!='\n')
 	{
	 ch1=dec(ch);
	 cout<<ch1;
	 if(ch1!='1')
	 outfile<<ch1; 
	 else
	 outfile<<" ";
	fflush(stdin);
	 ch=infile.get();
 	}
	outfile<<'\n';
	lines--;
	i++;
 }

 outfile.close();
}
