#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}

struct plant{
	int x,y,r;
};

double length(int x1,int y1, int x2, int y2, double r1, double r2) {
	return (sqrt(1.0*(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))+r1+r2)/2;
}
int main() {
	//ifstream cin("in.txt");
	ifstream cin("D-small.in");
	//ifstream cin("D-large.in");
	//ofstream cout("out");
	freopen("out","w",stdout);
	int T, Case;
	int i, j, k, n;
	struct plant p;
	for (cin>>T, Case=1; T; T--,Case++) {
		vector<struct plant> v;
		cin>>n;
		for (i=0; i<n; i++) {
			cin>>p.x>>p.y>>p.r;
			v.push_back(p);
		}
		double r1,r2;
		double res = 2000000000;
		if (n==1) res = v[0].r;
		else if (n==2) {
			res = max(1.0*v[0].r,1.0*v[1].r);
		}
		else {
		r1 = v[0].r;
		r2 = length(v[1].x,v[1].y,v[2].x,v[2].y,v[1].r,v[2].r);
		res = min(res,max(r1,r2));
		//res = max(r2,res);

		r1 = v[1].r;
		r2 = length(v[0].x,v[0].y,v[2].x,v[2].y,v[0].r,v[2].r);
		res = min(res,max(r1,r2));
		//res = max(r2,res);

		r1 = v[2].r;
		r2 = length(v[1].x,v[1].y,v[0].x,v[0].y,v[1].r,v[0].r);
		res = min(res,max(r1,r2));
		//res = max(r2,res);
		}
		printf("Case #%d: %.6lf\n",Case,res);
		//cout<<"Case #"<<Case<<": "<<setprecision(6)<<res<<endl;
	}

}