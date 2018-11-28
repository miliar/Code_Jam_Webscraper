#include <stdint.h>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;


int n;
int64_t A, B, C, D, x0, y0, M, X[100009], Y[100009], cnt;


int main()
{
	int N;
	cin >> N;
	for (int testCase=1; testCase<=N; ++testCase) {
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		X[0] = x0; Y[0] = y0;
		for (int i=1; i<n; ++i) {
			X[i] = (A * X[i-1] + B) % M;
			Y[i] = (C * Y[i-1] + D) % M;
		}

		cnt = 0;
		for (int i=0; i<n-2; ++i) for (int j=i+1; j<n-1; ++j) for (int k=j+1; k<n; ++k) {
			if ((((X[i] + X[j] + X[k]) % 3) == 0) && (((Y[i] + Y[j] + Y[k]) % 3) == 0))
				++cnt;
		}

		cout << "Case #" << testCase << ": " << cnt << endl;
	}
	return 0;
}
