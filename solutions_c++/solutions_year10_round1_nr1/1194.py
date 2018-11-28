#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)


ifstream fin;
ofstream fout;

int a[60][60];
int red;
int blue;
int n,k;


void check(int cc)
{
	int i,j,l;
	int find;
	find=0;

	for(j=n-1;j>=0;j--)
	{
		if(a[n-1][j]==0)
			continue;
		for(i=n-1;i>=0;i--)
		{
			if(a[i][j]!=cc)
				continue;
			find=1;
			for(l=1;l<k;l++)
			{
				if(a[i][j-l]!=cc)
				{find=0;break;}
			}
			if(find==1)
			{
				red=red+cc;return;
			}
			find=1;
			for(l=1;l<k;l++)
			{
				if(a[i-l][j]!=cc)
				{find=0;break;}
			}
			if(find==1)
			{
				red=red+cc;return;
			}
		}
	}

	for(j=n-k;j>=0;j--)
	{
		if(a[n-1][j]==0)
			continue;
		for(i=n-1;i>=0;i--)
		{
			if(a[i][j]!=cc)
				continue;
			find=1;
			for(l=1;l<k;l++)
			{
				if(a[i-l][j+l]!=cc)
				{find=0;break;}
			}
			if(find==1)
			{
				red=red+cc;return;
			}
			if(i>n-k)
				continue;
			find=1;
			for(l=1;l<k;l++)
			{
				if(a[i+l][j+1]!=cc)
				{find=0;break;}
			}
			if(find==1)
			{
				red=red+cc;return;
			}
		}
	}
}

void main()
{
	fin.open("b.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con;
	int i,j;
	char c;
	int l;
	
	fin>>cases;
	rep(con,cases)
	{

		fin>>n>>k;
		red=0;
		blue=0;
		rep(i,n)			
		{
			rep(j,n)
			{
				fin>>c;
				if(c=='.')
					a[i][j]=0;
				else if(c=='R')
					a[i][j]=1;
				else
					a[i][j]=2;
			}

		}
		rep(i,n)
		{
			l=n-1;
			for(j=n-1;j>=0;j--)
			{
				if(a[i][j]==0)
					continue;
				if(l==j)
				{l--;continue;}
				a[i][l]=a[i][j];
				a[i][j]=0;
				l--;
			}
		}

		check(1);
		check(2);

		if(red==0)
		{fout<<"Case #"<<con+1<<": Neither"<<endl;}
		else if(red==1)
		{fout<<"Case #"<<con+1<<": Red"<<endl;}
		else if(red==2)
		{fout<<"Case #"<<con+1<<": Blue"<<endl;}
		else
		{fout<<"Case #"<<con+1<<": Both"<<endl;}

	}
	return;
}