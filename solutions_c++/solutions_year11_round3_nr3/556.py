#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

typedef long long lint;

int gcd(int m,int n) {
	if (m < n) {
		int tmp = m;
		m = n;
		n = tmp;
	}

	if (n == 0)
		return m;

	while (n > 0) {
		int tmp = m % n;
		m = n;
		n = tmp;
	}

	return m;
}

int n;
lint l, h, gy, gb;
lint notes[10000];

bool test(int num) {
	for (int i=0; i<n; i++)
		if (notes[i]%num!=0 && num%notes[i]!=0) return false;
	return true;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("6s.out", "w", stdout);
	int t; cin>>t;
	for (int k=1; k<=t; k++) {
		cin>>n>>l>>h;
		for (int i=0; i<n; i++) cin>>notes[i];
		cout<<"Case #"<<k<<": ";
		int i;
		for (i=l; i<=h; i++) {
			if (test(i)) {
				cout<<i<<endl;
				break;
			}
		}
		if (i==h+1) cout<<"NO\n";
	}

	return 0;
}
