#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <gmpxx.h>

using namespace std;
using namespace tr1;

typedef mpz_class number;

#define MAX 105

vector <int> adj[MAX];
string m[MAX];
int n;

double WP[MAX], OWP[MAX], OOWP[MAX];

double wp(int i) {
	
	if (WP[i] < -0.5) {
		int wins = 0;
		
		for (int j=0; j < adj[i].size(); j++) {
			wins += (m[i][adj[i][j]] == '1');
		}
		
		WP[i] = wins / (double) adj[i].size();
	}
	
	return WP[i];
}

double owp(int i) {
	
	if (OWP[i] < -0.5) {
		double sum = 0.0;
		
		for (int j=0; j < adj[i].size(); j++) {
			int other = adj[i][j];
			sum += (wp(other) * adj[other].size() - (m[other][i] == '1')) / (adj[other].size() - 1.0);
			//printf("%d <- %d) %lf\n", i, other, (wp(other) * adj[other].size() - (m[other][i] == '1')) / (adj[other].size() - 1.0));
		}
		
		OWP[i] = sum / (double) adj[i].size();
	}
	
	return OWP[i];
}

double oowp(int i) {
	
	if (OOWP[i] < -0.5) {
		double sum = 0.0;
		
		for (int j=0; j < adj[i].size(); j++) {
			sum += owp(adj[i][j]);
		}
		
		OOWP[i] = sum / adj[i].size();
	}
	
	return OOWP[i];
}

double rpi(int i) {
	return 0.25 * wp(i) + 0.5 * owp(i) + 0.25 * oowp(i);
}

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		
		cin >> n;
		
		for (int i=0; i < n; i++) {
			cin >> m[i];
			
			adj[i].clear();
			for (int j=0; j < n; j++) {
				if (m[i][j] != '.') {
					adj[i].push_back(j);
				}
			}
			
			WP[i] = OWP[i] = OOWP[i] = -1.0;
		}
		
		printf("Case #%d:\n",t++);
		
		for (int i=0; i < n; i++) {
			printf("%.9lf\n",rpi(i));
		}
	}
	
	return 0;
}
