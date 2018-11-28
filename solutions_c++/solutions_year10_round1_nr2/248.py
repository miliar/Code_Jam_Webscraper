#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
typedef long long int64;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back
const int maxn = 101;
const int maxc = 256;
const int oo = maxn*maxc*2;
vi a;
int d[maxn][maxc];
int m,n;
int D,I;

int solve() {
	memset(d,0,sizeof(d));
	for (int i=1;i<=n;i++) {
		//from i-1 layer
		for (int j0=0;j0<maxc;j0++) d[i][j0] = d[i-1][j0]+D;
		for (int j0=0;j0<maxc;j0++) 
			for (int j=0;j<maxc;j++) if (j0-j<=m && j-j0<=m) {
				d[i][j] = min(d[i][j],d[i-1][j0]+abs(j-a[i]));	
			}

		//inside i-th layer
		bool fixed[maxc];
		memset(fixed,0,sizeof(fixed));		
		for (int turn=0;turn<maxc;turn++) {
			int minv = oo, minp;
			for (int j0=0;j0<maxc;j0++) if (!fixed[j0] &&  d[i][j0]<minv) {minv=d[i][j0];minp=j0;}
			fixed[minp] = true;
			int j0 = minp;
			for (int j=0;j<maxc;j++) if (j0-j<=m && j-j0<=m && d[i][j]>d[i][j0]+I) {
				d[i][j] = d[i][j0]+I;
			}
		}
		//for (int j0=0;j0<maxc;j0++) cout<<d[i][j0]<<" ";
		//cout<<endl;
	}
	return *min_element(d[n],d[n]+maxc);
}

int main() {
	int nTest;
	cin>>nTest;
	for (int test=1;test<=nTest;test++) {
		cin>>D>>I>>m>>n;
		a = vi(n+1);
		for (int i=0;i<n;i++) cin>>a[i+1];
		cout<<"Case #"<<test<<": "<<solve()<<endl;
	}
	return 0;
}
