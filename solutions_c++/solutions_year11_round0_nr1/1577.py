#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
using namespace std;

int T, n;
string ss[200];
int arr[200];

int main() {
	freopen("bt.in", "r", stdin);
	freopen("bt.out", "w", stdout);
	scanf("%d", &T);
	for(int s = 1; s <= T; ++s) {
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			cin >> ss[i] >> arr[i];
		}
		int t1 = 0, t2 = 0, t11 = 1, t22 = 1;
		int first = 0;
		for(int i = 0; i < n; ++i) {
			if(ss[i] == "O") {
				int move = abs(arr[i] - t11);
				t1 += move;
				t11 = arr[i];
				if(t1 < t2) t1 = t2;
				t1 += 1;
			} else {
				int move = abs(arr[i] - t22);
				t2 += move;
				t22 = arr[i];
				if(t2 < t1) t2 = t1;
				t2 += 1;
			}
		}
		printf("Case #%d: %d\n", s, max(t1, t2));
	}
	return 0;
}