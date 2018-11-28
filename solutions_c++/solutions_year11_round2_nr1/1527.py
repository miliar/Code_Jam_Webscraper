#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <cstring>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int n;
double wp[100], owp[100], oowp[100];
char sc[100][100];

double WPCalc(int i, int ignore) {
	double total = 0;
	int wins = 0;
	
	for(int j = 0; j < n; j++) {
		if(ignore == j)
			continue;

		if(sc[i][j] != '.') {
			total += 1;
			if(sc[i][j] == '1')
				wins++;
		}
	}
	return (wins/total);
}

double OWPCalc(int i) {
	int total = 0;
	double sum = 0;
	
	for(int j=0; j < n; j++) {
		if(sc[i][j] != '.') {
			total++;
			sum += WPCalc(j, i);
		}
	}
	return (sum/total);
}

double OOWPCalc(int i) {
	int total = 0;
	double sum = 0;

	for(int j=0; j<n; j++) {
		if(sc[i][j] != '.') {
			total++;
			sum += owp[j];
		}
	}
	return (sum/total);
}

int main() {
	int t;
	cin>>t;

	for(int i = 0; i < t; i++) {
		cin >> n;
		
		for(int j = 0; j < n; j++) {
			for(int k = 0; k < n; k++) {
				cin>>sc[j][k];
			}
		}

		for(int j = 0; j < n; j++)
			wp[j] = WPCalc(j,-1);

		for(int j=0; j< n; j++)
			owp[j] = OWPCalc(j);

		for(int j=0; j< n; j++)
			oowp[j] = OOWPCalc(j);

		cout<<"Case #"<<i+1<<":"<<endl;
		
		for(int j=0; j<n; j++) {
			cout<<(0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j])<<endl;
		}
	}
}
