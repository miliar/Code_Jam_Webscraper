#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
int a[1010];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q,i,n,sx,sum,s1,s2,m1,m2,mx;
	cin >> t;
	for (q=1;q<=t;++q) {
		cin >> n;
		for (i=0;i<n;++i)
			cin >> a[i];
		sort(a,a+n);
		s1 = m1 = 0;
		for (i=1;i<n;++i) {
			s1 += a[i];
			m1 ^= a[i];
		}
		s2 = m2 = 0;
		for (i=0;i<n-1;++i) {
			s2 += a[i];
			m2 ^= a[i];
		}
		printf("Case #%d: ",q);
		mx=-1;
		if (m1==a[0])
			mx = max(mx, max(a[0],s1));
		if (m2==a[n-1])
			mx = max(mx, max(a[n-1],s2));
		if (mx==-1)
			printf("NO\n");
		else printf("%d\n",mx);
	}

	
	return 0;
}