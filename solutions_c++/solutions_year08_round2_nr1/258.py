#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

long long n, A, B, C, D, x0, y0, M;
vector<long long> xs, ys;


void getPoints()
{
	xs.clear();
	ys.clear();
	long long X = x0;
	long long Y = y0;
	xs.push_back(X);
	ys.push_back(Y);
	for (int i=1; i<n; ++i) {
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		xs.push_back(X);
		ys.push_back(Y);
	}
/*
	for (int i=0; i<xs.size(); ++i) {
		cout << xs[i] << ' ' << ys[i] << endl;
	}
*/
}

long long calc()
{
	int i, j, k;
	long long ans = 0;
	for (i=0; i<n; ++i) for (j=i+1; j<n; ++j) for (k=j+1; k<n; ++k) {
		if ((xs[i]+xs[j]+xs[k])%3 == 0 && (ys[i]+ys[j]+ys[k])%3 == 0) ans ++;

	}

	return ans;
}

int main(void)
{
	int N;
	cin >> N;
	for (int i=1; i<=N; ++i) {
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		getPoints();

		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}
