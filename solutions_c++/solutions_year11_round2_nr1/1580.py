#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

double RPI(double WP, double OWP, double OOWP) {
	return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
}

int main() {
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	cin >> tests;
	for(int test = 0; test < tests; test++) {
		int n;
		cin >> n;
		vector< vector<int> > a;
		a.resize(n);
		for(int i = 0; i < n; i++) {
			string inputRow;
			cin >> inputRow;
			a[i].resize(n);
			for(int j = 0; j < n; j++) {
				if(inputRow[j] == '1') {
					a[i][j] = 1;
				}else if (inputRow[j] == '0') {
					a[i][j] = 0;
				}else {
					a[i][j] = -1;
				}
			}
		}
		vector<double> WP(n);
		vector<double> OWP(n);
		vector<double> OOWP(n);
		for(int i = 0; i < n; i++) {
			double wins = 0;
			double allGames = 0;
			for(int j = 0; j < n; j++) {
				if(a[i][j] >= 0)
					allGames++;
				if(a[i][j] == 1)
					wins++;
			}
			if(allGames == 0)
				WP[i] = 0;
			else
				WP[i] = wins/allGames;
		}
		vector< vector<double> > _OWP(n);
		for(int i = 0; i < n; i++) {
			_OWP[i].resize(n, -1);
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(i == j || a[i][j] == -1)
					continue;
				double wins = 0;
				double allGames = 0;
				for(int k = 0; k < n; k++) {
					if(k == i) 
						continue;
					if(a[j][k] >= 0)
						allGames++;
					if(a[j][k] == 1)
						wins++;
				}
				if(allGames == 0)
					_OWP[i][j] = 0;
				else
					_OWP[i][j] = wins/allGames;
			}
			double tOWP = 0;
			double tGames = 0;
			for(int j = 0; j < n; j++) {
				if(_OWP[i][j] != -1) {
					tGames++;
					tOWP += _OWP[i][j];
				}
			}
			if(tGames == 0)
				OWP[i] = 0;
			else
				OWP[i] = tOWP / tGames;
		}
		for(int i = 0; i < n; i++) {
			double tOWP = 0;
			double allGames = 0;
			for(int j = 0; j < n; j++) {
				if(a[i][j] == -1)
					continue;
				tOWP += OWP[j];
				allGames++;
			}
			if(allGames == 0)
				OOWP[i] = 0;
			else
				OOWP[i] = tOWP / allGames;
		}
		cout << "Case #" << test + 1 << ":\n";
		for(int i = 0; i < n; i++) {
			printf("%.12lf\n",RPI(WP[i], OWP[i], OOWP[i]));
		}
	}

}