// geo.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
#define for if(1)for
#define printf
struct XY
{
	XY(int i,int j):x(i),y(j)
{}
	int x;
	int y;
};
int lowest(int c,int n,int w,int e,int s)
{
	int m=c>n?n:c;
	m = m>w?w:m;
	m = m>e?e:m;
	m = m>s?s:m;
	return m;
}
void sinkbas(vector<vector<int> > &vi,vector<vector<char> >&vo,int x,int y, vector<XY>&vxy, char&ch)
{
	int c = vi[x][y];
	int n=10000;
	vxy.push_back(XY(x,y));
	if(0!=x)
	{
		n =vi[x-1][y];
	}
	int w=10000;
	if(0!=y)
	{
		w =vi[x][y-1];
	}
	int e=10000;
	if(y<vi[0].size()-1)
	{
		e =vi[x][y+1];
	}
	int s=10000;
	if(x<vi.size()-1)
	{
		s =vi[x+1][y];
	}

	int l=lowest( c, n, w, e, s);
	do
	{
		char chtmp=vo[x][y];

		if(l == c)
		{
			
			if(chtmp==0)
			{
				chtmp = ch;
				++ch;
			}
			for(int i=0;i<vxy.size();++i)
			{
				vo[vxy[i].x][vxy[i].y] =chtmp;
			}
			return;
		}
		//north
		if(l == n)
		{
			chtmp=vo[x-1][y];
			vxy.push_back(XY(x-1,y));
			if(chtmp!=0)
			{
				
				for(int i=0;i<vxy.size();++i)
				{
					vo[vxy[i].x][vxy[i].y]=chtmp;
				}
				return;
			}
			
			sinkbas(vi,vo,x-1,y,vxy,ch);
			break;

		}
		//west
		if(l == w)
		{
			chtmp=vo[x][y-1];
			vxy.push_back(XY(x,y-1));
			if(chtmp!=0)
			{
				
				for(int i=0;i<vxy.size();++i)
				{
					vo[vxy[i].x][vxy[i].y]=chtmp;
				}
				return;
			}
			
			sinkbas(vi,vo,x,y-1,vxy,ch);
			break;

		}
		//east
		if(l == e)
		{
			chtmp=vo[x][y+1];
			vxy.push_back(XY(x,y+1));
			if(chtmp!=0)
			{
				
				for(int i=0;i<vxy.size();++i)
				{
					vo[vxy[i].x][vxy[i].y]=chtmp;
				}
				return;
			}
			
			sinkbas(vi,vo,x,y+1,vxy,ch);
			break;

		}
		//north
		if(l == s)
		{
			chtmp=vo[x+1][y];
			vxy.push_back(XY(x+1,y));
			if(chtmp!=0)
			{
				
				for(int i=0;i<vxy.size();++i)
				{
					vo[vxy[i].x][vxy[i].y]=chtmp;
				}
				return;
			}
			
			sinkbas(vi,vo,x+1,y,vxy,ch);
			break;

		}
	}while(0);
}
void sinkcal(vector<vector<int> > &vi,vector<vector<char> >&vo)
{
	char ch = 'a';
	for(int i=0;i<vi.size();++i)
	{
		
		for(int j=0;j<vi[i].size();++j)
		{
			vector<XY>vxy;
			sinkbas(vi,vo,i,j,vxy,ch);
			
		}

	}
}
int main(int argc, char* argv[])
{
	FILE*pfn=NULL;
	pfn=fopen("test.txt","r");
	int t = 0;

	fscanf(pfn,"%d",&t);
	vector<vector<vector<int> > >vs;
	vector<vector<vector<char> > >vout;
	vs.resize(t);
	vout.resize(t);
	for(int i=0;i<t;++i)
	{
		int h=0;
		int w = 0;
		fscanf(pfn,"%d %d",&h,&w);
		printf("w=%d,h=%d\n",w,h);
		vs[i].resize(h);
		vout[i].resize(h);
		for(int j=0;j<h;++j)
		{
			vs[i][j].resize(w);
			vout[i][j].resize(w);
		}
		for(int k=0;k<h;++k)
		{
			for(int l=0;l<w;++l)
			{
				fscanf(pfn,"%d",&(vs[i][k][l]));
				printf("vs[%d][%d][%d]=%d ",i,k,l,vs[i][k][l]);
			}
			printf("\n");
		}

	}
	fclose(pfn);
	for(int i=0;i<t;++i)
	{
		sinkcal(vs[i],vout[i]);
	}
	pfn=fopen("result.txt","w");
	for(int i=0;i<t;++i)
	{
		fprintf(pfn,"Case #%d:\n",i+1);
		printf("Case #%d:\n",i+1);
			int h=vout[i].size();

		int w = vout[i][0].size();
		for(int j=0;j<h;++j)
		{
			for(int l=0;l<w-1;++l)
			{
				fprintf(pfn,"%c ",vout[i][j][l]);
				printf("%c ",vout[i][j][l]);

			}
			fprintf(pfn,"%c\n",vout[i][j][w-1]);
			printf("%c\n",vout[i][j][w-1]);
		}
	}
	fclose(pfn);
	return 0;
}


