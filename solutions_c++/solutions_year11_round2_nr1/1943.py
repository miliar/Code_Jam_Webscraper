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

void pseudo();
int calcRPI();
void calcWin();
void calcOwin();
void calcOOwin();

int worthUsing(list<node>::iterator);
int useCard(list<node>::iterator);

int main()
{
	pseudo();
	return 0;
}


list<node> teams;
void pseudo()
{
	list<node>::iterator it;
	int numCases=0;
	int n=0;
	char record;
	int num=0;
	int rpi=0;
	scanf("%d\n",&numCases);
	//printf("%d\n",numCases);
	for (int i=0;i<numCases;i++)
	{
		scanf("%d\n",&n);
		//printf("%d\n",n);
		totalteams=n;
		for (int j=0;j<n;j++)
		{
			teams.push_back(node(j));
			it=teams.end();
			it--;
			for (int k=0;k<n;k++)
			{
				scanf("%c", &record);
				//printf("%c", record);
				if (record=='1')
				{
					(*it).record[k]=1;
				}
				else if (record=='0')
				{
					(*it).record[k]=0;
				}
				else
				{
					(*it).record[k]=-1;
				}
			}
			scanf("\n");
			//printf("\n");
		}
		printf("Case #%d:\n", i+1);
		//printf("Case #%d: %d\n", i+1,rpi);
		rpi=calcRPI();
		teams.clear();
	}
	return;
}

int calcRPI()
{
	list<node>::iterator it;
	//it=hand.erase(it);
	int rpi=0;
	calcWin();
	calcOwin();
	calcOOwin();
	for (it=teams.begin();it!=teams.end();it++)
	{
		//printf("num:%d;  %d,%d,%d,%d\n",(*it).teamNum,(*it).record[0],(*it).record[1],(*it).record[2], (*it).record[3]);
		
		(*it).rpi=.25 *(*it).win+ 0.50 * (*it).owin + 0.25 * (*it).oowin;
		//printf("num:%d;    %f,   %f,   %f\n",(*it).teamNum,(*it).win,(*it).owin,(*it).oowin);
		printf("%.10f\n",(*it).rpi);
	}


	return rpi;
}
void calcWin()
{
	list<node>::iterator it;
	double wins;
	double losses;
	for (it=teams.begin();it!=teams.end();it++)
	{
		wins=0;
		losses=0;
		for (int i=0;i<totalteams;i++)
		{
			if ((*it).teamNum!=i)
			{
				if ((*it).record[i]==0)
				{
					losses++;
				}
				else if ((*it).record[i]==1)
				{
					wins++;
				}
			}
		}
		(*it).win=wins/(wins+losses);
		(*it).numOpp=wins+losses;
	}
}
void calcOwin()
{
	list<node>::iterator it;
	list<node>::iterator opp;
	int count=0;
	for (it=teams.begin();it!=teams.end();it++)
	{
		//count=0;
		for (opp=teams.begin();opp!=teams.end();opp++)
		{
			if ((*it).teamNum!=(*opp).teamNum)
			{
				if ((*opp).record[(*it).teamNum]==0)
				{
					(*it).owin+=((((*opp).win*(*opp).numOpp))/((*opp).numOpp-1));
					//printf("win to be added: %f\n",(*opp).win);
					//printf("owin: %f\n",(*it).owin);
				}
				else if ((*opp).record[(*it).teamNum]==1)
				{
					(*it).owin+=((((*opp).win*(*opp).numOpp)-1)/((*opp).numOpp-1));
					//printf("win to be added: %f\n",(*opp).win);
					//printf("owin: %f\n",(*it).owin);
				}
			}
			//count++;
		}
		(*it).owin=(*it).owin/(*it).numOpp;
	}
}


void calcOOwin()
{
	list<node>::iterator it;
	list<node>::iterator opp;
	int count=0;
	for (it=teams.begin();it!=teams.end();it++)
	{
		//count=0;
		for (opp=teams.begin();opp!=teams.end();opp++)
		{
			if ((*it).teamNum!=(*opp).teamNum)
			{
				if ((*opp).record[(*it).teamNum]>=0)
				{
					(*it).oowin+=(*opp).owin;
				}
			}
			//count++;
		}
		(*it).oowin=(*it).oowin/(*it).numOpp;
	}

}