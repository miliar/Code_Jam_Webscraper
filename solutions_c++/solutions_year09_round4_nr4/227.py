// progd.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"




#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");

int n;
double xv[100];
double yv[100];
double rv[100];

int sols[30000][2];
double solv[30000];
int curr;

double x,y,r;

void mk()
{
	
	int a=0;
	int i;
	for(i=0;i<20 && i<n; i++)
	{
		if( (xv[i]-x)*(xv[i]-x)+(yv[i]-y)*(yv[i]-y) <= (r+1e-9-rv[i])*(r+1e-9-rv[i]) && r>rv[i]-1e-9)
			a+=(1<<i);
		//cout << (xv[i]-x)*(xv[i]-x)+(yv[i]-y)*(yv[i]-y) << " " << (r+1e-9-rv[i])*(r+1e-9-rv[i]) << endl;
	}
	sols[curr][0]=a;
	a=0;
	for(i=20;i<40 && i<n; i++)
	{
		if( (xv[i]-x)*(xv[i]-x)+(yv[i]-y)*(yv[i]-y) <= (r+1e-9-rv[i])*(r+1e-9-rv[i]) && r>rv[i]-1e-9)
			a+=(1<<(i-20));
	}
	sols[curr][1]=a;
	solv[curr]=r;
	//cout << x << " " << y << " " << r << endl;
	//cout << sols[curr][0] << endl;
	curr++;
	return;
}

void mk2(int a, int b)
{
	double d= (xv[a]-xv[b])*(xv[a]-xv[b])+(yv[a]-yv[b])*(yv[a]-yv[b]);
	d=sqrt(d);
	d+=rv[a]+rv[b];
	d/=2;
	r=d;
	d=2*r-rv[a]-rv[b];
	//cout << d << endl;
	if(d<1e-9)
	{
		x=xv[a];
		y=yv[a];
	}
	else
	{
		x=(r-rv[a])/d*xv[b]+(r-rv[b])/d*xv[a];
		y=(r-rv[a])/d*yv[b]+(r-rv[b])/d*yv[a];
	}
	return;
}

void mk3(int a, int b, int c)
{
	return;
}

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	while(ttt>0)
	{
		ct++;
		ttt--;
		
		int i,j,k,m;
		double d;
		cout.precision(10);
		fout.precision(10);
		memset(sols,0,sizeof(sols));
		cin >> n;
		for(i=0; i<n; i++)
		{
				cin >> xv[i] >> yv[i] >> rv[i];
				//cout << xv[i] << " " << yv[i] << " " << rv[i] << endl;
		}
		curr = 0;
		for(i=0; i<n; i++)
		{
			x=xv[i];
			y=yv[i];
			r=rv[i];
			
			mk();
			
		}
		for(i=0; i<n;i++)
		{
			for(j=i+1; j<n; j++)
			{
				mk2(i,j);
				mk();
			}
		}
		/*for(i=0; i<n;i++)
		{
			for(j=i+1; j<n; j++)
			{
				for(k=j+1; k<n; k++)
				{
					mk3(i,j,k);
					mk();
				}
			}
		}*/
		double ans = 100000.0;
		int a,b;
		if(n>20)
		{
			a=(1<<(20))-1;
			b=(1<<(n-20))-1;
		}
		else
		{
			a=(1<<n)-1;
			b=0;
		}
		for(i=0;i<curr; i++)
		{
			for(j=0; j<curr; j++)
			{
				if((sols[i][0]|sols[j][0])==a && (sols[i][1]|sols[j][1])==b)
				{
					if(solv[i]<solv[j])
						d=solv[j];
					else
						d=solv[i];
					if(d<ans)
						ans=d;
				}
			}
		}
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

