#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int n, a, b , rest_a, rest_b, now_time, x;
char ch;

void solve(int t){
	cin >> n;
	a = b = 1;
	rest_a = rest_b = 0;
	now_time = 0;
	for (int i = 0; i < n; i++){
		cin >> ch >>  x;
		if (ch == 'O'){
			rest_b += max(abs(x - a) - rest_a + 1, 1);
			now_time += max(abs(x - a) - rest_a + 1, 1);
			rest_a = 0;
			a = x;
		}
		if (ch == 'B'){
			rest_a += max(abs(x - b) - rest_b + 1, 1);
			now_time += max(abs(x - b) - rest_b + 1, 1);
			rest_b = 0;
			b = x;
		}
	}

	printf("Case #%d: %d\n", t, now_time);
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i + 1);

	return 0;
}
