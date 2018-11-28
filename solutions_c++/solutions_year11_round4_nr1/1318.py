#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int n;
double x, s, r, t;
vector< pair< pair<double, double>, double > > v;
vector< pair< double, pair<double, double> > > v2, v3;

double solvecase(){
	double ans = 0;
	v.clear(); v2.clear(); v3.clear();
	cin >> x >> s >> r >> t >> n;
	for(int i=0; i<n; i++){
		double b, e, w;
		cin >> b >> e >> w;
		v.push_back(make_pair(make_pair(b, e), w));
	}
	v.push_back(make_pair(make_pair(x, x), 0));
	sort(v.begin(), v.end());
	double curx = 0;
	for(int i=0; i<v.size(); i++){
		if(v[i].first.first!=curx){
			v2.push_back(make_pair(0, make_pair(curx, v[i].first.first)));			
		}
		if(v[i].first.first!=v[i].first.second)
			v2.push_back(make_pair(v[i].second, make_pair(v[i].first.first, v[i].first.second)));
		curx = v[i].first.second;
	}
	sort(v2.begin(), v2.end());
	for(int i=0; i<v2.size(); i++){
		double X = v2[i].second.second - v2[i].second.first;
		double vel = r+v2[i].first;
		double tt = X/vel;
		if(tt<=t){
			t-=tt;
			ans += tt;
		} else {
			ans += t;
			double curx = vel*t;
			t = 0;
			X = v2[i].second.second - v2[i].second.first - curx;
			ans += X/(s+v2[i].first);
		}
	}
	return ans;
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t;
	cin >> t;
	for(int q=0; q<t; q++){
		cout << "Case #" << q+1 << ": ";
		double ans = solvecase();
		printf("%.8lf", ans);
		cout << endl;
	}
	return 0;
}