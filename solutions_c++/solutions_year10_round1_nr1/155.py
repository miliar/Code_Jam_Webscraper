#include <cstdio>
#include <cstring>
//#include <iostream>
#include <algorithm>
#include <cctype>
using namespace std;
const int c=55;
int t,ii;
int N,K;
bool qb,qr;
char a[c][c];
int main() {
	int i,j,k;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d%d\n",&N,&K);
		for (i=0; i<N; ++i) gets(a[i]);
		for (i=0; i<N; ++i) {
			for (j=N-1; j>=0; --j) if (a[i][j]!='.') {
				for (k=N-1; k>j; --k) if (a[i][k]=='.') break;
				swap(a[i][j],a[i][k]);
			}
		}
/*
		for (i=0; i<N; ++i) {
			for (j=0; j<N; ++j) cerr << a[i][j];
			cerr << '\n';
		}
*/
		qb=qr=0;
		for (i=0; i<N; ++i)
			for (j=0; j<N; ++j) {
				if (a[i][j]=='B' && !qb) {
					for (k=0; k<K; ++k) if (j+k>=N || a[i][j+k]!='B') break;
					if (k==K) qb=1;
					for (k=0; k<K; ++k) if (i+k>=N || a[i+k][j]!='B') break;
					if (k==K) qb=1;
					for (k=0; k<K; ++k) if (i+k>=N || j+k>=N || a[i+k][j+k]!='B') break;
					if (k==K) qb=1;
					for (k=0; k<K; ++k) if (i+k>=N || j-k<0 || a[i+k][j-k]!='B') break;
					if (k==K) qb=1;
				} else if (a[i][j]=='R' && !qr) {
					for (k=0; k<K; ++k) if (j+k>=N || a[i][j+k]!='R') break;
					if (k==K) qr=1;
					for (k=0; k<K; ++k) if (i+k>=N || a[i+k][j]!='R') break;
					if (k==K) qr=1;
					for (k=0; k<K; ++k) if (i+k>=N || j+k>=N || a[i+k][j+k]!='R') break;
					if (k==K) qr=1;
					for (k=0; k<K; ++k) if (i+k>=N || j-k<0 || a[i+k][j-k]!='R') break;
					if (k==K) qr=1;
				}
			}
		if (!qb && !qr) printf("Neither\n"); else
		if (qb && qr) printf("Both\n"); else
		if (qr && !qb) printf("Red\n"); else
		if (qb && !qr) printf("Blue\n");
	}
	return 0;
}