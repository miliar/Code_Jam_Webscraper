#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[1100];

void solve(int test){
	int n;
	cin >> n;
	int ans = 0, solution = 0;
	for (int i = 0; i < n; i++){
		cin >> a[i];
		ans ^= a[i];
		solution += a[i];
	}
	if (ans != 0){
		printf("Case #%d: NO\n", test);
		return;
	}
	
	sort(a, a + n);
	solution -= a[0];
	printf("Case #%d: %d\n", test, solution);
}

int main(){
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1 ; i <= t; i++)
		solve(i);
	return 0;
}
