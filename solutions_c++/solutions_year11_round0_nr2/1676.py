/*
 *  Magicka.cpp
 *  
 *
 *  Created by Shobhit Srivastava on 07/05/11.
 *  Copyright 2011 IIT Rajisthan. All rights reserved.
 *
 */


#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

char buf[1000];
char soln[100];

int matnum(char a)
{
	switch (a)
	{
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default : return 8;
	}
}

int main() 
{
	freopen("B-large.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for(int test=1;test<=t;test++) 
	{
		char data[8][8][2];
		int c,d,n;
		int count=0,len;
		char token[4];
		char string[101];
		scanf("%d ",&c);
		for(int i=0;i<8;i++)
			for(int j=0;j<8;j++)
				for(int k=0;k<2;k++)
					data[i][j][k]='0';
		while(count<c)
		{
			scanf( " %s ", token);
			data[matnum(token[0])][matnum(token[1])][0]=token[2];
			data[matnum(token[1])][matnum(token[0])][0]=token[2];
			count++;
		}
		scanf(" %d ",&d);
		count=0;
		while(count<d)
		{
			scanf(" %s ",token);
			data[matnum(token[0])][matnum(token[1])][1]='1';
			data[matnum(token[1])][matnum(token[0])][1]='1';
			count++;
		}
		scanf(" %d ",&n);
		scanf(" %s ",string);
		memset(soln,'\0',100);
		soln[0]=string[0];
		count=0;
		for(int i=1;i<n;i++)
			if(count==-1)
			{
				count++;
				soln[count]=string[i];
			}
			else
			if(matnum(soln[count])==8)
			{
				for (int k=0; k<=count;k++)
						if(matnum(soln[k])!=8)
							if(data[matnum(string[i])][matnum(soln[k])][1]!='0')
							{
								memset(soln,'\0',100);
								count=-1;
							}
					if(soln[0]!='\0')
					{
						count++;
						soln[count]=string[i];
					}
				
			}
			else
				if(data[matnum(string[i])][matnum(soln[count])][0]!='0')
					soln[count]=data[matnum(string[i])][matnum(soln[count])][0];
				else
				{
					for (int k=0; k<=count;k++)
						if(matnum(soln[k])!=8)
							if(data[matnum(string[i])][matnum(soln[k])][1]!='0')
							{
								memset(soln,'\0',100);
								count=-1;
							}
					if(soln[0]!='\0')
					{
						count++;
						soln[count]=string[i];
					}
					
				}

		printf("Case #%d: [",test);
		if(soln[0]!='\0')
		{
		for(int i=0;i<count;i++)
			printf("%c, ",soln[i]);
		printf("%c]\n",soln[count]);
		}
		else
			printf("]\n");
	}
	return 0;
}
				
				
					
			
