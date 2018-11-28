// CJ_Q_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>

int way(int *t,int i,int W, int H)
{
	int max = W*H;
	int min = t[i];
	int minpos = i;
	if (i-W>=0)
	{
		if (t[i-W]<min)
		{
			min = t[i-W];
			minpos = i-W;
		}
	}
	if (i%W>0)
	{
		if (t[i-1]<min)
		{
			min = t[i-1];
			minpos = i-1;
		}
	}

	if (i%W<W-1)
	{
		if (t[i+1]<min)
		{
			min = t[i+1];
			minpos = i+1;
		}
	}
	if (i+W<max)
	{
		if (t[i+W]<min)
		{
			min = t[i+W];
			minpos = i+W;
		}
	}

	return minpos;

}
int maxvalue;

void path(int *t,int *to,int j,int H,int W)
{
	int i=j;
	int next=-1;
	int value;
	int list[10000];
	
	for (int ii=0; ii<10000; ii++) list[ii]=-1;

	int k=0; // list length
	list[k] = j; 
	k++;

	if (to[i]!=-1) return;
	bool ok=false;

	
	while (i!=next && !ok)
	{
		next = way(t,i,W,H);
		if (next == i)
		{
			maxvalue++;
			value = maxvalue;
			break;
		}

		if (to[next] != -1) 
		{
			ok=true;
			value = to[next];
		}
		else
		{
			list[k] = next;
			k++;
			i = next; 
			next = -1;
		}
	}

	i=0;
	while (list[i]!=-1)
	{
		to[list[i]] = value;
		i++;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
    fout = fopen("F:\\CodeJam\\\Bl.out","w+b");
    std::string str_in = "F:\\CodeJam\\\B-large.in";
    std::ifstream is(str_in.c_str());
    
    int N,H,W;
	int t[10000];
	int to[10000];
	
    is >> N;//number of cases
	for (int i=0; i<N; i++)
	{
		maxvalue = 0;
		for (int j=0; j<10000; j++)
		{
			t[j]=-1;
			to[j]=-1;		
		}

		is >> H;
		is >> W;
		for (int j=0; j<H*W; j++)
		{
			is >> t[j];
		}

		for (int j=0; j<H*W; j++)
		{
			 path(t,to,j,H,W);
		}

		fprintf(fout,"Case #%d:",i+1);
		for (int j=0; j<H*W; j++)
		{
			if (j%W==0) fprintf(fout,"\n");
			else fprintf(fout," ");
			fprintf(fout,"%c",'a'-1+to[j]);
			
		}

		 fprintf(fout,"\n");
		
	}
	fclose(fout);
	return 0;
}

