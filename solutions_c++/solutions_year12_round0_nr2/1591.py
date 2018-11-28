/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<double> point;
typedef long double ldb;

int n,s,p,t;
int no[200],yes[200],a[200];
int dp[200][200];

int main(){
	
	cin >> t;

	for (int i=0; i<=10; i++)
		for (int j=i; j<=10; j++)
			for (int z=j; z<=10; z++) if (z-i<=2){
				if (z-i==2)
					yes[i+j+z] = max(yes[i+j+z],z);
				else
					no [i+j+z] = max(no [i+j+z],z);
			}

	for (int o=1; o<=t; o++){

		cin >> n >> s >> p;
		for (int i=1; i<=n; i++)
			cin >> a[i];
		
		for (int i=0; i<=n; i++)
			for (int j=0; j<=s; j++)
				dp[i][j] = -10000000;

		dp[0][0] = 0;

		for (int i=1; i<=n; i++){
			for (int j=0; j<=s; j++){
				dp[i][j] = max(dp[i][j] , dp[i-1][j] + (no[a[i]]>=p));
				if (j!=0 && yes[a[i]])
					dp[i][j] = max(dp[i][j], dp[i-1][j-1] + (yes[a[i]]>=p));
			
			}
		}

		cout << "Case #" << o << ": " << dp[n][s] << endl;
	}
	return 0;
}
