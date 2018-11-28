#include<iostream>
#include<fstream>
#include<cstring>
#define MAXX 2147483647
using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
int W,H,id;
int res[10000],a[10000];//res为0表示'a',初始值为-1
int go(int xy)
{
	int x,y,nxy,nx,ny,min=MAXX,zxy;
	x=xy%W;y=xy/W;

	//1:
	nx=x;ny=y-1;nxy=ny*W+nx;
	if(ny>=0)
	{
		if(a[nxy]<min)
		{
			min=a[nxy];
			zxy=nxy;
		}
	}
	//2:
	nx=x-1;ny=y;nxy=ny*W+nx;
	if(nx>=0)
	{
		if(a[nxy]<min)
		{
			min=a[nxy];
			zxy=nxy;
		}
	}

	//3:
	nx=x+1;ny=y;nxy=ny*W+nx;
	if(nx<=W-1)
	{
		if(a[nxy]<min)
		{
			min=a[nxy];
			zxy=nxy;
		}
	}
	//4:
	nx=x;ny=y+1;nxy=ny*W+nx;
	if(ny<=H-1)
	{
		if(a[nxy]<min)
		{
			min=a[nxy];
			zxy=nxy;
		}
	}	

	if(a[xy]<=min)
	{
		res[xy]=id;
		id++;
		return res[xy];
	}
	else
	{
		if(res[zxy]==-1)
		res[xy]=go(zxy);
		else res[xy]=res[zxy];
		return res[xy];
	}
}
int main()
{
	int N,i,k,j,t;
	fin>>N;
	for(k=1;k<=N;k++)
	{
		fin>>H>>W;
		for(i=0;i<=H-1;i++)
		{
			for(j=0;j<=W-1;j++)
			{
				fin>>a[i*W+j];
			}
		}
		memset(res,-1,sizeof(res[0])*H*W);
		t=0;id=0;
		while(t<=H*W-1)
		{
			go(t);
			while(res[t]!=-1&&t<=H*W-1)t++;
		}
		fout<<"Case #"<<k<<":\n";
		for(i=0;i<=H-1;i++)
		{
			for(j=0;j<=W-1;j++)
			{
				fout<<char(res[i*W+j]+'a')<<' ';
			}
			fout<<endl;
		}
	}
	return 0;
}
