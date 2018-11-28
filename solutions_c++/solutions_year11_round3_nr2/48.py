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
const int maxn = 1000010;
long long x[maxn] = {0};
int d[maxn] = {0};
long long e[maxn]={0};
void solve() {
	int i,j,n,L,c,pos;
	long long T;
	cin >> L >> T >> n >> c;
	L=L;
	for (i=1;i<=c;++i) {
		cin >> d[i];
	}
	for (i=1;i<=n;++i) {
		pos = i % c;
		if (!pos)
			pos = c;
		x[i] = x[i-1] + d[pos];
	}
	long long res = 0;
	int all = 0;
	for (i=0;i<n;++i) {
		if (T >= x[i] * 2ll && T <= x[i+1] * 2ll) {
			res += T - x[i] * 2ll;
			e[++all] = x[i + 1] * 2ll - T;
			for (j = i + 1; j < n; ++j) {
				e[++all] = (x[j+1]-x[j]) * 2ll;
			}
			break;
		}
		else {
			res += (x[i+1]-x[i]) * 2ll;
		}
	}	
	sort(e+1,e+1+all);
	reverse(e+1,e+1+all);
	for (i=1;i<=min(L,all);++i)
		res += e[i] / 2;

	for (;i<=all;++i)
		res += e[i];
	cout << res << "\n";
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