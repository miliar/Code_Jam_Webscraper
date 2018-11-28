#include <stdio.h>
#include <math.h> 
#include <iostream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>

using namespace std;

int n,m,a; 
int x,y;
int x2,y2,x3,y3;
bool possible;

void PrintResult(int i)
{		cout<<"Case #"<<i<<": ";
		if(!possible)
			cout<<"IMPOSSIBLE";
		else
			cout<<"0 0 "<<x2<<" "<<y2<<" "<<x3<<" "<<y3;
		cout<<"\n";
}


void SolveTriangle()
{
	possible=false;
	if (n*m<a)
		return;
	x=n;y=m;
	possible=true;
	if (n*m==a)
		return;
	for(x=1;x<=n;++x)
	{
		y=a/x;
		double check=double(x)*double(y);
		if(check==a)
			return;
	}
	possible=false;
}

void SolveTriangle2()
{
	possible=true;
	double t;
	for(x3=0;x3<=n;++x3)
	{
		for(x2=x3+1;x2<=n;++x2)
		{
			for(y3=0;y3<=m;++y3)
			{
				for(y2=0;y2<=y3-1;++y2)
				{
					t=2*x2*y3-x3*y3-y2*x2-(x2-x3)*(y3-y2);
					if(t==a)
						return;
				}
				{
					y2=y3;
					t=2*x2*y2-y2*x3-y2*x2;
					if(t==a)
						return;
				}
				for(y2=y3+1;y2<=m;++y2)
				{
					t=2*x2*y2-2*x3*(y2-y3)-(x2-x3)*(y2-y3)-x3*y3-x2*y2;
					if(t==a)
						return;
				}
			}
		}
		{
			x2=x3;
			for(y2=0;y2<=m-1;++y2)
			{
				for(y3=y2+1;y3<=m;++y3)
				{
					t=2*x2*y3-x2*y3-x2*y2;
					if(t==a)
						return;
				}
			}
		}
	}
	possible=false;
}

void SolveTriangles()
{
	/*SolveTriangle();
	if(possible)
	{
		x2=x;
		y2=0;
		x3=0;
		y3=y;
		return;
	}*/
	SolveTriangle2();
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int N;
	cin>>N;

	for(int i=1;i<=N;++i)
	{
		cin>>n>>m>>a;
		SolveTriangles();
		PrintResult(i);
	}
	return 0;
}
