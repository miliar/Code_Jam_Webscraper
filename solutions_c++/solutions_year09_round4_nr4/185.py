#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

struct Circle{
	double x, y, r;
}c[100];
double calc_dist(Circle c1, Circle c2){
	double x1 = c1.x-c2.x, y1 = c1.y-c2.y;
	double d = sqrt(x1*x1+y1*y1);
	return d+c1.r+c2.r;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int T, N, K, i, j, k;
	cin>>T;
	double ans, t1, t2, t3;
	for(int t = 1; t <= T; ++t){
		cin>>N;
		for(i = 0; i < N; ++i){
			cin>>c[i].x>>c[i].y>>c[i].r;
		}
		if(N == 1){
			ans = c[0].r;
		}else if(N == 2){
			ans = max(c[0].r, c[1].r);
		}else {
			t1 = calc_dist(c[0], c[1])/2;
			t1 >?= c[2].r;
			t2 = calc_dist(c[0], c[2])/2;
			t2 >?= c[1].r;
			t3 = calc_dist(c[2], c[1])/2;
			t3 >?= c[0].r;
			ans = min(min(t1, t2), t3);
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
