#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>

void rep(char * s, int t)
{
	switch(s[t])
	{
		case 'a': s[t]='y'; break;
		case 'b': s[t]='h'; break;
		case 'c': s[t]='e'; break;
		case 'd': s[t]='s'; break;
		case 'e': s[t]='o'; break;
		case 'f': s[t]='c'; break;
		case 'g': s[t]='v'; break;
		case 'h': s[t]='x'; break;
		case 'i': s[t]='d'; break;
		case 'j': s[t]='u'; break;
		case 'k': s[t]='i'; break;
		case 'l': s[t]='g'; break;
		case 'm': s[t]='l'; break;
		case 'n': s[t]='b'; break;
		case 'o': s[t]='k'; break;
		case 'p': s[t]='r'; break;
		case 'q': s[t]='z'; break;
		case 'r': s[t]='t'; break;
		case 's': s[t]='n'; break;
		case 't': s[t]='w'; break;
		case 'u': s[t]='j'; break;
		case 'v': s[t]='p'; break;
		case 'w': s[t]='f'; break;
		case 'x': s[t]='m'; break;
		case 'y': s[t]='a'; break;
		case 'z': s[t]='q'; break;
		case ' ': s[t]=' '; break;
	}
}

void conv(char* a)
{      int t=0;
	while(a[t]!='\0')
	{
		rep(a,t);
		t++;
	}
}


void main()
{
	int n;
       char str[105];
       ifstream fin;
       ofstream fout;
       fin.open("input.txt");
       fout.open("out.txt");
       fin>>n;
       fin.getline(str,105);
       for(int i=0;i<n;i++)
       {
	    //gets(str);
	    fin.getline(str,105);
	    conv(str);
	    fout<<"Case #"<<i+1<<": "<<str<<endl;
       }

}

