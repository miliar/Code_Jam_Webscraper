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

bool has[6000000];
int val[6000000];




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
		memset(has, 0, sizeof(has));
		memset(val, 0, sizeof(val));

		set<pair<int, int> > sp;

		int n;
		cin>>n;
		__int64 sum = 0;
		for (int i=0;i<n;i++)
		{
			int t,v;
			cin>>t>>v;
			t += 3000000;

			int v2 = v / 2;
			for (int i=0;i<=v2;i++)
				sum += i * i;
			for (int i=-v2;i<=v2;i++)
			{
				if (v2 + v2 == v && i == 0)
					continue;
				has[t+i] = true;
				++val[t+i];
			}
		}
		for (int i=0;i<6000000;i++)
			if (has[i])
				sp.insert(make_pair(-val[i], i));


		while (sp.begin()->first != -1)
		{
			int v = - sp.begin()->first;
			int w = sp.begin()->second;
			sp.erase(sp.begin());
			if (has[w - 1])
				sp.erase(make_pair(-val[w-1], w-1));
			if (has[w + 1])
				sp.erase(make_pair(-val[w+1], w+1));

			int dv = v >> 1;
			v -= dv + dv;

			has[w] = false;
			val[w] = v;

			if (v != 0)
			{
				sp.insert(make_pair(-v, w));
				has[w] = true;
			}

			val[w-1] += dv;
			val[w+1] += dv;
			has[w-1] = true;
			has[w+1] = true;
			sp.insert(make_pair(-val[w-1], w-1));
			sp.insert(make_pair(-val[w+1], w+1));
			sum += dv;
		}


		cout<<"Case #"<<aaa+1<<": "<<sum<<endl;
	}

	return 0;
}