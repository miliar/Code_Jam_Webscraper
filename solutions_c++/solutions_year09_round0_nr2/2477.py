

#include <iostream>
#include<fstream>
using namespace std;
const int N=150;
const int M=100000;
const int dir[4][2]={{0,-1},{-1,0},{1,0},{0,1}};
int map[N][N];
char result[N][N];
int  father[M];
int  flag[M];
int ncase;
int len,height;
int index=0;
ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");
//*****************************************************
void Init(int num)
{
	for(int i=0;i<=num;++i)
	{
		father[i]=i;
		flag[i]=-1;
	}
}
//******************************************************
int find(int num)
{
	int t=num;
	while(father[t]!=t)
	{
		t=father[t];
	}
	int temp=num;
	int x=0;
	while(temp!=t)
	{
		x=father[temp];
		father[temp]=t;
		temp=x;
	}
	return t;
}
//******************************************************
void solve()
{
	int temp=len*height;
	int m=0;
	int min=0;
		for(int i=0;i<height;++i)
		{
			for(int j=0;j<len;++j)
			{
				min=map[i][j];
				m=i*len+j;
				for(int k=0;k<4;++k)
				{
					int x=j+dir[k][0];
					int y=i+dir[k][1];
					if(x>=0 && x<len && y>=0 &&  y<height && min>map[y][x] )
					{
						min=map[y][x];
						m=y*len+x;
					}
				}
				father[i*len+j]=m;
			}
		}
}
//******************************************************
void sol()
{
	for(int i=0;i<height;++i)
	{
		for(int j=0;j<len;++j)
		{
			int x=find(i*len+j);
			if(flag[x]==-1)
			{
				flag[x]=index++;
			}
			result[i][j]=flag[x]+'a';
		}
	}
}
//*******************************************************
int main()
{
	fin>>ncase;
	int count=0;
	while(ncase--)
	{
		fin>>height>>len;
		for(int i=0;i<height;++i)
		{
			for(int j=0;j<len;++j)
			{
				fin>>map[i][j];
			}
		}
		index=0;
		Init(height*len);
		solve();
		sol();
		fout<<"Case #"<<++count<<":"<<endl;
		for(int i=0;i<height;++i)
		{
			for(int j=0;j<len-1;++j)
				fout<<result[i][j]<<' ';
			fout<<result[i][len-1]<<endl;
		}

	}
	return 0;
}