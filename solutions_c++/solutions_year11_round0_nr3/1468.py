#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int a[2000];

int main() {
	int t, n;
	scanf("%d", &t);
	for(int cas=1; cas<=t; ++cas) {
		scanf("%d", &n);
		int sum = 0, bsum = 0, min=10000000;
		for(int i=0; i<n; ++i) {
			scanf("%d", a+i);
			bsum ^= a[i];
			sum += a[i];
			if(min>a[i]) min = a[i];
		}
		if(bsum!=0)
			printf("Case #%d: NO\n", cas);
		else
			printf("Case #%d: %d\n", cas, sum-min);
	}
}
