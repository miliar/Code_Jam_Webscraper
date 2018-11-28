#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <float.h>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <iostream>
#include <list>
#include <vector>
#include <iterator>
#include "BigIntegerLibrary.hh"
using namespace std;

int totalteams=0;

class node
{
public:
	int teamNum;
	int record[100];
	double win;
	double owin;
	double oowin;
	double rpi;
	double numOpp;
	node(int TeamNum)
	{
		teamNum=TeamNum;
		for (int i=0;i<100;i++)
		{
			record[i]=-1;
		}
		win=0;
		owin=0;
		oowin=0;
		rpi=0;
		numOpp=0;
	}
	/*bool operator < (const node& rhs)
	{
		if (sortMethod==1)
		{
			return c > rhs.c;
		}
		else if(sortMethod==2)
		{
		return s > rhs.s;
		}
		else
		{
			return t < rhs.t;
		}
	}*/
};

void tiles();
void reset();
void calcPossible();

int worthUsing(list<node>::iterator);
int useCard(list<node>::iterator);

int main()
{
	tiles();
	return 0;
}


char picture[51][51];
int r=0;
int c=0;
void tiles()
{
	reset();
	int numCases=0;
	int n=0;
	char ch;
	scanf("%d\n",&numCases);
	//printf("%d\n",numCases);
	for (int i=0;i<numCases;i++)
	{
		scanf("%d %d\n",&r, &c);
		//printf("%d %d\n",r, c);
		for (int j=0;j<r;j++)
		{
			for (int k=0;k<c;k++)
			{
				scanf("%c",&ch);
				//printf("%c",ch);
				picture[j][k]=ch;

			}
			scanf("\n");
			//printf("\n");
		}
		printf("Case #%d:\n", i+1);
		//printf("Case #%d: %d\n", i+1,rpi);
		calcPossible();
		reset();
	}
	return;
}

void calcPossible()
{
	for (int j=0;j<r;j++)
	{
		for (int k=0;k<c;k++)
		{
			if (picture[j][k]=='#')
			{//printf("got here,%c,%c,%c\n",picture[j+1][k],picture[j][k+1],picture[j+1][k+1]);
				if (picture[j+1][k]=='#' && picture[j][k+1]=='#' && picture[j+1][k+1]=='#')
				{//printf("got here 2\n");
					picture[j][k]='/';
					picture[j+1][k]='\\';
					picture[j][k+1]='\\';
					picture[j+1][k+1]='/';
				}
				else
				{
					printf("Impossible\n");
					return;
				}
			}
		}
	}
	for (int j=0;j<r;j++)
	{
		for (int k=0;k<c;k++)
		{
			printf("%c",picture[j][k]);
		}
		printf("\n");
	}
}


void reset()
{
	for (int j=0;j<51;j++)
	{
		for (int k=0;k<51;k++)
		{
			picture[j][k]='\0';
		}
	}
}