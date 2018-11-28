#include <iostream>
#include <stdio.h>
using namespace std;
int main () {
	freopen ("C-large.in","r",stdin);
	freopen ("C-large.out","w",stdout);
	int test,ca;
	cin>>test;
	for (ca= 1;ca<=test;ca++) {
		int n;
		cin>>n;
		int min = 10000000;
		int sum=0;
		int ans;
		for (int i=0;i<n;i++) {
			int a;
			cin>>a;
			if (i == 0) {
				ans = a;
			} else {
				ans ^= a;
			}
			sum+=a;
			if (min > a) {
				min = a;
			}
		}
		
		if (ans != 0) {
			printf ("Case #%d: NO\n",ca);
		} else {
			printf ("Case #%d: %d\n",ca,sum-min);
		}
	}
	return 0;
}
