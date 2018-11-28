#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <stack>
#include <assert.h>
#include <iomanip>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

struct Pos
{
	long double t;
	long double x;
	long double v;
};

long double D;
long double a;
int N;
Pos	p[3000];

long double dist(const Pos& p, long double dt)
{
	return dt * (p.v + a*dt*0.5);
}

long double getTime(long double l, long double v0)
{
	long double Disk = sqrt(4*v0*v0 + 8*a*l);
	long double ans = (Disk -2*v0)/(2*a);
	return ans;
}

long double solve()
{
	int i;
	long double d, dt;
	Pos current;
	current.t = 0;
	current.x = 0;
	current.v = 0;

	for(i=1; i<N; ++i)
	{
		p[i].v = (p[i].x - p[i-1].x) / (p[i].t - p[i-1].t);
		if(p[i].x <= D)
		{
			 dt = p[i].t - p[i-1].t;
			 d = dist(current, dt);
			 if(current.x + d <= p[i].x)
			 {
				 current.x += d;
				 current.t = p[i].t;
				 current.v = current.v + a*dt;
			 }
			 else
			 {
				 long double tt = getTime(p[i].x - current.x, current.v);
				 current.v = current.v + a*tt;
				current.x = p[i].x;
				current.t = p[i].t;
				//current.v = p[i].v;
			 }
		}
		else
		{
			if(D > p[i-1].x)
			{
				dt = (D - p[i-1].x) / p[i].v;
				d = dist(current, dt);
				if(current.x + d <= D)
				{
					current.t = current.t + getTime(D - current.x, current.v);
					current.x = D;
				}
				else
				{
					current.x = D;
					current.t = p[i-1].t + dt;
					current.v = p[i].v;
				}
			}
			else
			{
						current.t = current.t + getTime(D - current.x, current.v);
					current.x = D;
			}
		}
		if(current.x == D)
			break;
	}
	if(current.x != D)
	{
		current.t = current.t + getTime(D - current.x, current.v);
		current.x = D;
	}
	return current.t;
}

void read()
{
	int t,k,i,j,m;
	fin>>t;
	for(k=1; k<=t; ++k)
	{
		fout<<"Case #"<<k<<":"<<endl;
		fin>>D;
		fin>>N>>m;
		for(i=0; i<N; ++i)
			fin>>p[i].t>>p[i].x;
		for(j=0; j<m; ++j)
		{
			fin>>a;
			fout<<setprecision(10)<<solve()<<endl;
		}
	}
}

int main()
{
	read();
	return 0;
}