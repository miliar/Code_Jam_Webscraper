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

int main() {
	//ifstream cin("in.txt");
	//ifstream cin("B-small.in");
	ifstream cin("B-large.in");
	//ofstream cout("out");
	freopen("out.txt","w",stdout);
	int T, Case, N;
	int x, y, z, vx, vy, vz;
	long long sx, sy, sz, svx, svy, svz;
	double t, d;
	int i, j, k;
	for (cin>>T, Case=1; T; T--,Case++) {
		cin>>N;
		sx = sy = sz = svx = svy = svz =0;
		for (i=0; i<N; i++) {
			cin>>x>>y>>z>>vx>>vy>>vz;
			sx += x, sy += y, sz += z, svx += vx, svy += vy, svz += vz;
		}
		long long a = -1*(2*sx*svx+2*sy*svy+2*sz*svz);
		long long b = 2*(svx*svx+svy*svy+svz*svz);
		if (a<0 || b==0) t=0,d= sqrt(1.0*sx*sx+sy*sy+sz*sz)/N;
		else {
			t = 1.0*a/b;
			d = sqrt(1.0*(sx+t*svx)*(sx+t*svx)+(sy+t*svy)*(sy+t*svy)+(sz+t*svz)*(sz+t*svz))/N;
		}
		printf("Case #%d: %.8lf %.8lf\n",Case,d,t);
		//cout<<"Case #"<<Case<<": "<<d<<" "<<t<<endl;
	}

}