// round1c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int **mat;
struct Line
{
	int a,b;
}*lines;


int calc(int N)
{
	int count=0,i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(mat[i][j]==1 || mat[i][j]==-1 || i==j)
				continue;
			if((lines[i].a < lines[j].a && lines[i].b > lines[j].b) || (lines[i].a > lines[j].a && lines[i].b < lines[j].b))
			{
				count++;
				mat[i][j] = 1;
				mat[j][i] = 1;
			}
			else
			{
				mat[i][j]=-1;
				mat[j][i]=-1;
			}
		}
	}
	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0,N=0,K=0,i,j;
	string line;
	ifstream myfile ("example.txt");
	ofstream outfile("out.txt");
	if (myfile.is_open())
	{
		getline (myfile,line);
		T = atoi(line.c_str()); 
		for(i=0; i<T; i++)
		{
			getline (myfile,line);
			N = atoi(line.c_str());
			lines = new struct Line[N];

			for(j=0;j<N;j++)
			{
				getline (myfile,line);
				char *pch = (char *)line.c_str();
				lines[j].a = atoi(strtok (pch," "));
				lines[j].b = atoi(strtok (NULL," "));
			}
			
			mat = (int **)malloc(N * sizeof(int *));
			for(j=0;j<N;j++)
			{
				mat[j] = new int[N];
				mat[j][j] = 0;
			}
			int ret = calc(N);
			outfile << "Case #" << i+1 << ": " << ret << endl;
		}
		myfile.close();
		outfile.close();
	}
	return 0;
	return 0;
}

