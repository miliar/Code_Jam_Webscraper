#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	size_t T;
	cin >> T;
	for (int t = 1 ;t <= T ;++t){
		int N ;
		int xdv[10000] = {0} ,xlv[10000] = {0};
		int D;
		cin >> N;
		int dp[10000] = {0};
		int d ,l;
		cin >> d >> l;
		dp[0] = d + d;
		xdv[0] = d;
		int mmax = dp[0];	
		for (size_t i = 1 ;i < N ;++i){
			cin >> d >> l;
			xdv[i] = d;
			dp[i] = 0;
			for (int k = 0 ;k < i ;++k){
				if (dp[k] >= d){
					dp[i] = max(dp[i] ,d + min(xdv[i] - xdv[k] ,l));
				}
			}
			mmax = max(mmax ,dp[i]);
		}
		cin >> D;
		cout << "Case #" << t << ": " ;
		if (D <= mmax)
			cout << "YES" ;
		else
			cout << "NO" ;
		cout << endl;
	}
}
