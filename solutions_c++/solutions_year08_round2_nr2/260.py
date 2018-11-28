#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MAXN 2000000

int kosk[MAXN];

int dset[MAXN];

int fset(int x) { 
	if(x != dset[x]) dset[x] = fset(dset[x]);
	return dset[x];
}

void uset(int x, int y) {
	dset[fset(y)] = fset(x);
}

__int64 gcd(__int64 a,__int64 b) {
	return b==0?a:gcd(b,a%b);
}

int main() {
	freopen("Bs.in","r",stdin);
	freopen("Bs.out","w",stdout);
	int n,N,i,j;
	__int64 A, B, P, a, b, p, cnt=0, d,t;
	for(i=2;i*i<MAXN;i++) {
		if(kosk[i]) continue;
		for(j=i*i;j<MAXN;j+=i) {
			kosk[j] = i;
		}
	}

	scanf("%d",&N);
	for(n=1;n<=N;n++) {
		scanf("%I64d %I64d %I64d", &A, &B, &P);
		for(i=0;i<=B-A;i++) dset[i] = i;
		for(a=A;a<=B;a++) {
			for(b=a+1;b<=B;b++) {
				if(fset(a-A) == fset(b-A)) continue;
				d = gcd(a,b);
				while(kosk[d]) {
					if(kosk[d]>=P) {
						uset(a-A,b-A);
						break;
					}
					d/=kosk[d];
				}
				if(d>=P) {
					uset(a-A,b-A);
				}
			}
		}
		cnt=0;
		for(i=0;i<=B-A;i++) {
			cnt += (fset(i)==i);
		}
		printf("Case #%d: %I64d\n",n,cnt);
	}
	return 0;
}