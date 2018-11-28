#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int gcd(int a,int b) {
	if (b==0)
		return a;
	return gcd(b,a%b);
}

int main() {
	int T,n,a[3],ans,delta,kase=0;
	cin>>T;
	while (T--) {
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>a[i];
		if (n==2) {
			delta=abs(a[0]-a[1]);
		}
		else {
			int d1=abs(a[0]-a[1]);
			int d2=abs(a[0]-a[2]);
			int d3=abs(a[1]-a[2]);
			delta=gcd(d1,d2);
			delta=gcd(delta,d3);
		}
		ans=a[0]%delta;
		if (ans>0)
			ans=delta-ans;
		cout<<"Case #"<<++kase<<": "<<ans<<endl;
	}
	return 0;
}
