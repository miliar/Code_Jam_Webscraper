#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#include <stdlib.h>

int solve(vector<char> &R, vector<int> &P)
{
	int ans = 0;
	int ro = 1, rb = 1;
	int lo = 0, lb = 0;
	for (int i = 0; i < R.size(); ++i) {
		if (R[i] == 'O') {
			int d = labs(P[i] - ro) - (ans - lo);
			if (d < 0) d = 0;
			ans += d + 1;
			lo = ans;
			ro = P[i];
		} else {
			int d =labs(P[i] - rb) - (ans - lb);
			if (d < 0) d = 0;
			ans += d + 1;
			lb = ans;
			rb = P[i];
		}
		//printf("%d, %d, %d\n", ans, ro, rb);
	}
	return ans;
}
int main()
{
	int T, N;
	vector<char> R;
	vector<int> P;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		cin >> N;
		R.clear();
		P.clear();
		for (int j = 0; j < N; ++j) {
			string x, y;
			int p;
			
			cin >> x >> y;
			istringstream iss(y);
			iss >> p;
			R.push_back(x[0]);
			P.push_back(p);
		}
		cout << "Case #" << i + 1 << ": " << solve(R, P) << endl;
	}
	return 0;
}