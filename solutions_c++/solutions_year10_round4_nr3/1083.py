#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>

using namespace std;

bool primo(int n) {
	if(n<=1)return false;
	for (int i=2; i*i <= n; i++) if (n%i==0) return false;
	return true;
}

int cn,cases,res,bac,r1,r2,c1,c2,sr,er,sc,ec,lr,mr,lc,mc,alt,past,n;
int world[200][200][2];

bool repr(int i, int j, int k) {
	if (i==0 || j==0) return false;
	if (world[i][j-1][k]==cn && world[i-1][j][k]==cn) return true;
	return false;
}

void dbg(int k) {
		for (int i=lr; i <= mr; ++i) {
			for (int j=lc; j <= mc; ++j) {
				if (world[i][j][k]==cn) printf("1");
				else printf("0");
			}
			printf("\n");
		}
		printf("\n");
}

bool die(int i, int j, int k) {
	if (i==0&&j==0) return true;
	else if (i==0) {
		if (world[i][j-1][k]!=cn) return true;
		return false;
	} else if (j==0) {
		if (world[i-1][j][k]!=cn) return true;
		return false;
	}
	
	if (world[i][j-1][k]!=cn && world[i-1][j][k]!=cn) return true;
	return false;
}

void simul() {
	alt=1;
	res=0;
	while (bac>0) {
		past=(alt+1)&1;
		++res;
		for (int i=lr; i <= mr; ++i) {
			for (int j=lc; j <= mc; ++j) {
				world[i][j][alt]=world[i][j][past];
				if (world[i][j][alt] != cn) {
					if (repr(i,j,past)) {
						world[i][j][alt]=cn;
						++bac;
					}
				}
				if (world[i][j][alt] == cn) {
					if (die(i,j,past)) {
						world[i][j][alt]=cn-1;
						--bac;
					}
				}
				
			}
		}
		//dbg(alt);
		alt=(alt+1)&1;
	}
}

bool read() {
	scanf("%d",&n);
	bac=0;
	lr=0x7f7f7f7f;
	mr=-1;
	lc=lr;
	mc=mr;
	for (int k=0; k < n; ++k) {
		scanf("%d %d %d %d",&c1,&r1,&c2,&r2);
		sr=min(r1,r2);
		er=max(r1,r2);
		sc=min(c1,c2);
		ec=max(c1,c2);
		lr=min(lr,sr);
		mr=max(mr,er);
		lc=min(lc,sc);
		mc=max(mc,ec);
		for (int i=sr; i <= er; ++i) {
			for (int j=sc; j <= ec; ++j) {
				if (world[i][j][0]==cn) continue;
				world[i][j][0]=cn;
				++bac;
			}
		}
	}
	//dbg(0);
}

void process() {
	simul();
	printf("Case #%d: %d\n",cn,res);
	fflush(stdout);
}

int main() {
	scanf("%d",&cases);
	for (cn=1; cn <= cases; ++cn) {
		read();
		process();
	}
	return 0;
}
