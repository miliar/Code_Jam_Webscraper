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

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("1s.out", "w", stdout);
	int t; cin>>t;
	int n, pd, pg, opd, n1, n2;
	bool all;
	for (int k=1; k<=t; k++) {
		cin>>n>>pd>>pg;
		opd = 100-pd;
		if (pd!=0) n1 = pd/(gcd(pd,100));
		else n1=0;
		if (opd!=0) n2 = opd/(gcd(opd,100));
		else n2=0;

		all=true;
		if (pd!=0 && pg==0) all=false;
		if (pd!=100 && pg==100) all=false;

		cout<<"Case #"<<k<<": ";
		if (all && (n1+n2)<=n) cout<<"Possible\n";
		else cout<<"Broken\n";
	}

	return 0;
}
