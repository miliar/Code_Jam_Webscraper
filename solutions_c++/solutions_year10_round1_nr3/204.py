#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

int d[2000][2000];

bool arya(int x,int y) {
	if (x>=2*y || y>=2*x) return true;
	if (x==y) return false;
	if (y>x) {
		int t=x; x=y; y=t;
	}
	if (x<2000 && y<2000) if (d[x][y]>=0) return d[x][y];
	bool b=!arya(x-y,y);
	if (x<2000 && y<2000) d[x][y]=b;
	return b;
}

int main() {
	int TT;
	cin>>TT;
	memset(d,-1, sizeof d);
	for(int T=1;T<=TT;T++) {
		int a1,a2,b1,b2;
		cin>>a1>>a2>>b1>>b2;
		int ans=0;
		for(int i=a1;i<=a2;i++) for(int j=b1;j<=b2;j++) {
			bool b=arya(i,j);
			if (b) ans++;
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
