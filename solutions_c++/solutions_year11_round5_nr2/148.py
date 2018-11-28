#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <list>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <climits>
#include <set>
#include <memory.h>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <map>
#include <cassert>
#include <time.h>
#define _USE_MATH_DEFINES
using namespace std;

typedef long long ll;
typedef pair<double, double> xy_t;
typedef pair<int, int> P;
typedef pair<int, P> PP;
typedef pair<string, int > Ps;
typedef vector<int> vec;
typedef vector<vec> mat;
const int INF = 1 << 30;
const double EPS = 1e-9;

int nums[10002];

int calc(){
	int res = INF;
	int l = 0, r = 0;
	while(true){
		while(!nums[l] && l < 10000) l++;
		if(nums[l] == 0) return res;
		r = l;
		while(nums[r] && nums[r+1] >= nums[r]) r++;
		res = min(res, r - l + 1);
		for(int i = l; i <= r; i++){
			nums[i]--;
		}
	}
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n;
		cin >>n;
		memset(nums, 0, sizeof(nums));
		for(int i = 0; i < n; i++){
			int num;
			cin >> num;
			nums[num]++;
			
		}
		int res = calc();
		if(res == INF) res = 0; 
		cout << "Case #" << t + 1 << ": " << res << endl;
	}
	cin.close();
	cout.close();
	return 0;
}

/*
int W, U, L, G;
xy_t Us[200];
xy_t Ls[200];

double tri_area(xy_t p0, xy_t p1, xy_t p2){
	double dx1 = p1.first - p0.first;
	double dx2 = p2.first - p0.first;
	double dy1 = p1.second - p0.second;
	double dy2 = p2.second - p0.second;
	return (dx1 * dy2 - dx2 * dy1) / 2;
}

double pol_area(vector<xy_t> &p){
	int n = p.size();
	double res = 0.0;
	for(int i = 0; i < n - 2; i++){
		res += tri_area(p[0], p[i+1], p[i+2]);
	}
	return abs(res);
}

double get_area(double px){
	double res = 0;
	int uub = U;
	int ulb = 0;
	int lub = L;
	int llb = 0;
	while(uub - ulb > 1){
		int mb = (uub + ulb) / 2;
		if(Us[mb].first < px) ulb = mb;
		else uub = mb;
	}
	while(lub - llb > 1){
		int mb = (lub + llb) / 2;
		if(Ls[mb].first < px) llb = mb;
		else lub = mb;
	}
	double uy = Us[ulb].second + (px - Us[ulb].first) / 
		(Us[ulb+1].first - Us[ulb].first) * (Us[ulb+1].second - Us[ulb].second);
	double ly = Ls[llb].second + (px - Ls[llb].first) / 
		(Ls[llb+1].first - Ls[llb].first) * (Ls[llb+1].second - Ls[llb].second);
	vector<xy_t> pol;
	for(int i = 0; i <= ulb; i++) pol.push_back(Us[i]);
	pol.push_back(xy_t(px, uy));
	pol.push_back(xy_t(px, ly));
	for(int i = llb; i >= 0; i--) pol.push_back(Ls[i]);
	return pol_area(pol);
}

int main(){
//	ifstream cin("input.txt");
//	ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		cerr << t + 1 << endl;
		cin >> W >> U >> L >> G;
		double x,y;
		for(int i = 0; i < U; i++){
			cin >> x >> y;
			Us[i] = xy_t(x, y);
		}
		for(int i = 0; i < L; i++){
			cin >> x >> y;
			Ls[i] = xy_t(x, y);
		}

		double area = get_area(W);
		
		cout << "Case #" << t + 1 << ":" << fixed << setprecision(6) << endl;
		for(int i = 1; i < G; i++){
	
			double s = area * i / G;
		
			double ub = W;
			double lb = 0;
			for(int j = 0; j < 100; j++){
				double mb = (ub + lb) / 2;
				double ar = get_area(mb);
				if(ar < s + EPS) lb = mb;
				else ub = mb;
			}
			cout << lb << endl;
		}
	}
//	cin.close();
//	cout.close();
	return 0;
}

*/