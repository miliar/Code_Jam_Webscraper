#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int d[10001];
int l[10001];
int dp[10001];

int main(){
	int t, i, j, k, n, fd, r;
	cin >> t;
	for (i=0; i<t; ++i) {
		cin >> n;
		
		for (j=0; j<n; ++j) {
			cin >> d[j] >> l[j];
			dp[j] = d[j];
		}
		dp[0] = 0;
		
		cin >> fd;
		d[n] = fd;
		dp[n] = 1<<30;
		l[n] = 1<<30;
		
		for (j=0; j<n-1; ++j) {
			r = 2*d[j]-dp[j];
			for (k=j+1; d[k]<=r && k<n+1; ++k) {
				if (d[j]<dp[k]) {
					if (d[j]>(d[k]-l[k])) {
						dp[k] = d[j];
					} else {
						dp[k] = d[k]-l[k];
					}
				}
			}
		}

		
		if ((2*d[n-1]>=dp[n-1]+fd) || dp[n]!=(1<<30)) {
			cout << "Case #" << (i+1) <<": YES"<<endl;
		} else {
			cout << "Case #" << (i+1) <<": NO"<<endl;
		}
	}
	
	return 0;
}