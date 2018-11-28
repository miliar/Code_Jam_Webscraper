#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

int C, N;

long long sel[50][50];

double calc()
{
	double ans = 0;
	for (int i=0; i<C; ++i) {
		ans += 1.0/sel[C][i];
	}

	return ans*C/N;
}

double cache[100];
bool ok[100];
double calc(int al)
{
	if (al>= C) return 0;

	if (ok[al]) return cache[al];

	int need = C-al;
	if (need > N) need = N; 

	int j;
	double ans = 0;
	double p = 0;
	for (j=1; j<=need; ++j) {
		//cout << C-al << ' ' << j << endl;
		//cout << C << ' ' << j << endl;
		//cout << al << ' '  << N-j << endl;

		double p1 = 1.0 * sel[C-al][j] / sel[C][N] * sel[al][N-j];
		ans += calc(al+j) * p1;
		p += p1;
	}
	ans++;
	ans /= p;
	//ans++;
	ok[al] = true;
	return cache[al] = ans;
}

int main(void)
{
	memset(sel, 0, sizeof(sel));
	int i, j;

	sel[1][0] = 1;
	sel[1][1] = 1;

	for (i=2; i<=40; ++i) {
		sel[i][0] = 1;
		//cout << i << ' ' << 0 << " : " << sel[i][0] << endl;
		for (j=1; j<=i; ++j) {
			sel[i][j] = sel[i-1][j-1] + sel[i-1][j];
			//cout << i << ' ' << j << " : " << sel[i][j] << endl;
		}
	}


	int T;
	cin >> T;
	for (int ca=1; ca<=T; ++ca) {
		cin >> C >> N;
		memset(ok, 0, sizeof(ok));
		cout << "Case #" << ca << ": " << calc(N)+1 << endl;
	}
	return 0;
}
