//#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;
ifstream cin("B-small-attempt0.in");
ofstream cout("B-small.out");

//ifstream cin("B-large.in");
//ofstream cout("B-large.out");
int main() {
int T;
int N,L;
int C;
long long t;
cin >> T;

int A[1000000];
for (int i=1; i<=T; i++) {
	cin >> L >> t >> N >> C;
	vector<int> ais;
	for (int c=0; c<C; c++) {
		int ai;
		cin >> ai;
		ais.push_back(ai);
	}
	//before building speed booster
	int cur = 0;
	for (int j=0; j<N; j++) {
		A[j] = ais[cur];
		cur = (cur+1)%C;
	}
	int stationat = 0;
	long long time=0;
	double left = 0;
	while (time < t && stationat <N) {
		left+=0.5;
		if (left == A[stationat]) { stationat++; left = 0; }
		time+=1;
	}
	if (stationat < N) {
	vector<double> dists;
	dists.push_back((double)A[stationat]-left);
	for (int j=stationat+1; j<N; j++) {
		dists.push_back((double)A[j]);
	}
	sort(dists.begin(), dists.end());
	reverse(dists.begin(), dists.end());
	
	for (int j=0; j<dists.size(); j++) {
		if (L>0) {
			time += dists[j];
			L--;
		} else {
			time += 2*dists[j];
		}
	}	
	}
	cout << "Case #"<<i<<": "<<time<<endl;
}
return 0;
}
