#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

#define REP(i,a,b) for(int i=a;i<=b;i++)

long long L, T, N, C;
long long a[10100];
long long DP[10100][50];

int parsecs(int i)
{
	return a[i%C];
}

int main()
{
	int NO;
	cin >> NO;
	for(int no=1;no<=NO;no++) {
		cin >> L >> T >> N >> C;
		for(int i=0;i<C;i++) {
			cin >> a[i];
		}
		
		for(int i=0;i<50;i++) {
			DP[0][i] = 0;
		}
		
		for(int i=1;i<=N;i++) {
			for(int j=0;j<L;j++) {
				long long buildTime = max(T-DP[i-1][j+1], 0LL);
				DP[i][j] = DP[i-1][j] + parsecs(i-1)*2; // not boosted
				
				// boosted
				if(parsecs(i-1)*2>buildTime) {
					DP[i][j] = min(DP[i][j] ,
						DP[i-1][j+1] + parsecs(i-1)+buildTime/2
					);
				}
				//cout << buildTime << ","<<  DP[i][j] << "\t";
			}
			DP[i][L] = DP[i-1][L] + parsecs(i-1)*2;
			//cout << DP[i][L] << endl;
		}
		
		long long ans = DP[N][0];
		for(int i=0;i<L;i++) {
			ans = min(ans, DP[N][i]);
		}
		
		cout << "Case #" << no << ": " << ans << endl;
	}
	return 0;
}
