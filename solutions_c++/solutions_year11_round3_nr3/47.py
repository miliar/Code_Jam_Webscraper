#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
const int maxn = 10010;
long long a[maxn];
void solve() {
	int n,x,y;
	cin >> n >> x >> y;
	int i,j;
	for ( i=1;i<=n;++i)
		cin >> a[i];
	
	for ( i=x;i<=y;++i) {
		for (j=1;j<=n;++j) {
			if (a[j] % i !=0 && i%a[j]!=0) {
				break;
			}
		}
		if (j > n) {
			cout << i << "\n";
			return;
		}
	}
	cout << "NO\n";
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, tst;
	cin >> t;
	for (tst = 1; tst <= t; ++tst) {
		cout << "Case #" << tst << ": ";
		solve();
		
	}
	
	return 0;
}