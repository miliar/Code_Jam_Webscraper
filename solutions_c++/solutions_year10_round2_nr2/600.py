#include <iostream>
#include <iomanip>
#include <cmath>

#define REP(x,a,n) for(int x=(a); x<(n); x++)
#define rep(x,n) REP(x,0,n)

using namespace std;

void main2() {
	int N, K, B, T;
	cin >> N >> K >> B >> T;

	int X[50], V[50];
	char chicks[50];


	rep(i,N) cin >> X[i];
	rep(i,N) cin >> V[i];

	int total = 0;
	rep(i,N) {
		if(B <= X[i] + T * V[i]) {
			chicks[i] = 1;
			total++;
		} else {
			chicks[i] = 0;
		}
	}
	if(total < K) {
		cout << "IMPOSSIBLE";
		return;
	}

	int i = N-1, nch = 0, swaps = 0;
	while(nch < K && i >= 0) {
		if(chicks[i]) {
			nch++;
			int j = i+1;
			while(j < N && chicks[j]==0) {
				chicks[j-1] = 0;
				swaps++;
				j++;
			}
			if(j <= N) chicks[j-1] = 1;
			//rep(_i,N) cout << ((int)chicks[_i]);
			//cout << endl;
		}
		i--;
	}
	cout << swaps;
}

int main() {
	int T, caseno = 1;
	cin >> T;

	while(caseno <= T) {
		cout << "Case #" << caseno++ << ": ";
		main2();
		cout << endl;
	}
	return 0;
}
