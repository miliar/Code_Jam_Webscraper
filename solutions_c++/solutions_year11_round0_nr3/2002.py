#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int n,a[1005];

void solve() {
	int t=0;
	for (int i=0;i<n;i++) t^=a[i];
	if (t!=0) {
		cout<<"NO"<<endl;
	}
	else {
		int sum=0;
		sort(a,a+n);
		for (int i=1;i<n;i++) sum+=a[i];
		cout<<sum<<endl;
	}
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>n;
		for (int i=0;i<n;i++) cin>>a[i];
		printf("Case #%d: ",++kase);
		solve();
	}
	return 0;
}
