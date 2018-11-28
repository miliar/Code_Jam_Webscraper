#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <math.h>
#include <algorithm>
#include <memory.h>
using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt;
	cin >> tt;
	for (int t=1;t<=tt;t++) {
		int r,c;
		cin >> r >> c;
		vector <string> v;
		v.resize(r);
		for (int i=0;i<r;i++) cin >> v[i];
		bool ans = true;
		for (int i=0;i<r-1;i++) {
			for (int j=0;j<c-1;j++) {
				if (v[i][j]=='#') {
					if (v[i][j+1]=='#' && v[i+1][j]=='#' && v[i+1][j+1]=='#') {
						v[i][j]=v[i+1][j+1]='/';
						v[i][j+1]=v[i+1][j] = '\\';
					} else {
						ans = false;
						break;
					}
				}
			}
			if (!ans) break;
		}
		for (int i=0;i<r;i++) {
			for (int j=0;j<c;j++) {
				if (v[i][j]=='#') {
					ans = false;
					break;
				}
			}
			if (!ans) break;
		}
		cout << "Case #"<< t <<":" << endl;
		if (ans) {
			for (int i=0;i<r;i++) cout << v[i] << endl;
		} else cout << "Impossible" << endl;
	}
}