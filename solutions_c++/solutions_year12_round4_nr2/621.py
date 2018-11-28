#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i,n) for(int i=0; i < (n); ++i)

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

double my_rand()
{
	return double(rand()) / RAND_MAX;
}

void solve()
{
	int n;
	double w, l;
	double r[2000];

	double x[2000], y[2000];

	cin >> n >> w >> l;
	REP(i,n) cin >> r[i];

	//sort(r+0, r+n, greater<double>());
	
	x[0] = y[0] = 0;

	for(int i = 1; i < n; ++i) {
		x[i] = my_rand() * w;
		y[i] = my_rand() * l;
		int push_count = 0;
		bool pushed = true;
		while(pushed) {
			++push_count;
			if(push_count > 10) {
				push_count = 0;
				x[i] = my_rand() * w;
				y[i] = my_rand() * l;
			}
			pushed = false;
			for(int j = 0; j < i; ++j) {
				double dx = x[i] - x[j];
				double dy = y[i] - y[j];
				double dr = r[i] + r[j];
				double len_sq = dx*dx+dy*dy;
				if(len_sq >= dr*dr) {
					// pull
				}
				else {
					double len = ::sqrt(len_sq);
					dr *= 1.0001;
					dx *= (dr / len);
					dy *= (dr / len);
					x[i] = x[j] + dx;
					y[i] = y[j] + dy;

					if(x[i] < 0 || x[i] > w || y[i] < 0 || y[i] > l) {
						push_count = 0;
						x[i] = my_rand() * w;
						y[i] = my_rand() * l;
					}

					pushed = true;
				}
			}
		}
	}
/*
	// check
	REP(i,n) {
		REP(j, n) {
			if(i == j) continue;
			double dx = x[i] - x[j];
			double dy = y[i] - y[j];
			double dr = r[i] + r[j];
			if(dx * dx + dy * dy < dr * dr) cout << "NO!!" << endl;
		}
		if(x[i] < 0 || x[i] > w || y[i] < 0 || y[i] > l) cout << "NO2!!" << endl;
	}
*/
	REP(i,n) {
		cout << x[i] << " " << y[i] << " ";
	}
	cout << endl;
}

int main(int argc, char *argv[])
{
	srand(1);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

