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
#include <cmath>
#include <cstdlib>
#include <ctime> 
using namespace std;

int geta(int n) {
	int x=n/3;
	if(n%3) x++;
	return x;
}

int getb(int n) {
	n-=2;
	int x=n/3;
	return x+2;
}

int main() {
	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		int n, s, p; cin>>n>>s>>p;
		vector<int> v(n);
		for (int i=0; i<n; i++) cin>>v[i];

		sort(v.begin(), v.end(), greater<int>());

		int ans=0;
		for (int i=0; i<n; i++) {
			int val=v[i], cur=geta(val);
			if(cur>=p) ans++;
			else {
				if(s && val>=2) {
					cur=getb(val);
					if(cur>=p) ans++;
					s--;
				}
			}
		}
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}
