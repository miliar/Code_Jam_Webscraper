#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;

struct SS{
	int d, w;
};

bool order(SS s1, SS s2){
	return s1.w < s2.w;
}

double solve(double X, double S, double R, double t, int N, vector<int> B, vector<int> E, vector<int> w){
	double result = 0.0;
	
	int Y = 0;
	for(int i = 0; i < N-1; i++){
		Y += B[i+1]-E[i];
	}
	Y += B[0] + X-E[N-1];
	
	vector<SS> v;
	for(int i = 0; i < N; i++){
		SS s = {E[i]-B[i], w[i]};
		v.push_back(s);
	}
	
	sort(v.begin(),v.end(), order);
	
	double now = 0.0;
	double time = (double)Y/R;
	if(t-time >= -EPS){
		result += time;
		t -= time;
	}
	else{
		result += t;
		now += R*t;
		t = 0.0;
		result += ((double)Y-now)/S;
	}
	
	for(int i = 0; i < N; i++){
		now = 0.0;
		double time = double(v[i].d)/(R+(double)v[i].w);
		if(t-time >= -EPS){
			result += time;
			t -= time;
		}
		else{
			result += t;
			now = (R+(double)v[i].w)*t;
			t = 0.0;
			result += ((double)v[i].d-now)/(S+(double)v[i].w);
		}
	}
	return result;
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int a, b, c, d, e;
		cin >> a >> b >> c >> d >> e;
		vector<int> A, B, C;
		for(int i = 0; i < e; i++){
			int aa, bb, cc;
			cin >> aa >> bb >> cc;
			A.push_back(aa);
			B.push_back(bb);
			C.push_back(cc);
		}
//		cout << "Case #" << t << ": " << solve(a, b, c, d, e, A, B, C) << endl;
		printf("Case #%d: %.9f\n", t, solve(a, b, c, d, e, A, B, C));
	}
	return 0;
}
