#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

int n;
int num1[810], num2[810];

void solve(int id) {
	sort(num1, num1+n);
	sort(num2, num2+n);
	ll res = 0;
	for (int i=0; i<n; ++i) {
		res += static_cast<ll>(num1[i]) * num2[n-1-i];
	}	
	printf("Case #%d: %lld\n", id, res);	
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int id=1; id<=T; ++id) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) 
			scanf("%d", num1+i);
		for (int i=0; i<n; ++i)
			scanf("%d", num2+i);
		solve(id);
	}
	return 0;
}