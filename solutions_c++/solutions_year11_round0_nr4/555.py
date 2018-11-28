#include <iostream>
#include <stdio.h>
using namespace std;
int n,a[1005],i,j,sum,temp;
int main() {
	freopen ("D-large.in","r",stdin);
	freopen ("D-large.out","w",stdout);
	int t;
	cin>>t;
	for (int ca = 1;ca<=t;ca++) {
		sum=0;
		cin>>n;
		
		for(i=1;i<=n;i++) {
			cin>>a[i];
			if (a[i] != i) {
				sum++;
			}
		}
		
		printf("Case #%d: %.6lf\n",ca,sum*1.0);
	}
	return 0;
}
