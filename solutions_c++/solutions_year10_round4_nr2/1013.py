// 0605_1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <map>
#include <vector>
#include <stdlib.h>
#include <iostream>
#define  INT64 long long
using namespace std;

#define MSET(p) memset(p,0,sizeof(p))
int t[10][1024];
int m[1024];
int _tmain(int argc, _TCHAR* argv[])
{
	char databuffer[16*1024];
	int iNumOfCases;int R,C;
	INT64 iTemp,iResult;
	char * p;
	int i,j,l,k,r,q,it;
	int x,y;
	freopen("test.txt","r+",stdin);
	freopen("out.txt","w+",stdout);

	cin>>iNumOfCases;

	for (int iIndex1 = 1;iIndex1 <= iNumOfCases;iIndex1++)
	{
		MSET(t);
		MSET(m);

		iResult = 0;
		printf("Case #%d: ",iIndex1);
		cin>>r;
		x = (int)pow((double)2,(double)r);
		for (j = 0;j<x;j++)
		{
			cin>>y;
			m[j] = r - y ;
		}
		x/=2;
		l = 0;
		while(x>0)
		{
			for (j = 0;j<x;j++)
			{
				cin>>t[l][j];
			}
			l++;
			x/=2;
		}
		x = (int)pow((double)2,(double)r);
		j = 0;
		while(j != x)
		{
			it = x;
			for ( j = 0;j <x;j++)
			{
				int imax = 0;
				if (m[j] > imax)
					it = j;
			}
			j = it;
			for (k = r-1;k>=0;k--)
			{
				y = (int)pow((double)2,k+1);
				if (t[k][j/y] > 0)
				{
					iResult +=t[k][j/y] ;
					t[k][j/y] = 0;
					for (q = 0;q<x;q++)
					{
						if (q/y == j/y)
						{
							m[q]--;
						}
					}
					break;
				}
			}
		}
		
		char num[64];
		_i64toa(iResult,num,10);
		memset(databuffer,0,sizeof(databuffer));
		sprintf(databuffer,"%s\n",num);
		printf(databuffer);
	}

	fflush(stdout);
	return 0;
}

