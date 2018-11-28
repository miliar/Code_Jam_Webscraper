#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

#define M 100003
#define N 501

int pick[N][N];

int pure[N][N]; // [last][size]

int main() {
    pick[0][0] = 1;
    for(int n = 1; n < N; n++) {
	pick[n][0] = 1;
	for(int k = 1; k <= n; k++) {
	    pick[n][k] = (pick[n-1][k-1] + pick[n-1][k]) % M;
	}
    }
    for(int n = 2; n < N; n++) {
	pure[n][1] = 1; // {n}
	for(int s = 2; s < n; s++) {
	    // rank of n is s.
	    int c = 0;
	    for (int rs = 1; rs < s; rs++) {
		// rank of s is rs
		//  <  rs  >< s - rs >
		// {.......s.........n}
		// need to pick s - 1 - rs numbers in [s+1 .. n-1]
		c += pick[n-1-s][s-1-rs] * pure[s][rs] % M;
	    }
	    pure[n][s] = c % M;
	}
    }
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
	cout << "Case #"<<(t+1)<<": ";
	DBG(1,"CASE " << (t+1));
	int n; cin >> n;
	cin.getline(buf,sizeof buf);
	int r = 0;
	for(int s = 1; s < n; s++) r += pure[n][s];
	cout << r % M;
	cout << endl;
    }
    return 0;
}
