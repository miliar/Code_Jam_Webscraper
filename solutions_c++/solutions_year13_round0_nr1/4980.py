#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>
#include <fstream>

using namespace std;

typedef  unsigned int uint;

char gstate[4][4];

uint state(char input)
{
    uint i,j,k,incnt,tcnt;

	/* hang ; */
    for(i = 0;i<4;i++)
    {
        incnt = 0;
		tcnt = 0;
        for(j = 0;j < 4;j++)
        {
            if(input == gstate[i][j])
            {
                incnt++;
            }
			else if('T' == gstate[i][j])
			{
			    tcnt++;
			}
        }

		if((4 == (incnt+tcnt))&&(tcnt<=1))
		{return 1;}
    }


	/* lie ; */
    for(i = 0;i<4;i++)
    {
        incnt = 0;
		tcnt = 0;
        for(j = 0;j < 4;j++)
        {
            if(input == gstate[j][i])
            {
                incnt++;
            }
			else if('T' == gstate[j][i])
			{
			    tcnt++;
			}
        }

		if((4 == (incnt+tcnt))&&(tcnt<=1))
		{return 1;}
    }


	/* dui jiao*/
	incnt = 0;
	tcnt = 0;
	for(i= 0;i<4;i++)
	{
	    if(input == gstate[i][i])
        {
            incnt++;
        }
		else if('T' == gstate[i][i])
		{
		    tcnt++;
		}
	}
	if((4 == (incnt+tcnt))&&(tcnt<=1))
	{return 1;}
	/* fan - dui jiao*/
	incnt = 0;
	tcnt = 0;
	for(i= 0;i<4;i++)
	{
	    if(input == gstate[i][3-i])
        {
            incnt++;
        }
		else if('T' == gstate[i][3-i])
		{
		    tcnt++;
		}
	}
	if((4 == (incnt+tcnt))&&(tcnt<=1))
	{return 1;}


	return 0;
}

void main()
{
    uint t,tidx;
	uint i,j,k;
	uint remain;
	uint xwin,owin;
	fstream testfin,testfout;

    testfout.open("out.txt",ios::out);
	testfin.open("A-large.in",ios::in);

    testfin >> t;

    
	for(tidx = 1;tidx < (t+1);tidx++)
	{
	    remain = 0;
		xwin = 0;
		owin = 0;

		/* remain detection; */
	    for(i = 0;i < 4;i++)
	    {
	        for(j = 0;j < 4;j++)
    	    {
    	        testfin >> gstate[i][j];
    	        if('.' == gstate[i][j])
    	        {remain = 1;}
    	    }
	    }

		/* state detection; */
		xwin = state('X');
		owin = state('O');

		if((1 == xwin)&&(1 == owin))
		{testfout << "Errrrrrrrrrrrrrrr" << endl;return;}

		if(1 == remain)
		{
		    if(1 == xwin)
		    {testfout << "Case #" << tidx << ": X won"  << endl;}
			else if(1 == owin)
			{testfout << "Case #" << tidx << ": O won"  << endl;}
			else
			{testfout << "Case #" << tidx << ": Game has not completed"  << endl;}
		}
		else
		{
		    if(1 == xwin)
		    {testfout << "Case #" << tidx << ": X won"  << endl;}
			else if(1 == owin)
			{testfout << "Case #" << tidx << ": O won"  << endl;}
			else
			{testfout << "Case #" << tidx << ": Draw"  << endl;}
		}

		
	    
	}

	
}