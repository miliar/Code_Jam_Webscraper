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
const int maxn = 110;
char a[maxn][maxn]={{0}};
void solve() {
	int i,j,n,m;
	cin >> n >> m;
	for (i=1;i<=n;++i)
		for (j=1;j<=m;++j)
			cin >> a[i][j];
	for (i=1;i<n;++i) {
		for (j=1;j<m;++j) {
			if (a[i][j]=='#' && a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#') {
				a[i][j]='/';
				a[i][j+1]='\\';
				a[i+1][j]='\\';
				a[i+1][j+1]='/';
			}
		}
	}
	for (i=1;i<=n;++i)
		for (j=1;j<=m;++j)
			if (a[i][j]=='#') {
				cout << "Impossible\n";
				return;
			}
			for (i=1;i<=n;++i) {
				for (j=1;j<=m;++j) {
					cout << a[i][j];
				}
				cout << "\n";
			}

}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, tst;
	cin >> t;
	for (tst = 1; tst <= t; ++tst) {
		cout << "Case #" << tst << ":\n";
		solve();
		
	}
	
	return 0;
}