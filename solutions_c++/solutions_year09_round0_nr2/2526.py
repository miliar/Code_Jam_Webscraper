#include <iostream>
#include <fstream>
using namespace std;
int a[102][102];
char d[100][100];
int t,i,j,h,w,cur;
ifstream fin("input.txt");
ofstream fout("output.txt");
void input()
{
	int k;
	fin>>h>>w;
	for (j=1;j<=h;j++)
		for (k=1;k<=w;k++)
			fin>>a[j][k];
}
char b[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

int dfs(int a0,int b0,int a1,int b1)
{
	int minn=15000;
	pair<int,int> dir;
	if ((a[a1-1][b1]<minn)&&(a[a1][b1]>a[a1-1][b1]))
	{
		dir.first=-1;
		dir.second=0;
		minn=a[a1-1][b1];
	}
	if ((a[a1][b1-1]<minn)&&(a[a1][b1]>a[a1][b1-1]))
	{
		dir.first=0;
		dir.second=-1;
		minn=a[a1][b1-1];
	}
	if ((a[a1][b1+1]<minn)&&(a[a1][b1]>a[a1][b1+1]))
	{
		dir.first=0;
		dir.second=1;
		minn=a[a1][b1+1];
	}
	if ((a[a1+1][b1]<minn)&&(a[a1][b1]>a[a1+1][b1]))
	{
		dir.first=1;
		dir.second=0;
		minn=a[a1+1][b1];
	}
	if (minn<15000)
	{
		if (d[a1+dir.first-1][b1+dir.second-1]=='0')
			return dfs(a0,b0,a1+dir.first,b1+dir.second);
		else
		{
			d[a0-1][b0-1]=d[a1+dir.first-1][b1+dir.second-1];
			return 0;
		}
	}
	else 
	{
		d[a1-1][b1-1]=b[cur];
		d[a0-1][b0-1]=b[cur];
		cur++;
		return 0;
	}
}
int main()
{
	fin>>t;
	for (i=0;i<t;i++)
	{
		for (int i1=0;i1<102;i1++)
			for (j=0;j<102;j++)
				a[i1][j]=15000;
		for (int i1=0;i1<100;i1++)
			for (j=0;j<100;j++)
				d[i1][j]='0';
		input();
		cur=0;
		for (j=1;j<=h;j++)
			for (int i1=1;i1<=w;i1++)
				if (d[j-1][i1-1]=='0')
					dfs(j,i1,j,i1);
		fout<<"Case #"<<i+1<<":"<<endl;
		for (j=0;j<h;j++)
		{
			for (int i1=0;i1<w;i1++)
				fout<<d[j][i1]<<' ';
			fout<<endl;
		}
	}
	return 0;
}