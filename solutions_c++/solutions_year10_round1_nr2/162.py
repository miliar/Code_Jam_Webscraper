#include <cstdio>
#include <algorithm>
//#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;
const int c=300;
const int inf=1000000;
int t,ii;
int D,I,M,N;
int r[c][c];
int a[c];
inline int f(int p, int k, int M) {
	if (p==k) return 0;
	if (M==0) return inf;
	return ((abs(p-k)+M-1)/M)*I;
}
int ans;
int main() {
	int i,j,k,p;
	int d;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d%d%d%d",&D,&I,&M,&N);
//		cerr << D << ' ' << I << ' ' << M << ' ' << N << '\n';
		for (i=1; i<=N; ++i) scanf("%d",&a[i]);
		for (i=0; i<256; ++i) r[0][i]=0;
		for (i=1; i<=N; ++i)
			for (k=0; k<256; ++k) {
				r[i][k]=r[i-1][k]+D;
				for (p=0; p<256; ++p) {
					d=min(255,p+M);
					for (j=max(0,p-M); j<=d; ++j) r[i][k]=min(r[i][k],r[i-1][j]+abs(a[i]-p)+f(p,k,M));
				}
			}
/*
		for (i=1; i<=N; ++i) {
			for (j=0; j<=7; ++j) cerr << r[i][j] << ' ';
			cerr << '\n';
		}
*/
		ans=inf;
		for (i=0; i<256; ++i) ans=min(ans,r[N][i]);
		printf("%d\n",ans);
	}
	return 0;
}