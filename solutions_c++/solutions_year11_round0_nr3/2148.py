#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

main() {
int n, t, no = 1;
int result;
	vector<int> v(10);
	
scanf("%d", &t);
while(t--) {
	scanf("%d", &n);
	v.resize(n);
	result = 0;
	for(int i = 0; i < n; i++) {
		scanf("%d ", &v[i]);
		result = result xor v[i];
	}
	if(result != 0) {
		printf("Case #%d: NO\n", no++);
	} else {
		sort(v.begin(), v.end());
		int sum = 0;
		for(int i = 1; i < n;i++) {
			sum += v[i];
		}
		printf("Case #%d: %d\n", no++, sum);
	}	
}
}
