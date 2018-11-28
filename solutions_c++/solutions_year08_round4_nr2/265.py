#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define forn(i,n) for (int i=0;i<n;++i)
#define all(a) a.begin(),a.end()
#define and 1


void solve(){
	long long n,m,a;
	cin >> n >> m >> a;
	for (long long x1=0;x1<=n;++x1)
		for (long long y1=0;y1<=m;++y1)
			for (long long x2=0;x2<=n;++x2)
				for (long long y2=0;y2<=m;++y2){
					long long s=x1*y2-x2*y1;
					if (s<0)s=-s;
					if (s==a){
						cout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
						return;
					}
				}
	cout << "IMPOSSIBLE";
	cout << endl;
	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	forn(i,n){
		cout << "Case #" << i+1 << ": ";
		solve();
	}

	return 0;
}