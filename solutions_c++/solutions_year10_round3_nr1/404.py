#include<iostream>
using namespace std;

int a[10010], b[10010];;
int n;

int main() {
	
	freopen("A-large.in.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int t;
	cin >> t;
	for(int idx = 1; idx <= t; idx ++) {
		cin >> n;
		for(int i = 0; i < n; i ++) {
			cin >> a[i] >> b[i];
		}
		int count = 0;
		for(int i = 0; i < n; i ++) {
			for(int j = i+1; j < n; j ++) {
				if((a[i]<a[j]) ^ (b[i]<b[j])) {
					count ++;
				}
			}
		}
		printf("Case #%d: %d\n", idx, count);
	}
	return 0;
}
