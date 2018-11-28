#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;

const int nmax = 3;

struct circle{
	int x,y,r;
};

circle a[nmax];

double dist(circle a,circle b){
	return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y) + 0.0);
}

bool belong(circle a,circle b){
	return (dist(a,b) + b.r + 0.0 <= a.r + 0.0);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int ntest;
	cin >> ntest;

	for (int test = 1;test <= ntest; ++test){
		int n;
		cin >> n;
		for (int i = 0;i < n; ++i) cin >> a[i].x >> a[i].y >> a[i].r;
		printf("Case #%i: ",test);
		if (n == 1) printf("%.6lf\n",a[0].r + 0.0);
		else
		if (n == 2) printf("%.6lf\n",max(a[0].r,a[1].r) + 0.0);
		else {
			double mi = 1e+10;

			for (int i = 0;i < 3; ++i)
				for (int j = i+1;j < 3; ++j)
				for (int k = 0;k < 3; ++k) if (k !=i && k !=j){
					double cur;
					if (belong(a[i],a[j]) || belong(a[j],a[i]))
						cur = max(a[i].r,a[j].r);
					else 
						cur = (dist(a[i],a[j]) + a[i].r + a[j].r + 0.0) / 2;
					cur = max(cur,a[k].r+0.0);
					if (cur < mi) mi = cur;
				}
			printf("%.6lf\n",mi);
		}
	}
	
	return 0;
}