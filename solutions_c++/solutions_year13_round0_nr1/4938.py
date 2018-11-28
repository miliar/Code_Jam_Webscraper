#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<fstream>
#include<string>

using namespace std;


int main()
{
	char a[4][4];

	int n;

	cin >> n;

	for(int i=1;i<=n;i++)
	{

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				cin >> a[j][k];
		}

		int xflag=1;

		for(int j=0;j<4;j++)
		{
			int f=1;
			for(int k=0;k<4;k++)
			{
				if (a[j][k]!='X' && a[j][k]!='T')
					f=0;
			}
			if (f==1)
			{
				xflag=0;
				break;
			}
		}
		for(int j=0;j<4;j++)
		{
			int f=1;
			for(int k=0;k<4;k++)
			{
				if (a[k][j]!='X' && a[k][j]!='T')
					f=0;
			}
			if (f==1)
			{
				xflag=0;
				break;
			}
		}
		int f=1;
		for(int j=0;j<4;j++)
		{
			if (a[j][j]!='X' && a[j][j]!='T')
				f=0;
		}
		if (f==1)
		{
			xflag=0;
		}

		f=1;
		if (a[0][3]!='X' && a[0][3]!='T')
			f=0;
		if (a[1][2]!='X' && a[1][2]!='T')
			f=0;
		if (a[2][1]!='X' && a[2][1]!='T')
			f=0;
		if (a[3][0]!='X' && a[3][0]!='T')
			f=0;
		if (f==1)
		{
			xflag=0;
		}
		if (xflag==0)
		{
			cout << "Case #" << i <<": X won\n";
			continue;
		}

		xflag=1;

		for(int j=0;j<4;j++)
		{
			int f=1;
			for(int k=0;k<4;k++)
			{
				if (a[j][k]!='O' && a[j][k]!='T')
					f=0;
			}
			if (f==1)
			{
				xflag=0;
				break;
			}
		}
		for(int j=0;j<4;j++)
		{
			int f=1;
			for(int k=0;k<4;k++)
			{
				if (a[k][j]!='O' && a[k][j]!='T')
					f=0;
			}
			if (f==1)
			{
				xflag=0;
				break;
			}
		}
		f=1;
		for(int j=0;j<4;j++)
		{
			if (a[j][j]!='O' && a[j][j]!='T')
				f=0;
		}
		if (f==1)
		{
			xflag=0;
		}

		f=1;
		if (a[0][3]!='O' && a[0][3]!='T')
			f=0;
		if (a[1][2]!='O' && a[1][2]!='T')
			f=0;
		if (a[2][1]!='O' && a[2][1]!='T')
			f=0;
		if (a[3][0]!='O' && a[3][0]!='T')
			f=0;
		if (f==1)
		{
			xflag=0;
		}
		if (xflag==0)
		{
			cout << "Case #" << i <<": O won\n";
			continue;
		}
		xflag=1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if (a[j][k]=='.')
					xflag=0;
			}
		}
		if (xflag==1)
		{
			cout << "Case #" << i <<": Draw\n";
			continue;
		}
		else
		{
			cout << "Case #" << i <<": Game has not completed\n";
			continue;
		}



	}

	return 0;
}
