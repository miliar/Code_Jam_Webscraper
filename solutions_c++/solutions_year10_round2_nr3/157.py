#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
using namespace std;

typedef long long int64;

#define MOD 100003

int64 f[501][501];

//combinations C[n][r]
int64 C[2001][2001];
void comb(int lim) {
	int n,r;
	memset(C,0,sizeof(C));
	C[0][0]=1;
	for (n=1;n<=lim;n++) {
		C[n][0]=1;
		for (r=1;r<=n-1;r++) {
			C[n][r]=(C[n-1][r-1]+C[n-1][r])%MOD;
		}
		C[n][n]=1;
	}
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	comb(2000);
	int tests;
    scanf("%d",&tests);
    for (int ti=1;ti<=tests;ti++) {
    	fprintf(stderr,"%d/%d\r",ti,tests);
    	int N;
    	scanf("%d",&N);
    	memset(f,0,sizeof(f));
    	for (int n=2;n<=N;n++) {
    		f[1][n]=1;
    	}
    	int r=1;
    	for (int k=2;k<=N;k++) {
			for (int n=k+1;n<=N;n++) {
				for (int k2=k-1;k2>=1;k2--) {
					int p=k-k2-1;
					int num=n-k-1;
					f[k][n]+=f[k2][k]*C[num][p];
					f[k][n]%=MOD;
				}
				//printf("%d %d: %d\n",k,n,f[k][n]);
			}
			r+=f[k][N];
			r%=MOD;
    	}

    	printf("Case #%d: %d\n",ti,r);
    	fflush(stdout);
    }
    return 0;
}
