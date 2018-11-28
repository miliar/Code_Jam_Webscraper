#include <ios>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

bool map[105][105],save[105][105];
FILE *fin, *fout;
void solve()
{
	int n,i,j;
	int X1,Y1,X2,Y2;
	fscanf(fin,"%d",&n);
	memset(map,false,sizeof(map));
	while(n--)
	{
		fscanf(fin,"%d%d%d%d",&X1,&Y1,&X2,&Y2);
		for(i=X1;i<=X2;i++)
			for(j=Y1;j<=Y2;j++)
				map[i][j]=true;
	}
	int days=0;
	bool flag=true;
	while(flag)
	{
		flag=false;
		for(i=1;i<=100;i++)
			for(j=1;j<=100;j++)
			{
				if(map[i][j])
				{
					if(map[i-1][j]||map[i][j-1])
						save[i][j]=true;
					else
						save[i][j]=false;
				}
				else
				{
					if(map[i-1][j]&&map[i][j-1])
						save[i][j]=true;
					else
						save[i][j]=false;
				}
				if(save[i][j])
					flag=true;
			}
		for(i=1;i<=100;i++)
			for(j=1;j<=100;j++)
				map[i][j]=save[i][j];
		days++;
	}
	fprintf(fout,"%d\n",days);
}

int main()
{
	fin = fopen("\C-small-attempt0.in","r");
	fout = fopen("\C-small-attempt0.out","w");

	int t,cnt=0;
	fscanf(fin,"%d",&t);
	while (t--)
	{
		fprintf(fout,"Case #%d: ",++cnt);
		solve();
	}
}
