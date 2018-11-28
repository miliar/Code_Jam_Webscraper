#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int n,m,ans;
int st[111][33];
bool g[111][111],y[111];
int lk[111];

bool find(int x) {
	for(int i=0;i<n;i++) if (g[x][i] && !y[i]) {
		y[i]=true;
		if (lk[i]==-1 || find(lk[i])) {
			lk[i]=x;
			return true;
		}
	}
	return false;
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>n>>m;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>st[i][j];
		memset(g,0,sizeof g);
		for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
			bool ok=true;
			for(int k=0;k<m;k++) if (st[i][k]>=st[j][k]) ok=false;
			if (ok) g[i][j]=true;
		}
		ans=0;
		memset(lk,-1,sizeof lk);
		for(int i=0;i<n;i++) {
			memset(y,0,sizeof y);
			if (find(i)) ans++;
		}
		ans=n-ans;
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
