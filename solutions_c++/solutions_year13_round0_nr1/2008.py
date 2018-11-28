#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;
int row(int a);
int col(int a);
int dia1();
int dia2();
char a[4][4];
int main()
{
	int tc,j,i,l=0,k,tp;
	ifstream ifile("d:/tic.txt");
	ofstream ofile("d:/tac.txt");
	ifile>>tc;
	
	for (j=0;j<tc;j++)
	{
		tp=0;
		l=0;
		for (i=0;i<4;i++)
		ifile>>a[i];
		
		i=0;
		while (l==0&&i<4)
		{
			l=row(i);
			i++;
		}
		i=0;
		while (l==0&&i<4)
		{
			l=col(i);
			i++;
		}
		if (l==0)
		l=dia1();
		if (l==0)
		l=dia2();
		
		if (l==1)
		ofile<<"Case #"<<j+1<<": X won"<<endl;
		
		else if (l==2)
		ofile<<"Case #"<<j+1<<": O won"<<endl;
		
		else if (l==0)
		{
			for (i=0;i<4;i++)
			{
				for (k=0;k<4;k++)
				if (a[i][k]=='.')
				{
					ofile<<"Case #"<<j+1<<": Game has not completed"<<endl;
					tp=1;
					break;
				}
				if (tp==1)
				break;
			}
			if (tp==0)
			{
				ofile<<"Case #"<<j+1<<": Draw"<<endl;
			}
		}
		
	}
	return 0;
}


int row (int n)
{
	int j=0;
	while (j<4&&(a[n][j]=='X'||a[n][j]=='T'))
	++j;
	if (j==4)
	return 1;
	else
	{
		j=0;
		while (j<4&&(a[n][j]=='O'||a[n][j]=='T'))
		++j;
		if (j==4)
		return 2;
		else
		return 0;
	}
}


int col(int n)
{
	int j=0;
	while (j<4&&(a[j][n]=='X'||a[j][n]=='T'))
	++j;
	if (j==4)
	return 1;
	else
	{
		j=0;
		while (j<4&&(a[j][n]=='O'||a[j][n]=='T'))
		++j;
		if (j==4)
		return 2;
		else
		return 0;
	}
}


int dia1()
{
	int i=0,j=0;
	while (i<4&&j<4&&(a[i][j]=='X'||a[i][j]=='T'))
	{
		++i;
		++j;
	}
	if (i==4)
	return 1;
	else
	{
		i=0;
		j=0;
		while (i<4&&j<4&&(a[i][j]=='O'||a[i][j]=='T'))
		{
			++i;
			++j;
		}
		if (i==4)
		return 2;
		else
		return 0;
	}
}

int dia2()
{
	int i=0,j=3;
	while (i<4&&j>=0&&(a[i][j]=='X'||a[i][j]=='T'))
	{
		++i;
		--j;
	}
	if (i==4)
	return 1;
	else
	{
		i=0;
		j=3;
		while (i<4&&j>=0&&(a[i][j]=='O'||a[i][j]=='T'))
		{
			++i;
			--j;
		}
		if (i==4)
		return 2;
		else
		return 0;
	}
}

