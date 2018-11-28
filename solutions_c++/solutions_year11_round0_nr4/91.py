#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int calc(int n) {
	if (n <= 1) return 0;
	return n;
}

int go(int i, vector <int> &v, vector <bool> &visited) {
	if (visited[i]) {
		return 0;
	}
	visited[i] = true;
	return 1 + go(v[i],v,visited);
}

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		int n;
		
		cin >> n;
		
		vector <int> v(n);
		vector <bool> visited(n,false);
		
		for (int i=0; i < n; i++) {
			cin >> v[i];
			v[i]--;
		}
		
		int ans = 0;
		
		for (int i=0; i < n; i++) {
			ans += calc(go(i,v,visited));
		}
		
		printf("Case #%d: %d\n",t++,ans);
	}
	
	return 0;
}
