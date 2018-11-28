#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char l[1000];
int x,n,i;
int main()
{
	scanf("%d ", &n);
	n++;
	while(--n)
	{
		i++;
		gets(l);
		x=strlen(l);
		cout << "Case #" << i << ": ";
		for(int i=0; i<x; i++)
		{
			if(l[i]=='a')
				cout << "y";
			if(l[i]=='b')
				cout << "h";
			if(l[i]=='c')
				cout << "e";
			if(l[i]=='d')
				cout << "s";
			if(l[i]=='e')
				cout << "o";
			if(l[i]=='f')
				cout << "c";
			if(l[i]=='g')
				cout << "v";
			if(l[i]=='h')
				cout << "x";
			if(l[i]=='i')
				cout << "d";
			if(l[i]=='j')
				cout << "u";
			if(l[i]=='k')
				cout << "i";
			if(l[i]=='l')
				cout << "g";
			if(l[i]=='m')
				cout << "l";
			if(l[i]=='n')
				cout << "b";
			if(l[i]=='o')
				cout << "k";
			if(l[i]=='p')
				cout << "r";
			if(l[i]=='q')
				cout << "z";
			if(l[i]=='r')
				cout << "t";
			if(l[i]=='s')
				cout << "n";
			if(l[i]=='t')
				cout << "w";
			if(l[i]=='u')
				cout << "j";
			if(l[i]=='w')
				cout << "f";
			if(l[i]=='v')
				cout << "p";
			if(l[i]=='x')
				cout << "m";
			if(l[i]=='y')
				cout << "a";
			if(l[i]=='z')
				cout << "q";
			if(l[i]==' ')
				cout << " ";
		}
		cout << endl;
	}
}
