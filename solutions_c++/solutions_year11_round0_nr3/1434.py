#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;
#define FOR(i,a,n) for(int i = a; i < n; i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back


int main() {
	int n;
	cin >> n;
	REP(i,n) {

		int m, mn = 10000000;
		long long sm = 0LL, x = 0LL;
		cin >> m;
		REP(j,m) {
			int a;
			cin >> a;
			sm += a;
			x ^= a;
			if(mn > a) mn = a;
		}
		cout << "Case #" << i+1 <<": ";
		if(x == 0LL) {
			cout << sm-mn << endl;
		}
		else cout << "NO\n";

		
	}
}			

		
		

