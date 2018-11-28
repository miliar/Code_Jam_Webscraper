#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <cmath>
//#include <iostream>
using namespace std;
typedef long long ll;
int t,ii;
const int c=512;
int w[c][c];
int n,m,d;
inline ll ds (int ii, int i, int k) {
	double d=fabs(ii-(i+k/2.0-0.5));
	if (ii==i || ii==i+k-1) d-=0.5;
	return ll(d*2+1e-6);
}
inline bool ok(int k, int i, int j) {
	ll s1,s2;
	int ii,jj;
	if (k%2) {
		s1=s2=0;
		for (ii=i; ii<i+k; ++ii)
			for (jj=j; jj<j+k; ++jj)
				if (!(ii==i && jj==j || ii==i && jj==j+k-1 || ii==i+k-1 && jj==j || ii==i+k-1 && jj==j+k-1))
					if (ii<i+k/2) s1+=w[ii][jj]*ds(ii,i,k); else
					if (ii>=i+k/2+1) s2+=w[ii][jj]*ds(ii,i,k);
//		if (k==5 && i==2 && j==2) cerr << s1 << ' ' << s2 << '\n';
		if (s1!=s2) return 0;
		s1=s2=0;
		for (ii=i; ii<i+k; ++ii)
			for (jj=j; jj<j+k; ++jj)
				if (!(ii==i && jj==j || ii==i && jj==j+k-1 || ii==i+k-1 && jj==j || ii==i+k-1 && jj==j+k-1))
					if (jj<j+k/2) s1+=w[ii][jj]*ds(jj,j,k); else
					if (jj>=j+k/2+1) s2+=w[ii][jj]*ds(jj,j,k);
//		if (k==5 && i==2 && j==2) cerr << s1 << ' ' << s2 << '\n';
		if (s1!=s2) return 0;
	} else {
		s1=s2=0;
		for (ii=i; ii<i+k; ++ii)
			for (jj=j; jj<j+k; ++jj)
				if (!(ii==i && jj==j || ii==i && jj==j+k-1 || ii==i+k-1 && jj==j || ii==i+k-1 && jj==j+k-1))
					if (ii<i+k/2) s1+=w[ii][jj]*ds(ii,i,k); else
					if (ii>=i+k/2) s2+=w[ii][jj]*ds(ii,i,k);
		if (s1!=s2) return 0;
		s1=s2=0;
		for (ii=i; ii<i+k; ++ii)
			for (jj=j; jj<j+k; ++jj)
				if (!(ii==i && jj==j || ii==i && jj==j+k-1 || ii==i+k-1 && jj==j || ii==i+k-1 && jj==j+k-1))
					if (jj<j+k/2) s1+=w[ii][jj]*ds(jj,j,k); else
					if (jj>=j+k/2) s2+=w[ii][jj]*ds(jj,j,k);
		if (s1!=s2) return 0;
	}
	return 1;
}
int main() {
	scanf("%d",&t);
//	cerr << ds(6,2,5) << '\n';
	int i,j,k;
	char h;
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d%d%d",&n,&m,&d);
		for (i=1; i<=n; ++i)
			for (j=1; j<=m; ++j) {
				do h=getchar(); while (!isdigit(h));
				w[i][j]=h-'0';				
			}
/*
		for (i=1; i<=n; ++i) {
			for (j=1; j<=m; ++j) cerr << w[i][j] << ' ';
			cerr << '\n';
		}
		cerr << '\n';
*/
		for (k=min(n,m); k>=3; --k) {
			for (i=1; i+k-1<=n; ++i) {
				for (j=1; j+k-1<=m; ++j)
					if (ok(k,i,j)) {
						printf("%d\n",k);
						break;
					}
				if (j+k-1<=m) break;
			}
			if (i+k-1<=n) break;
		}
		if (k<3) printf("IMPOSSIBLE\n");
	}
	return 0;
}