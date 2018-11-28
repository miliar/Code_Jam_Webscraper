#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace std;

vector < pair < int, int > > X;
int D,n;

bool checker(double t) {
	double l = -10e9,W;
	for (int i=0;i<X.size();i++) {
		for (int j=0;j<X[i].second;j++) {
			if (X[i].first-t >= l) {
				l = X[i].first-t + D;
			} else if (X[i].first+t>=l) {
				l+=D;
			} else return false;
		}
	}
	return true;
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t,a,b;
	cin >> t;
	for (int z=0;z<t;z++) {
		X.clear();
		cin >> n >> D;
		X.resize(n);
		for (int i=0;i<n;i++)
			cin >> X[i].first >> X[i].second;
		double l=0,r=10e10,c;
		while (fabs(l-r)>10e-11) {
			c = (r + l)/2;
			if (checker(c)) r=c; else l=c;
		}
		//cout << "Case #" << z+1 << ":" << c << endl; 
		printf("Case #%d: %.10lf\n",z+1,c);
	}
}