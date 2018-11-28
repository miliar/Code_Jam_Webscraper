#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

char convert(char ch);

void main()
{
	clrscr();
	ifstream a("A-small-attempt0.in");
	ofstream b("output.txt");
	char line[105];
	char outline[105];
	int count = 0;
	int size;
	if(!a)
		cout<<"unable to open file";
	a.getline(line,2);
	while(!a.eof())
	{    //fgets
		if(a.eof())
			break;
		a.getline(line,104);
		cout<<line<<endl;
		b<<"Case #"<<count<<": ";
		for(int i=0;i<strlen(line);i++)
		    b<<convert(line[i]);
		//outline[i]='\n';
		b<<endl;
		cout<<count<<endl;
		count++;
	}
	getch();
}
char convert(char ch)
{
	char a;
	switch(ch)
	{
		case 'y': a= 'a';
			break;
		case 'n': a= 'b';
			break;
		case 'f': a= 'c';
			break;
		case 'i': a= 'd';
			break;
		case 'c': a= 'e';
			break;
		case 'w': a= 'f';
			break;
		case 'l': a= 'g';
			break;
		case 'b': a= 'h';
			break;
		case 'k': a= 'i';
			break;
		case 'u': a= 'j';
			break;
		case 'o': a= 'k';
			break;
		case 'm': a= 'l';
			break;
		case 'x': a= 'm';
			break;
		case 's': a= 'n';
			break;
		case 'e': a= 'o';
			break;
		case 'v': a= 'p';
			break;
		case 'z': a= 'q';
			break;
		case 'p': a= 'r';
			break;
		case 'd': a= 's';
			break;
		case 'r': a= 't';
			break;
		case 'j': a= 'u';
			break;
		case 'g': a= 'v';
			break;
		case 't': a= 'w';
			break;
		case 'h': a= 'x';
			break;
		case 'a': a= 'y';
			break;
		case 'q': a= 'z';
			break;
		case ' ': a= ' ';
			break;
	}
	return a;
}