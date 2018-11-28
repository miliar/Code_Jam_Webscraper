// codejam_q_1.cpp : Defines the entry point for the console application.
//

#include"stdafx.h"
#include<iostream>
using namespace std;

#define max 101

char inp[max];

char out[max];

int main()
{
	freopen("inp.txt","r",stdin);

	freopen("out.txt","w",stdout);

	int t,testcases,i;

	scanf("%d",&testcases);

	cin.get();

	t=testcases;

	char mapp[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	while(t)
	{

	gets(inp);

	for(i=0;i<strlen(inp);i++)
	{
		if(inp[i]==' ')
		{
			out[i]=' ';
			
		}

		else
			
		out[i]=mapp[inp[i]-97];
	}

	out[i]='\0';
	printf("case #%d: %s\n",testcases-t+1,out);

	t--;

	}

}
