#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int a[1000],b[1000];

int main() {
	int cases,kase=0,n;
	for (scanf("%d",&cases);cases>0;cases--) {
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		for (int i=1;i<=n;i++) scanf("%d",&b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		long long sum=0;
		for (int i=1;i<=n;i++) {
			long long tmp=a[i];
			tmp=tmp*b[n+1-i];
			sum=sum+tmp;
		}
		cout<<"Case #"<<++kase<<": "<<sum<<endl;
	}
}
