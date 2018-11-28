#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

ll dp[501][501];
ll C[501][501];

int main()
{
	memset(C,0,sizeof(C));
	C[0][0]=1;
	memset(dp,0,sizeof(dp));
	for (int i=1;i<=500;i++){
		C[i][0]=1;
		for (int j=1;j<=i;j++)C[i][j]=(C[i-1][j]+C[i-1][j-1])%(ll)100003;
	}
	for (int i=2;i<=500;i++)dp[i][1]=1;
	for (int i=3;i<=500;i++){
		for (int j=2;j<i;j++){
			// last -- i, amount -- j
			for (int k=max(1,2*j-i);k<j;k++)dp[i][j]=(dp[i][j]+dp[j][k]*C[i-j-1][j-k-1])%(ll)100003;
		}
	}
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		int n;
		cin >> n;
		ll ans=0;
		for (int i=0;i<n;i++)ans=(ans+dp[n][i])%(ll)100003;
		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}
