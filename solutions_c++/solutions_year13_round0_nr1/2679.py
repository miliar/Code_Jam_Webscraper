#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <queue>
#include <cstdio>


#define sqr(t) ((t)*(t))
#define INF INT_MAX
using namespace std;

int i, j, q, poi, X, O, n, p;
char arr[10][10];

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>n;
	for (q=0; q<n; q++)
	for (int r=0; r<=0; r++)
	{
		poi=0;
		p=0;
		for (i=0; i<4; i++)
			for (j=0; j<4; j++)
				cin>>arr[i][j];

		for (i=0; i<4; i++)
		{
			O=0;
			X=0;
			for (j=0; j<4; j++)
			{
				if (arr[i][j]=='O')
					O++;
				if (arr[i][j]=='X')
					X++;
				if (arr[i][j]=='T')
				{
					X++;
					O++;
				}
				if (arr[i][j]=='.')
					poi++;
			}
			if (p!=1)
			if (X==4)
			{
				cout<<"Case #"<<q+1<<": X won"<<endl;
				p=1;
			}
			if (p!=1)
			if (O==4)
			{
				cout<<"Case #"<<q+1<<": O won"<<endl;
				p=1;
			}
		}
		O=0;
		X=0;
		for (j=0; j<4; j++)
		{
			O=0;
			X=0;
			for (i=0; i<4; i++)
			{
				if (arr[i][j]=='O')
					O++;
				if (arr[i][j]=='X')
					X++;
				if (arr[i][j]=='T')
				{
					X++;
					O++;
				}
				if (arr[i][j]=='.')
					poi++;
			}
			if (p!=1)
			if (X==4)
			{
				cout<<"Case #"<<q+1<<": X won"<<endl;
				p=1;
			}
			if (p!=1)
			if (O==4)
			{
				cout<<"Case #"<<q+1<<": O won"<<endl;
				p=1;
			}
		}
		O=0;
		X=0;
		for (i=0; i<4; i++)
		{
			if (arr[i][i]=='O')
				O++;
			if (arr[i][i]=='X')
				X++;
			if (arr[i][i]=='T')
			{
				X++;
				O++;
			}
			if (arr[i][i]=='.')
				poi++;
		}
		if (p!=1)
		if (X==4)
		{
			cout<<"Case #"<<q+1<<": X won"<<endl;
			p=1;
		}
		if (p!=1)
		if (O==4)
		{
			cout<<"Case #"<<q+1<<": O won"<<endl;
			p=1;
		}

		O=0;
		X=0;
		for (i=0; i<4; i++)
		{
			if (arr[i][3-i]=='O')
				O++;
			if (arr[i][3-i]=='X')
				X++;
			if (arr[i][3-i]=='T')
			{
				X++;
				O++;
			}
			if (arr[i][3-i]=='.')
				poi++;
		}
		if (p!=1)
		if (X==4)
		{
			cout<<"Case #"<<q+1<<": X won"<<endl;
			p=1;
		}
		if (p!=1)
		if (O==4)
		{
			cout<<"Case #"<<q+1<<": O won"<<endl;
			p=1;
		}
		if (p!=1)
		if (poi>0)
			cout<<"Case #"<<q+1<<": Game has not completed"<<endl;
		else
			cout<<"Case #"<<q+1<<": Draw"<<endl;
	}
}