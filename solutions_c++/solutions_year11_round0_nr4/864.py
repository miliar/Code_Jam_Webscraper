#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

double c[1005][1005];
double dp[1005][1005];
double bb[1005];
double pp[1005][1005];

int arr[1005];

//double bad(int a){
//	if (bb[a]){
//		return bb[a];
//	}
//	double ret = 1;
//	for (int i=1; i<a; i++){
//		double val = bad(a-i) * c[a][i];
//		ret -= val;
//	}
//	return bb[a] = ret;
//}
//double p(int a, int b){
//	if (pp[a][b] > -0.5){
//		return pp[a][b];
//	}
//	return c[a][b] * 
//}

//double DFS(int total, int bad){
//	if (dp[total][bad] > -0.5){
//		return dp[total][bad];
//	}
//	if (bad == 0){
//		return 0;
//	}
//	double ret = 0;
//	for (int i=0; i<bad; i++){
//		ret += (DFS(total, i) + 1) * p(i, bad);
//	}
//	ret /= 1 - p(bad, bad);
//	return dp[total][bad] = ret;
//}

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int t;
	c[0][0] = 1;
	for (int i=1; i<1005; i++){
		c[i][0] = 1;
		for (int j=1; j<1005; j++){
			c[i][j] = c[i-1][j-1] + c[i-1][j];
		}
	}
	memset(dp, -1, sizeof dp);
	memset(pp, -1, sizeof pp);
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int n, good = 0;
		cin >> n;
		for (int i=0; i<n; i++){
			cin >> arr[i];
			if (arr[i] == i+1){
				good++;
			}
		}
		cout << fixed << setprecision(6) << n-good << endl;
	}
	return 0;
}