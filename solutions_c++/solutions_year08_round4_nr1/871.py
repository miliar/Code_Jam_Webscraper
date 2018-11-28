#include <stdio.h>
#include <iostream>
#include <algorithm>

#define MAXINT 1000000000

using namespace std;

bool Tree[1000000];
bool BoolTree[1000000];
int isi[1000000];
int DP[1000000][5];

inline int left(int idx) {
	return idx*2+1;
}

inline int right(int idx) {
	return idx*2+2;
}

int f(int idx, int val) {
	// 1 is AND 0 is OR
	// 1 is changable
	int ret=MAXINT;
	// If child
	//printf("%d %d\n", idx, val);
	if (DP[idx][val]>-1) return DP[idx][val];
	// If not changable and must be 1.
	if (BoolTree[idx]==0 && val==1) {
		// If and then both must 1.
		if (Tree[idx]==1)
			ret=min(ret, f(left(idx), 1)+f(right(idx), 1));
		else {
			// else either must 1.
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1));
			ret=min(ret, f(left(idx), 1)+f(right(idx), 1));
		}
	} else if (BoolTree[idx]==0 && val==0) {
		if (Tree[idx]==1) {
			// 1 0, 0 1, 0 0.
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 0));
		} else {
			// Just 0 0 if OR.
			ret=min(ret, f(left(idx), 0)+f(right(idx), 0));
		}
	// If changable
	} else if (Tree[idx]==1) {
		if (val==1) {
			// If AND and val==1
			ret=min(ret, f(left(idx), 1)+f(right(idx), 1));
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0)+1);
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1)+1);
		} else {
			// if val=0 then either is 0.
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 0));
		}
	} else if (Tree[idx]==0) {
		// If or
		if (val==1) {
			// if val==1 then either must be 1
			ret=min(ret, f(left(idx), 1)+f(right(idx), 1));
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0));
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1));
		} else {
			// if val==0 then, both must be 0 or either 1.
			ret=min(ret, f(left(idx), 1)+f(right(idx), 0)+1);
			ret=min(ret, f(left(idx), 0)+f(right(idx), 1)+1);
			ret=min(ret, f(left(idx), 0)+f(right(idx), 0));
		}
	} else
		printf("Halo\n");
	DP[idx][val]=ret;
	return ret;
}

int main() {
	int nTC;
	scanf("%d", &nTC);
	for (int kasus=1; kasus<=nTC; kasus++) {
		int hasil=MAXINT;
		int nV, mau;
		scanf("%d %d", &nV, &mau);
		//printf("-%d %d\n", nV, mau);
		memset(DP, -1, sizeof(DP));
		for (int j=0; j<(nV-1)/2; j++) {
			isi[j]=-1;
			scanf("%d %d", &Tree[j], &BoolTree[j]);
		}
		for (int j=(nV-1)/2; j<nV; j++) {
			scanf("%d", &isi[j]);
			DP[j][isi[j]]=0;
			DP[j][(isi[j]+1)%2]=MAXINT;
		}
		//for (int j=0; j<nV; j++)
		//	printf("%d ", isi[j]);
		//printf("\n");
		hasil=f(0, mau);
		if (hasil==MAXINT)
			printf("Case #%d: IMPOSSIBLE\n", kasus);
		else
			printf("Case #%d: %d\n", kasus, hasil);
	}
	
	return 0;
}
