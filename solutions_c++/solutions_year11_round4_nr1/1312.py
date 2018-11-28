#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <iomanip>

using namespace std;

int T;
int X, S, R, N;
long double t;

struct WalkWay {
	int B, E, w;
};

WalkWay walkways [1000];

bool cmp (WalkWay A, WalkWay B) {
	return A.w < B.w;
}

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	
	for (int z = 1; z <= T; z ++) {
		fin >> X >> S >> R >> t >> N;
		int empty = X;
		long double ans = 0;
		for (int i = 0; i < N; i ++) {
			fin >> walkways [i].B >> walkways [i].E >> walkways [i].w;
			empty -= walkways [i].E - walkways [i].B;
			ans += ((long double) walkways [i].E - walkways [i].B) / (walkways [i].w + S);
		}
		ans += ((long double) empty) / S;
		sort (walkways, walkways + N, cmp);
		if (t <= ((long double) empty) / R) {
			ans -= ((long double) empty) / S;
			ans += t + ((long double) (empty - R * t)) / S;
			t = 0;
		}
		else {
			ans -= ((long double) empty) / S;
			ans += ((long double) empty) / R;
			t -= ((long double) empty) / R;
		}
		for (int i = 0; i < N; i ++) {
			if (t <= ((long double) (walkways [i].E - walkways [i].B)) / (R + walkways [i].w)) {
				ans -= ((long double) (walkways [i].E - walkways [i].B)) / (S + walkways [i].w);
				ans += t + ((long double) (walkways [i].E - walkways [i].B) - (R + walkways [i].w) * t) / (S + walkways [i].w);
				t = 0;
			}
			else {
				ans -= ((long double) (walkways [i].E - walkways [i].B)) / (S + walkways [i].w);
				ans += ((long double) (walkways [i].E - walkways [i].B)) / (R + walkways [i].w);
				t -= ((long double) (walkways [i].E - walkways [i].B)) / (R + walkways [i].w);
			}
		}
		cout << setprecision (8);
		fout << setprecision (8);
		cout << "Case #" << z << ": " << ans << endl;
		fout << "Case #" << z << ": " << ans << endl;
	}
}