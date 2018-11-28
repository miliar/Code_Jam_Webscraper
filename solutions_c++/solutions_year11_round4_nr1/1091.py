#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
using namespace std;

void solve(int pno)
{
	int X, S, R, N, T;
	
	cin >> X >> S >> R >> T >> N;
	
	vector<int> B(N, 0), E(N, 0), W(N, 0);
	for (int i = 0; i < N; ++i) cin >> B[i] >> E[i] >> W[i];
	
	double ans = 0;
	int pos = 0;
	
	vector<double> WT, RT;
	vector<int> WS, RS, D;
	
	for (int i = 0; i < N; ++i) {
		if (pos != B[i]) {
			WS.push_back(S);
			RS.push_back(R);
			D.push_back(B[i] - pos);
			WT.push_back( (double) (B[i] - pos) / (double) S);
			RT.push_back( (double) (B[i] - pos) / (double) R);
		}
		if (E[i] != B[i]) {
			WS.push_back(W[i] + S);
			RS.push_back(W[i] + R);
			D.push_back(E[i] - B[i]);
			WT.push_back( (double) (E[i] - B[i]) / (double) (W[i] + S) );
			RT.push_back( (double) (E[i] - B[i]) / (double) (W[i] + R) );
		}
		pos = E[i];
	}
	if (pos != X) {
		WS.push_back(S);
		RS.push_back(R);
		D.push_back(X - pos);
		WT.push_back( (double) (X - pos) / (double) S);
		RT.push_back( (double) (X - pos) / (double) R);
	}
	
	vector<pair<double, int> > dt;
	for (int i = 0; i < D.size(); ++i) {
		dt.push_back(make_pair( (RT[i] - WT[i]) / RT[i], i) );
		ans += WT[i];
	}
	sort(dt.begin(), dt.end() );
	double t = T;
	for (int i = 0; i < dt.size(); ++i) {
		if (t <= 0) break;
		int idx = dt[i].second;
		if (t >= RT[idx]) {
			ans -= WT[idx] - RT[idx];
			t -= RT[idx];
		} else {
			ans -= WT[idx];
			ans += t;
			ans += (D[idx] - RS[idx] * t) / WS[idx];
			break;
		}
	}
	
	printf("Case #%d: %.8f\n", pno, ans);
	cout.flush();
	
}

int main()
{
	int T;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}