// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>
#include <vector>

struct point
{
	long long int x;
	long long int y;
};

std::vector<point> mypoints;

void points (long long int x0,long long int y0, long long int n, long long int A,long long  int B,long long  int C,long long  int D,long long  int M)
{
	long long int X = x0;
	long long int Y = y0;

	point p;
	p.x = X;
	p.y = Y;
	mypoints.clear();
	mypoints.push_back(p);
	for (int i = 1; i< n; i++)
	{
	  X = (A * X + B) % M ;
	  Y = (C * Y + D) % M ;
	  point p;
	  p.x = X;
	  p.y = Y;
	  mypoints.push_back(p);
	}
}


int _tmain(int argc, _TCHAR* argv[])
{

	FILE * fout;
	fout = fopen("d:\\A2out.txt","w+b");
	std::string str_in = "d:\\A-small-attempt1.in";
	//std::string str_in = "d:\\A1.in";
	std::ifstream is(str_in.c_str());
	long long int N;
	
	is >> N;//number of cases


	for (int i=0; i<N; i++)
	{
		long long int n, A, B, C, D, x0, y0, M ;
		is >> n;
		is >> A;
		is >> B;
		is >> C;
		is >> D;
		is >> x0;
		is >> y0;
		is >> M;

		
		points(x0,y0,n,A,B,C,D,M);
		int trias = 0;
		for (int j=0; j<n-2; j++)
		{
			for (int k=j+1; k<n-1; k++)
			{
				for (int l=k+1; l<n; l++)
				{
					long long int centerx = mypoints[j].x + mypoints[k].x + mypoints[l].x;
					long long int centery = mypoints[j].y + mypoints[k].y + mypoints[l].y;
					if (centerx%3==0 && centery%3==0)
					{
						trias ++;
					}
				}
			}			
		}

		fprintf(fout,"Case #%d: %d\r\n",i+1,trias);
	}

	fclose(fout);

	return 0;
}

