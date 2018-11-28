#include <cstdio>
#include <cstring>
//#include <iostream>
using namespace std;
const int c=1024;
int m[c];
int a[c][c][12];
int p[c][c];
int t,ii;
int n,ans;
int main() {
	int i,j,k,o;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=0; i<(1<<n); ++i) scanf("%d",&m[i]);
		for (i=1; i<=n; ++i)
			for (j=0; j<(1<<(n-i)); ++j) scanf("%d",&p[i][j]);
		memset(a,-1,sizeof(a));
		for (i=0; i<(1<<n); ++i) a[0][i][m[i]]=0;
		for (i=1; i<=n; ++i)
			for (j=0; j<(1<<(n-i)); ++j)
				for (k=0; k<=10; ++k) {
					for (o=k; o<=10; ++o) {
					if (a[i-1][j*2][k]>=0 && a[i-1][j*2+1][o]>=0)
						if (a[i][j][k]==-1 || a[i][j][k]>a[i-1][j*2][k]+a[i-1][j*2+1][o]+p[i][j])
							a[i][j][k]=a[i-1][j*2][k]+a[i-1][j*2+1][o]+p[i][j];
					if (a[i-1][j*2][o]>=0 && a[i-1][j*2+1][k]>=0)
						if (a[i][j][k]==-1 || a[i][j][k]>a[i-1][j*2][o]+a[i-1][j*2+1][k]+p[i][j])
							a[i][j][k]=a[i-1][j*2][o]+a[i-1][j*2+1][k]+p[i][j];
					if (a[i-1][j*2][k+1]>=0 && a[i-1][j*2+1][o+1]>=0)
						if (a[i][j][k]==-1 || a[i][j][k]>a[i-1][j*2][k+1]+a[i-1][j*2+1][o+1])
							a[i][j][k]=a[i-1][j*2][k+1]+a[i-1][j*2+1][o+1];
					if (a[i-1][j*2][o+1]>=0 && a[i-1][j*2+1][k+1]>=0)
						if (a[i][j][k]==-1 || a[i][j][k]>a[i-1][j*2][o+1]+a[i-1][j*2+1][k+1])
							a[i][j][k]=a[i-1][j*2][o+1]+a[i-1][j*2+1][k+1];
 				}
		}
/*
		for (i=0; i<=n; ++i) {
			for (j=0; j<(1<<(n-i)); ++j) {
				for (k=0; k<=10; ++k) cerr << a[i][j][k] << ' ';
				cerr << "; ";
			}
			cerr << '\n';
		}
*/
		ans=-1;
		for (i=0; i<=10; ++i) if (a[n][0][i]>=0) if (ans==-1 || ans>a[n][0][i]) ans=a[n][0][i];
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}