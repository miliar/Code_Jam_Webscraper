/*
 * A.cpp
 *
 *  Created on: May 22, 2011
 *      Author: SICO
 */
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;
char grid [100][100];
int R,C;
int DI[]={0,1,1,0};
int DJ[]={0,0,1,1};
char Col[]={'/','\\','/','\\'};
bool check(int i,int j)
{
	for(int k=0;k<4;++k)
	{
		int ni=i+DI[k];
		int nj=j+DJ[k];
		if(ni <0 || nj<0 || ni>=R || nj>=C ) return false;
		if(grid[ni][nj]!='#')return false;
		grid[ni][nj]=Col[k];
	}
	return true;
}
int main()
{
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;++i)
			scanf("%s",grid[i]);


		bool f=true;
		for(int i=0;i<R;++i)
		{

			for(int j=0;j<C;++j)
			{
				if(grid[i][j]=='#')
				{
					f=true;
					if(!check(i,j))
					{
						//printf("hee\n");
						f=false;
						break;
					}
				}
				if(!f)break;
			}
			if(!f)break;
		}
		printf("Case #%d:\n",x);
		if(!f)printf("Impossible\n");
		else
		{
			for(int i=0;i<R;++i)
			{
					printf("%s\n",grid[i]);

			}
		}
	}

}
