#include <iostream>
#include <cmath>
using namespace std;

int a[200];
int n,m,dc,ic;
int d[200][300];
int q[300][300];

void dbg() {
			for(int i=0;i<n;i++) {
			for(int j=0;j<10;j++) cerr<<d[i][j]<<' ';
			cerr<<endl;
		}
}
void makeq() {
	for(int i=0;i<256;i++) {
		for(int j=0;j<256;j++) {
			if (abs(i-j)<=m) q[i][j]=ic;
			else q[i][j]=214748364;
		}
		q[i][i]=0;
	}
	for(int k=0;k<256;k++) for(int i=0;i<256;i++) {
		for(int j=0;j<256;j++) 
			if (q[k][j]+q[i][k]<q[i][j]) q[i][j]=q[k][j]+q[i][k];
	}
	//for(int i=0;i<8;i++) for(int j=0;j<8;j++) cerr<<'q'<<i<<j<<' '<<q[i][j]<<endl;
}

void wi(int p) {
	for(int i=0;i<256;i++) for(int j=0;j<256;j++)
		if (d[p][i]+q[i][j]<d[p][j]) d[p][j]=d[p][i]+q[i][j];
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>dc>>ic>>m>>n;
		cout<<"Case #"<<T<<": ";
		for(int i=0;i<n;i++) cin>>a[i];
		makeq();
		for(int j=0;j<256;j++) {
			int t=abs(j-a[0]);
			if (t<dc) d[0][j]=t;
			else d[0][j]=dc;
		}
		//dbg();
		wi(0);
		for(int i=1;i<n;i++) {
			for(int j=0;j<256;j++) {
				d[i][j]=dc+d[i-1][j];
				int s=abs(a[i]-j);
				for(int z=0;z<256;z++) if (abs(z-j)<=m) {
					int t=s+d[i-1][z];
					if (t<d[i][j]) d[i][j]=t;
				}
			}
			wi(i);
		}
		//dbg();
		int ans=214748364;
		for(int j=0;j<256;j++) if (d[n-1][j]<ans) ans=d[n-1][j];
		cout<<ans<<endl;
	}
	return 0;
}
