#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

long long t;
int N,C,L,T;
int a[1000100];

int main() {
	cin>>T;
	for (int I=1;I<=T;I++) {
		cin>>L>>t>>N>>C;
		for (int i=1;i<=C;i++) cin>>a[i];
		int now=1;
		for (int i=C+1;i<=N;i++) {
			a[i]=a[now];
			now++;
			if (now>C) now=1;
		}
		now=1;
		long long tt=0;
		long long ans=0;
		while (now<=N) {
			if (tt+a[now]*2<=t) {
				tt=tt+a[now]*2;
				ans=ans+a[now]*2;
				now++;
			} else {
				int k=(t-tt)/2;
				a[now]=a[now]-k;
				ans=t;
				break;
			}
		}
//		printf("now %d %d\n",now,N);
		if (now<=N) {
			sort(a+now,a+N+1);
			for (int i=N;i>=now;i--) {
				if (L>0) {
					L--;
					ans=ans+a[i];
				} else {
					ans=ans+a[i]*2;
				}
			}
		}
		cout<<"Case #"<<I<<": "<<ans<<endl;
	}
}
