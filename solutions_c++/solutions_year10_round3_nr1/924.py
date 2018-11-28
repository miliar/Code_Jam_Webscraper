// round1c_1.cpp : 定义控制台应用程序的入口点。
//
// round1B_1.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
struct node {
	int x;
	int y;
};

node data[1002];

bool comp(node&a, node& b)
{
	if (a.x < b.x)
		return true;
	else 
		return false;
}

int main(int argc, char* argv[])
{
	int testcase;
	
	scanf("%d",&testcase);
	for (int caseId =1 ; caseId <= testcase; caseId++)
	{
		printf("Case #%d:",caseId);
		//*****begin
		int i,j;
		int N;
		cin>>N;
		for (i=0;i<N;i++)
		{
			cin>>data[i].x>>data[i].y;
		}
		sort(data, data+N, comp);
		int count = 0;
		for (i=0; i<N;i++)
		{
			for (j=i+1;j<N;j++)
			{
				if (data[i].y>data[j].y)
					count++;
			}
		}

		//****end
		printf(" %d\n", count );

	}
	return 0;
}


