#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int find_gcd(int m, int n) {
if(m%n==0)
return n;
return find_gcd(n, m%n);
}

main() {
int t, n, cas = 1, l, h, gcd, lcm, prod, flag;
int a[100];

scanf("%d", &t);
while(t--) {
	scanf("%d %d %d", &n, &l, &h);
	for(int i =0;i<n;i++) {
	scanf("%d", &a[i]);
	}
	int ans =-1;
	for(int i =l;i<=h;i++) {
		flag = false;
		for(int j = 0; j<n;j++) {
			if(i%a[j]!=0 && a[j]%i!=0) {
				flag = true;
				break;
			}
		}
		if(flag == false) {
			ans = i;
			break;
		}
	}
	if(ans == -1)			
	printf("Case #%d: NO\n", cas++);	
	else	
	printf("Case #%d: %d\n", cas++, ans);	
}
}
