// Dance with Googleres.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include<stdio.h>
#include<iostream>
using namespace std;

void main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	int T;
	char G[100],S;
	scanf("%d",&T);
	for(int j=0;j<=T;j++)
	{
		gets(G);
		
		for(int i=0;i<strlen(G);i++)
		{
			
			switch(G[i])
			{
			case 'y': S='a';break;
			case 'n': S='b';break;
			case 'f': S='c';break;
			case 'i': S='d';break;
			case 'c': S='e';break;
			case 'w': S='f';break;
			case 'l': S='g';break;
			case 'b': S='h';break;
			case 'k': S='i';break;
			case 'u': S='j';break;
			case 'o': S='k';break;
			case 'm': S='l';break;
			case 'x': S='m';break;
			case 's': S='n';break;
			case 'e': S='o';break;
			case 'v': S='p';break;
			case 'z': S='q';break;
			case 'p': S='r';break;
			case 'd': S='s';break;
			case 'r': S='t';break;
			case 'j': S='u';break;
			case 'g': S='v';break;
			case 't': S='w';break;
			case 'h': S='x';break;
			case 'a': S='y';break;
			case 'q': S='z';break;
			case ' ': S=' ';break;
			}
			putc(S,stdout);	
		}
		if(j!=T)
		cout<<endl<<"Case #"<<j+1<<": ";
		
		
	}
}
