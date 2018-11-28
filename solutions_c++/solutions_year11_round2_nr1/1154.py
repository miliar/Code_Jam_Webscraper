#include <iostream>
#include <vector>
#include <cctype>
#include <map>
#include <algorithm>
#include <cstdio>

using namespace std;

double calcWP(vector<string> &V, int p) {
	int s = 0;
	int count = 0;
	for(int i = 0; i < V.size(); ++i) {
		if(V[p][i] != '.') {
			count++;
			s += V[p][i]-'0';
		}
	}
	return double(s) / double(count);
}

double calcOWP(vector<string> &V, int p) {
	double r = 0;
	int s = 0, s2 = 0;
	int count = 0, c2 = 0;
	for(int i = 0; i < V.size(); ++i) {
		if(V[p][i] != '.') {
			count++;
			c2 = 0;
			s2 = 0;
			for(int j = 0; j < V.size(); ++j) {
				if(V[i][j] != '.' && j != p) {
					c2++;
					s2 += V[i][j]-'0';
				}
			}
			r += double(s2)/double(c2);
		}
	}
	return r/double(count);	
}

double calcOOWP(vector<string> &V, int p) {
	double r = 0;
	double count = 0;
	for(int i = 0; i < V.size(); ++i) {
		if(V[p][i] != '.') {
			r += calcOWP(V, i);
			count++;
		}
	}
	return r /double(count);
}

int main() {
	int T, N;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i+1 << ": " << endl;
		cin >> N;
		vector <string> V(N);
		string tmp;
		for(int j = 0; j < N; ++j) {
			cin >> V[j];
		}
		for(int j = 0; j < N; ++j) {
			double RPI = 0.25*calcWP(V, j)+0.5*calcOWP(V, j)+0.25*calcOOWP(V, j);
			cout << RPI << endl;
		} 
	}
	return 0;
}