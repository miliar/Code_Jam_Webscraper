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
	int note;
	node(int Note)
	{
		note=Note;
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

void harmony();
void calcHarmony();


int worthUsing(list<node>::iterator);
int useCard(list<node>::iterator);

int main()
{
	harmony();
	return 0;
}


list<node> notes;
int l, h, n;
void harmony()
{
	list<node>::iterator it;
	int numCases=0;
	int freq=0;
	int orch=0;
	scanf("%d\n",&numCases);
	//printf("%d\n",numCases);
	for (int i=0;i<numCases;i++)
	{
		scanf("%d %d %d\n",&n, &l, &h);
		//printf("%d %d %d\n",n, l, h);
		for (int j=0;j<n;j++)
		{
			scanf("%d",&orch);
			//printf("%d ",orch);
			notes.push_back(node(orch));
		}
		scanf("\n");
		//printf("\n");
		printf("Case #%d: ", i+1);
		calcHarmony();
		notes.clear();
	}
	return;
}

void calcHarmony()
{
	int freq=-1;
	list<node>::iterator it;
	for (int i=l;i<=h;i++)
	{//printf("i=%d\n",i);
		for (it=notes.begin();it!=notes.end();it++)
		{
			if((*it).note%i!=0 && i%(*it).note!=0)
			{//printf("got here,%d, %d, %d\n",i,(*it).note%i,i%(*it).note);
				break;
			}
		}
		if (it==notes.end())
		{//printf("got here\n");
			freq=i;
			printf("%d\n",freq);
			return;
		}
	}
	printf("NO\n");
}