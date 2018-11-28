#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

double xs[64],ys[64],rs[64];

double dist(int a, int b)
{
	double x=xs[a]-xs[b];
	double y=ys[a]-ys[b];
	return sqrt(x*x+y*y);
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		int n;cin>>n;
		for(int i=0; i<n; ++i)
			cin>>xs[i]>>ys[i]>>rs[i];
		double res=0;
		if (n==1) res=rs[0];
		else if (n==2) res=max(rs[0],rs[1]);
		else if (n==3) {
			res=1e50;
			for(int i=0; i<3; ++i) {
				int j=i==0?1:0;
				int k=j==1||i==1?2:1;
				res = min(res, max(rs[i], .5*(dist(j,k)+rs[j]+rs[k])));
			}
		}
		else cerr<<"fail\n";

		printf("Case #%d: %.8f\n", a, res);
	}
}
