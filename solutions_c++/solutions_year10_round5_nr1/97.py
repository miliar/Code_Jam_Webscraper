#include <cassert>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#pragma comment(linker, "/STACK:10000000")
using namespace std;

__int64 gcd (__int64 a, __int64 b, __int64 & x, __int64 & y)
{
	if (a == 0)
	{
		x = 0; 
		y = 1;
		return b;
	}
	__int64 x1, y1;
	__int64 d = gcd (b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}
__int64 mod(__int64 a, __int64 p)
{
	a %= p;
	if (a < 0)
		a += p;
	return a;
}
__int64 inv(__int64 a, __int64 p)
{
	__int64 x,y;
	gcd(a,p,x,y);
	return mod(x, p);
}

vector<pair<__int64, __int64> > vs;

bool getNext(__int64 p, __int64 &v)
{
	vector<pair<__int64, __int64> > vp = vs;
	for (int i=1;i<(int)vp.size();i++)
	{
		vp[i].first = mod(vp[i].first - vp[0].first, p);
		vp[i].second = mod(vp[i].second - vp[0].second, p);
	}
	bool bHas = false;
	__int64 a = 0;
	for (int i=1;i<(int)vp.size();i++)
		if (vp[i].first != 0)
		{
			bHas = true;
			a = mod(inv(vp[i].first, p) * vp[i].second,p);
			break;
		}
	if (!bHas)
	{
		throw 0;
		v = 0;
		return false;
	}

	for (int i=1;i<(int)vp.size();i++)
		if (mod(vp[i].first * a, p) != vp[i].second)
			return false;

	__int64 b = mod(vp[0].second - a * vp[0].first, p);
	v = mod(a*vs.back().second + b, p);
	return true;
}
bool isPrime(__int64 n)
{
	if (n == 1)
		return false;
	for (__int64 i = 2;i*i <= n && i < n;i++)
		if (n % i == 0)
			return false;
	return true;
}

int main()
{ 
/*	time_t ct = time(0);
	int dt =5*60 + 0*1800 +0*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		cout<<char(7);
	}
	return 0;*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tn;
	cin>>tn;
	for (int aaa=0;aaa<tn;aaa++)
	{
		int d,k;
		cin>>d>>k;
		set<__int64> res;
		vs.resize(k);
		for (int i=0;i<k;i++)
			cin>>vs[i].first;
		
		__int64 mx = 0;
		for (int i=0;i<k;i++)
			mx = max(mx, vs[i].first);

		int d10 = 1;
		for (int i=0;i<d;i++)
			d10 *= 10;

		if (k == 1)
		{
			cout<<"Case #"<<aaa+1<<": "<<"I don't know."<<endl;
			continue;
		}

		bool allEq = true;
		for (int i=0;i<k;i++)
			if (mx != vs[i].first)
				allEq = false;
		if (allEq)
		{
			cout<<"Case #"<<aaa+1<<": "<<vs[0].first<<endl;
			continue;
		}
		if (k == 2)
		{
			cout<<"Case #"<<aaa+1<<": "<<"I don't know."<<endl;
			continue;
		}
		for (int i=0;i<k - 1;i++)
			vs[i].second = vs[i+1].first;
		vs.resize(k - 1);

		__int64 ans;
		for (__int64 i = mx + 1;i < d10;i++)
			if (isPrime(i))
				if (getNext(i, ans))
					res.insert(ans);

		if (!res.size())
			throw 0;
		if (res.size() > 1)
		{
			cout<<"Case #"<<aaa+1<<": "<<"I don't know."<<endl;
			continue;
		}
		cout<<"Case #"<<aaa+1<<": "<<*res.begin()<<endl;
	}

	return 0;
}