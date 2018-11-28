#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <cmath>

using namespace std;
#define  MAX 55

int main()
{
	ifstream cin("e:\\aa.in");
	ofstream cout("e:\\aa.out");

	int T;
	cin>>T;
	int i,j,k;
	for (i=0;i<T;i++)
	{
		int R,C;
		cin>>R>>C;
		char tables[MAX][MAX];
		memset(tables,0,sizeof(tables));
		for (j=0;j<R;j++)
		{
			cin>>tables[j];
		}
		for (j=0;j<C+1;j++)
		{
			tables[R][j]='.';
			tables[R+1][j]='\0';
		}
		for (j=0;j<R+1;j++)
		{
			tables[j][C]='.';
			tables[j][C+1]='\0';
		}
		bool ok=true;
		for (j=0;j<R;j++)
		{
			for (k=0;k<C;k++)
			{
				if(tables[j][k]=='.')
					continue;
				if (tables[j][k]=='/' || tables[j][k]=='\\')
					continue;
				
				if (tables[j][k]=='#' && 
					tables[j][k+1]=='#' &&
					tables[j+1][k]=='#' &&
					tables[j+1][k+1]=='#')
				{
					tables[j][k]='/';
					tables[j][k+1]='\\';
					tables[j+1][k]='\\';
					tables[j+1][k+1]='/';
				}
				else
				{
					ok=false;
					break;
				}
					
			}
			if(!ok)
				break;
		}
		cout<<"Case #"<<(i+1)<<":"<<endl;
		if(!ok)
			 cout<<"Impossible"<<endl;
		else
		{
			
			for (j=0;j<R;j++)
			{
				tables[j][C]='\0';
			}
			for(j=0;j<R;j++)
				cout<<tables[j]<<endl;
		}
	}
	return 0;
}