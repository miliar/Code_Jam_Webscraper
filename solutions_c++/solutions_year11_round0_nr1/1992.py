#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int n;
int a[105],b[105],p1,p2;

void solve() {
	p1=1;p2=1;
	int t,t1=0,t2=0,last=0;
	for (int i=0;i<n;i++) {
		if (a[i]==0) {
			t=abs(b[i]-p1)+1;
			if (last+1<t1+t)
				t1+=t;
			else
				t1=last+1;
			last=t1;
			p1=b[i];
//cout<<t<<" "<<p1<<" "<<last<<endl;
		}
		else {
			t=abs(b[i]-p2)+1;
			if (last+1<t2+t)
				t2+=t;
			else
				t2=last+1;
			last=t2;
			p2=b[i];
//cout<<t<<" "<<p2<<" "<<last<<endl;
		}
	}
	cout<<last<<endl;
}

int main() {
	char s[10];
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>n;
		for (int i=0;i<n;i++) {
			scanf("%s %d",s,&b[i]);
			if (s[0]=='O') a[i]=0;
			else a[i]=1;
		}
		printf("Case #%d: ",++kase);
		solve();
	}
	return 0;
}
