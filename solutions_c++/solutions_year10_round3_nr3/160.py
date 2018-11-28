// Making Chess Boards.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("outdata.txt");

int t;
int n;
int m;
int map[513][513];
int size[513][513];
int num[513];
int maxsize;
int maxi;
int maxj;
int leftnum;
int total;
int toint(char c)
{
	if(c>='0'&&c<='9')
		return int(c-48);
	else
		return int(c-'A'+10);
}



void init()
{
	for(int i=1;i<=m;i++)
		for(int j=1;j<=n;j++)
		{
			if(map[i][j]==-1)
				continue;

			if(i==1||j==1||map[i-1][j-1]==-1||map[i-1][j-1]!=map[i][j])
				size[i][j]=1;
			else
			{
				int col=0;
				int row=0;
				int orc=i-1;
				int orr=j-1;
				while(row<size[i-1][j-1]&&map[i][orr]!=map[i][orr+1]&&map[i][orr]!=-1)
				{
					row++;
					orr--;
				}
				while(col<size[i-1][j-1]&&map[orc][j]!=map[orc+1][j]&&map[orc][j]!=-1)
				{
					col++;
					orc--;
				}
				size[i][j]=min(col,row)+1;

			}
			

			if(size[i][j]>maxsize)
				{
					maxsize=size[i][j];
					maxi=i;
					maxj=j;		
			     }
		}
}
int _tmain(int argc, _TCHAR* argv[])
{
	fin>>t;
	int tn=1;
	while(tn<=t)
	{
		fin>>m>>n;
		memset(num,0,sizeof(num));

		string s;
		for(int i=1;i<=m;i++)
		{
			fin>>s;
			int len=s.length();
			int temp;
			for(int j=0;j<=len-1;j++)
			{
				temp=toint(s[j]);
				for(int k=4;k>=1;k--)
				{
					map[i][j*4+k]=temp%2;
					temp=temp/2;
				}
			}
		}
		
		total=0;
		leftnum=m*n;
		int lastsize=0;
		while(leftnum>0)
		{

			maxsize=0;
			init();
			if(maxsize!=lastsize)
				total++;
			lastsize=maxsize;

			if(maxsize==1)
			{
				num[maxsize]=leftnum;
				break;
			}
			
			num[maxsize]++;
			leftnum-=maxsize*maxsize;
			for(int i=maxi;i>maxi-maxsize;i--)
				for(int j=maxj;j>maxj-maxsize;j--)
					map[i][j]=-1;

		}
		
		fout<<"Case #"<<tn<<": "<<total<<endl;
		int nm=max(m,n);
		for(int i=nm;i>=1;i--)
			if(num[i]>0)
				fout<<i<<' '<<num[i]<<endl;
		tn++;
	}
	return 0;
}

