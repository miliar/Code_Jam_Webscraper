#include <iostream>

using namespace std;

int caseN, N;
int n, A, B, C, D, x_0, y_0, M;
long long x[100000], y[100000];
int i, j, k;
int ans;
int tmpx, tmpy, l;
int found;

int main() {
	cin >> caseN;
	for (N = 1; N <= caseN; N++) {
		cin >> n >> A >> B >> C >> D >> x_0 >> y_0 >> M;

		x[0] = x_0;
		y[0] = y_0;
		for (i = 1; i <= n-1; i++) {
			x[i] = (((A%M) * (x[i-1]%M) %M) + B) % M;
			y[i] = (((C%M) * (y[i-1]%M) %M) + D) % M;
		}


		ans = 0;
		for (i = 0; i < n-2; i++)
			for (j = i+1; j < n-1; j++)
				for (k = j+1; k < n; k++)
						if (((x[i]%3)+(x[j]%3)+(x[k]%3)) % 3 == 0)
							if (((y[i]%3)+(y[j]%3)+(y[k]%3)) % 3 == 0) {
								ans++;
						}

		cout << "Case #" << N << ": " << ans << endl;
	}
	return 0;
}
