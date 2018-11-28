#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<fstream>
using namespace std;
double s[500];
int n;
#define EPS 1e-9
bool can(int i, double x){
	double s1;
	s1 = s[i] + x;
	double k = 0;
	for(int j = 0; j < n; j++){
		if(s[j] + EPS < s1){
			k += (s1 - s[j]);
		}
	}
	if(k + EPS > 1.)
		return true;
	return false;
}

double bs(int i){
	double l = 0, h = 1. + EPS;
	for(int j = 0; j < 200; j++){
		double m = (l + h) / 2.;
		if(can(i, m))
			h = m;
		else
			l = m;
	}
	return l;
}
int main(){
	
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> n;
		double all = 0;
		for(int i = 0; i < n; i++){
			cin >> s[i];
			all += s[i];
		}
		for(int i = 0; i < n; i++)
			s[i] /= all;
		cout << "Case #" << i + 1 << ":";
	//	cout.precision(7);
		cout.flags(ios::fixed);
		for(int i = 0; i < n; i++)
			cout << " " << bs(i) * 100.;
		cout << endl;
	}
	return 0;
}
		