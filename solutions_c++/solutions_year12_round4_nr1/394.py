#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

struct V
{
	double p;
	double l;
};

bool operator<(const V& v1, const V& v2)
{
	return v1.p < v2.p;
}

int n, D;
V	a[10100];
double maxGo[10100];
double maxL[10100];

void fill(int i)
{
	int j;
	double maxG = 0, maxLL=0, d;
	maxGo[i] = maxL[i] =0;
	for(j=0; j<i; ++j)
		if(maxGo[j] >= a[i].p)
		{
			d = min(a[i].l, a[i].p - a[j].p);
			if(maxG < d + a[i].p || (maxG == d + a[i].p && maxLL < d))
			{
				maxG = d + a[i].p;
				maxLL = d;
			}
		}
	maxGo[i] = maxG;
	maxL[i] = maxLL;
}

int main()
{
	int i;
	int t,tt;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>n;
		for(i=0; i<n; ++i)
			fin>>a[i].p>>a[i].l;
		fin>>D;
		sort(a, a+n);

		maxGo[0] = 0;
		maxL[0] = 0;

		if(a[0].l >= a[0].p)
		{
			maxGo[0] = a[0].p * 2;
			maxL[0] = a[0].p;
		}

		for(i=1; i<n; ++i)
			fill(i);

		for(i=0; i<n; ++i)
			if(maxGo[i] >= D)
				break;

		if(i < n)
			fout<<"Case #"<<t<<": "<<"YES"<<endl;
		else
			fout<<"Case #"<<t<<": "<<"NO"<<endl;
	}
	return 0;
}