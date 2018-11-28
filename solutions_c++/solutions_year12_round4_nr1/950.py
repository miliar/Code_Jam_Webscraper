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

const int maxN = 10000 + 10;

int n,D,testCase;
int dp[maxN],d[maxN],l[maxN];

int main(){
	
	cin >> testCase;

	for (int o=1; o<=testCase; o++){
	
		cin >> n;
		for (int i=1; i<=n; i++)
			cin >> d[i] >> l[i];
		
		cin >> D;
	
		dp[1] = d[1];
		for (int i=2; i<=n; i++){
			dp[i] = 0;
			for (int j=1; j<i; j++) if (d[j] + dp[j] >= d[i]){
				dp[i] = max(dp[i],min(l[i],d[i]-d[j]));
			}
		}

		cout << "Case #" << o << ": ";

		bool f = false;
		for (int i=1; i<=n; i++) if (d[i] + dp[i] >= D){
			cout << "YES" << endl;
			f = true;
			break;
		}

		if (!f)
			cout << "NO" << endl;
	}

	return 0;
}
