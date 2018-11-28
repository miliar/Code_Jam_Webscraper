#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <iomanip>

using namespace std;

const int MAXN = 100;
double P[MAXN][MAXN];
double E[MAXN];

void BuildP() {
	P[0][0] = 1;

	for (int i=1;i < MAXN;++i)
	{
		P[i][0] = P[i-1][0]/ (i);
		P[i][1] = 0;
	}

	for (int N =0; N < MAXN;++N)
		for (int k=1;k <N;++k) {
			P[N][k+1] = (N-k)*(k*P[N][k] + (N-k+1)*P[N][k-1])/(k+1);
		}
}

void BuildE() {
	E[0] = 0;

	for (int K=1;K < MAXN;++K) {
		double S = 1;
		for (int J=0;J < K;++J) {
			S+= E[J]*P[K][J];
		}
		E[K] = S/(1-P[K][K]);
	}
}

double solve(const vector<int> & vals) {
	vector<int> q = vals;
	sort(q.begin(),q.end());

	int N = 0;
	for (int i=0;i < vals.size();++i)
		if (vals[i] != q[i]) ++N;

	return E[N];
}

int main(int argc, char **argv) {
	BuildP();
	BuildE();

	int T;

	cout << fixed << setprecision(6);
	cin >> T;

	for(int i=0;i < T;++i) {
		int N;
		cin >> N;

		vector<int> vals;

		for (int j=0;j < N;++j) {
			int C;
			cin >> C;
			vals.push_back(C);
		}

		cout << "Case #" << (i+1) << ": " << solve(vals) << endl;
	}
	
    return 0;
}
