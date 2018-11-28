#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int N;
int d[10005], I[10005];
int D;

int DP[10005];

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> d[i] >> I[i];
		cin >> D;
		d[N] = D;
		
		DP[0] = d[0];
		//cout << 0 << " " << DP[0] << endl;
		for (int i = 1; i <= N; i++) { // calculate DP[i]
			int val = 0;
			for (int k = 0; k < i; k++) {
				if (DP[k] >= abs(d[i]-d[k]))
				{
					int tmp = min(DP[k], abs(d[i]-d[k]));
					val = max(val, tmp);
				}
			}
			if (i < N)
				DP[i] = min(val, I[i]);
			else
				DP[i] = val;
			//cout << i << " " << DP[i] << endl;
		}
		
		string res;
		if (DP[N] != 0) res = "YES";
		else res = "NO";
		
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
