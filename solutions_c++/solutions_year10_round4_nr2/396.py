#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

int a[1111];
int c[1111], b[2111];
int s[1111][11];
int p,n;

void makeb(int x) {
	if (x>=n) {
		b[x]=a[x-n];
	}
	else {
		makeb(x*2);
		makeb(x*2+1);
		b[x]=min(b[x*2],b[x*2+1]);
		//cerr<<x<<"-"<<b[x]<<endl;
	}
}

int work(int x,int y) {
	if (x>=n) return 0;
	if (s[x][y]<0) {
		int ss=c[x];
		ss+=work(x*2,y)+work(x*2+1,y);
		s[x][y]=ss;
		if (b[x*2]>=y+1 && b[x*2+1]>=y+1) {
			int ss=work(x*2,y+1)+work(x*2+1,y+1);
			if (ss<s[x][y]) s[x][y]=ss;
		}
	}
	return s[x][y];
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		int p;
		cin>>p;
		n=(1<<p);
		for(int i=0;i<n;i++) cin>>a[i];
		for(int k=p-1;k>=0;k--) {
			int kk=(1<<k);
			for(int i=0;i<kk;i++) cin>>c[kk+i];
		}
		makeb(1);
		memset(s,-1,sizeof s);
		int ans=work(1,0);
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
