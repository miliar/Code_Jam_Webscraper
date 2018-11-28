#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <list>
#include <cstdlib>
#include <map>
#include <sstream>
#include <string>
#include <bitset>
#include <set>
#include <cmath>
using namespace std;
struct point
{
	long long x,y;
	point(long long a,long long b)
	{
		x=a;y=b;
	}
	point();
};

vector<point> v;
long long A,B,C,D,n,M,X,Y;

void func()
{
	v.push_back(point(X,Y));
	for(int i = 1 ; i<= n-1 ; i++)
  	{
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		v.push_back(point(X,Y));
	}
}

int possible(point a,point b,point c)
{
	long double x,y;
        long double z;
	x = (float)(a.x+b.x+c.x)/3;
	y = (float)(a.y+b.y+c.y)/3;
	return ((modf(x , &z) == 0.) && (modf(y , &z)==0.));
}

long long solve()
{
	long long ret=0;
	for(int i=0 ; i<v.size() ; i++)
	{
		for(int j=i+1;j<v.size();j++)
		{
			for(int k=j+1;k<v.size();k++)
			{
				if(possible(v[i],v[j],v[k]))
					ret++;
			}
		}	
	}
	
	return ret;
}

main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>A>>B>>C>>D>>X>>Y>>M;
		v.clear();
		func();
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
}
