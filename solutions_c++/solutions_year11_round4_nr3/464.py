#include <iostream>
#include <cmath>

using namespace std;

int x[10000],y[10000],z[10000],ans[10000];

int gcd(int a,int b) {
	if (a==0) return b;
	if (a>b) return gcd(b,a);
	return gcd(b % a,a);
}

int main()
{
	int n=1000;
	for (int i=2;i<=n;i++) {
		int d=1;
		for (int j=sqrt(i);j>=2;j--) if (i%j==0) {
			d=0;
			break;
		}
		x[i]=x[i-1]+d;
		y[i]=d;
		//if (d) cout << i << ' ';
	}
	for (int i=2;i<=n;i++) {
		z[i]=0;
		for (int j=0;j<=n;j++) if (y[j]==1) {
			int a=j;
			while (a<=i) {
				z[i]++;
				a=a*j;
			}
		}
		ans[i]=z[i]-x[i]+1;
	}
	int t;
	cin >> t;
	int ca=0;
	while (++ca<=t) {
		cin >> n;
		printf("Case #%d: %d\n",ca,ans[n]);
	}
}