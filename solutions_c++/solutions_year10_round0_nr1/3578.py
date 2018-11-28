#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out","w", stdout);
	
	int test; cin >> test;
	int no = 0;
	while(test --) {
		int n, k;
		cin >> n >> k;
		int msk = (1 << n) - 1;
		cout << "Case #" << ++ no <<": ";
		if((k & msk) == msk) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
