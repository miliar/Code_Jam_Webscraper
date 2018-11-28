#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int n,l,h,ans,a[105];

bool solve() {
	for (ans=l;ans<=h;ans++) {
		bool flag=true;
		for (int i=0;i<n;i++)
			if (ans%a[i]!=0&&a[i]%ans!=0) {flag=false;break;}
		if (flag) return true;
	}
	return false;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>n>>l>>h;
		for (int i=0;i<n;i++)
			scanf("%d",&a[i]);
		printf("Case #%d: ",++kase);
		if (solve()) {
			cout<<ans<<endl;
		}
		else cout<<"NO"<<endl;
//		printf("\n");
	}
	return 0;
}
