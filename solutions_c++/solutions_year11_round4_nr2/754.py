#include <iostream>
#include <string>
#define EPS 1e-9
using namespace std;

int R, C, D;
double m[600][600];
double cm_x[2][600][600]; //use a boolean to swap flags instead
double cm_y[2][600][600];
double mass[2][600][600];

bool flag;

bool Equals(double x, double y) {
	if (x-EPS <= y && x+EPS >= y) return true;
	return false;
}

bool setK3() {
	int K = 3;
	flag = 0;
	bool res = false;
	for (int i = 0; i+K <= R; i++)
		for (int j = 0; j+K <= C; j++) {
			double geom_x = i + 1.5;
			double geom_y = j + 1.5;
			double M = m[i][j+1] + m[i+1][j] + m[i+1][j+1] + m[i+1][j+2] + m[i+2][j+1]; 
			cm_x[flag][i][j] =
				((i+.5)*m[i][j+1] + (i+1.5)*m[i+1][j] + (i+1.5)*m[i+1][j+1] + (i+1.5)*m[i+1][j+2] + (i+2.5)*m[i+2][j+1]) / M;
			cm_y[flag][i][j] =
				((j+1.5)*m[i][j+1] + (j+.5)*m[i+1][j] + (j+1.5)*m[i+1][j+1] + (j+2.5)*m[i+1][j+2] + (j+1.5)*m[i+2][j+1]) / M;
			mass[flag][i][j] = M;
			if (Equals(geom_x,cm_x[flag][i][j]) && Equals(geom_y,cm_y[flag][i][j]))
				res = true;
			
			int a = i, b = j;
			//cout << "K = " << K << " -- ";
			//cout << a << "," << b << ": " << geom_x << "," << geom_y << " " << cm_x[flag][a][b] << "," << cm_x[flag][a][b] << endl;
	
		}
	return res;
}

bool calcCM(int K, int a, int b) {
	double M = 0; //mass along the edges
	double tmp_x = 0, tmp_y = 0;
	//get three special points first, then the rest
	M += m[a][b+K-2];
	tmp_x += m[a][b+K-2] * (a + .5);
	tmp_y += m[a][b+K-2] * (b+K-2 + .5);
	M += m[a+K-2][b];
	tmp_x += m[a+K-2][b] * (a+K-2 + .5);
	tmp_y += m[a+K-2][b] * (b + .5);
	M += m[a+K-2][b+K-2];
	tmp_x += m[a+K-2][b+K-2] * (a+K-2 + .5);
	tmp_y += m[a+K-2][b+K-2] * (b+K-2 + .5);
	
	for (int i = 1; i < K-1; i++) {
		M += m[a+K-1][b+i];
		tmp_x += m[a+K-1][b+i] * (a+K-1 + .5);
		tmp_y += m[a+K-1][b+i] * (b+i + .5);
		M += m[a+i][b+K-1];
		tmp_x += m[a+i][b+K-1] * (a+i + .5);
		tmp_y += m[a+i][b+K-1] * (b+K-1 + .5);
	}
	
	
	double geom_x = a + .5 * K;
	double geom_y = b + .5 * K;
	double MTOT = M + mass[!flag][a][b];
	cm_x[flag][a][b] = (mass[!flag][a][b]*cm_x[!flag][a][b] + tmp_x) / MTOT;
	cm_y[flag][a][b] = (mass[!flag][a][b]*cm_y[!flag][a][b] + tmp_y) / MTOT;
	mass[flag][a][b] = MTOT;
	
	//cout << "K = " << K << " -- ";
	//cout << a << "," << b << ": " << geom_x << "," << geom_y << " " << cm_x[flag][a][b] << "," << cm_x[flag][a][b] << endl;
	
	if (Equals(geom_x,cm_x[flag][a][b]) && Equals(geom_y,cm_y[flag][a][b]))
		return true;
	return false;
}

int solveDP() {
	int BESTK = -1;
	bool three = setK3(); //initialize DP
	if (three) BESTK = 3;
	
	for (int K = 4; K <= min(R,C); K++) {
		flag = !flag;
		for (int i = 0; i+K <= R; i++)
			for (int j = 0; j+K <= C; j++) {
				//calcCM(K, i, j);
				//if (CMequalsCenter(K, i, j)) {
				if (calcCM(K, i, j)) {
					//we CAN find a good K
					BESTK = K;
				}
			}
	}
	
	return BESTK;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> R >> C >> D;
		for (int i = 0; i < R; i++) {
			string str;
			cin >> str;
			for (int j = 0; j < C; j++) {
				int a = str[j] - '0';
				m[i][j] = a + D;
			}
		}
		
		int res = solveDP(); //returns -1 if impossible
		if (res < 0)
			cout << "Case #" << icase << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
