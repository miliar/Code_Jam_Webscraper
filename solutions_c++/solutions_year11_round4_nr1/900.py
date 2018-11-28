#include <iostream>
#include <algorithm>
#include <iomanip>
#define EPS 1e-10
using namespace std;

int X, S, R, T, N;
int B[1005], E[1005], w[1005];
int M; //number of distinct speeds w_i, including 0 where theres no walkway

struct WALK {
	double length;
	int speed;
} walk[1005];

struct WALKWAY {
	int length;
	int speed;
} walkway[1005];

bool comp1(WALKWAY a, WALKWAY b) {
	return (a.speed < b.speed);
}

void setWalks() {
	int L = 0;
	for (int i = 0; i < N; i++) {
		walkway[i].length = E[i] - B[i];
		walkway[i].speed = w[i];
		L += walkway[i].length;
		//cout << "L " << L << endl;
	}
	//cout << "L " << L << endl;
	int nopath = X - L;
	sort(walkway, walkway+N, comp1);
	
	M = 2;
	walk[0].length = nopath;
	walk[0].speed = 0;
	walk[1].length = walkway[0].length;
	walk[1].speed = walkway[0].speed;
	for (int i = 1; i < N; i++) {
		if (walkway[i].speed == walkway[i-1].speed) {
			walk[M-1].length += walkway[i].length;
		} else {
			walk[M].length = walkway[i].length;
			walk[M].speed = walkway[i].speed;
			M++;
		}
	}
}


double solveWalk() {
	double tleft = T;
	double TTOT = 0;
	for (int i = 0; i < M; i++) {
		double v = walk[i].speed;
		double l = walk[i].length;
		//cout << "walkway... " << i << " " << v << " " << l << endl;
		if (tleft > EPS) {
			double d = (v + (double)R) * tleft; //max dist we can go
			if (d >= l) { // we can take up this whole thing
				double t = l / (v + (double)R);
				TTOT += t;
				tleft -= t;
			} else {
				// go dist
				walk[i].length -= d;
				TTOT += tleft;
				tleft = 0;
				i--;
			}
		} else {
			// walk across entire thing
			double t = l / (v + (double)S);
			TTOT += t;
		}
	}
	return TTOT;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> X >> S >> R >> T >> N;
		for (int i = 0; i < N; i++) cin >> B[i] >> E[i] >> w[i];
		
		setWalks();
		
		double res = solveWalk();
		
		
		cout << fixed << setprecision(8);
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
