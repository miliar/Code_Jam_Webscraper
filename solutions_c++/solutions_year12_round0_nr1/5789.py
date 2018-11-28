#include <iostream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<fstream.h>

void main()
{
	clrscr();

	char G[100],ch;
	int T,t,i=0,j;
	ofstream fo("cj1.txt");
	fstream fil("trial2.txt",ios::in);
	T=30;
	for(j=0;j<=T+1;j++)
	{
	   fil.getline(G,100);
	   for(i=0;i<strlen(G);i++)
	   {
		switch(G[i])
		{
			case 'y': G[i]='a';
				  break;
			case 'n': G[i]='b';
				  break;
			case 'f': G[i]='c';
				  break;
			case 'i': G[i]='d';
				  break;
			case 'c': G[i]='e';
				  break;
			case 'w': G[i]='f';
				  break;
			case 'l': G[i]='g';
				  break;
			case 'b': G[i]='h';
				  break;
			case 'k': G[i]='i';
				  break;
			case 'u': G[i]='j';
				  break;
			case 'o': G[i]='k';
				  break;
			case 'm': G[i]='l';
				  break;
			case 'x': G[i]='m';
				  break;
			case 's': G[i]='n';
				  break;
			case 'e': G[i]='o';
				  break;
			case 'v': G[i]='p';
				  break;
			case 'z': G[i]='q';
				  break;
			case 'p': G[i]='r';
				  break;
			case 'd': G[i]='s';
				  break;
			case 'r': G[i]='t';
				  break;
			case 'j': G[i]='u';
				  break;
			case 'g': G[i]='v';
				  break;
			case 't': G[i]='w';
				  break;
			case 'h': G[i]='x';
				  break;
			case 'a': G[i]='y';
				  break;
			case 'q': G[i]='z';
				  break;

			case ' ': break;
		}
	   }
	   if(j!=0)
	   {
		cout<<G<<"\n";
		fo<<"Case #"<<j<<": "<<G<<"\n";
	   }
	}
	fo.close();
	fil.close();

	getch();
}


