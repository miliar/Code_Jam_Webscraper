#include <iostream>
#include <cstring>
#include <cstdio>
#include <utility>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <string>

#define F first
#define S second

using namespace std;
typedef long long int ll;

string board[110];

typedef pair<double,double> II;
vector<II> hot;

double d;
bool ok(double t)
{
	double rborder = -1e25, lborder = -1e25;
	for(int i = 0; i < hot.size(); i++)
	{
		double lpos = max(rborder+d, hot[i].F-t), rpos = lpos + d*(hot[i].S-1.);
		if(rpos>hot[i].F+t+1e-14) return false;
/*		if(fabs(lpos-hot[i].F)>t+1e-9) return false;
		if(fabs(rpos-hot[i].F)>t+1e-9) return false;*/
		rborder = rpos;
		lborder = lpos;
	}
	return true;
}

int main () {
	int t;
	cin >> t;
	for(int caso = 1; caso <= t; caso++) {
		int c;
		cin >> c >> d;
		hot.clear();
		for(int i = 0; i < c; i++)
		{
			double p,co;
			cin >> p >> co;
			hot.push_back(II(p,co));
		}
		sort(hot.begin(),hot.end());
		double lo = 0., hi = 1e25;
		for(int it = 0; it < 10000; it++)
		{
			double mid = (lo+hi)/2.;
			if(ok(mid))
			{
				hi = mid;
			} else {
				lo = mid;
			}
		}
		printf("Case #%d: %.12lf\n", caso, lo);
	}
	return 0;
}
