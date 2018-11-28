
#include <cstdio>
#include <algorithm>
using namespace std;

#define NN 1002
double fact[NN], exp[NN];
double cwrong[NN], bine[NN][NN];

double pb(int i, int m) {
	return bine[i][m]/fact[i]*cwrong[i-m];
}

main() {
	/*int a[50];
	for (int n=1; n<11; n++) {
		for (int i=0; i<n; i++) a[i]=i;
		int prm=0, cnt=0;
		do {
			prm++; cnt++;
			for (int i=0; i<n; i++) if (a[i]==i) {
				cnt--;
				break;
			}
		} while (next_permutation(a,a+n));
		printf(" prm[%d]=%d nomatched=%d\n", n, prm, cnt);
	}*/
	
	/*bine[0][0]=1;
	for (int n=1; n<NN; n++) {
		bine[n][0]=bine[n][n]=1;
		for (int c=1; c<n; c++) bine[n][c]=bine[n-1][c-1] + bine[n-1][c];
	}

	fact[0]=fact[1]=1;
	for (int i=2; i<NN; i++) fact[i]=i*fact[i-1];
	
	cwrong[0]=cwrong[1]=0;
	for (int i=2; i<NN; i++) {
		cwrong[i]=fact[i]-1;
		for (int ma=1; ma<i; ma++) if (i-ma!=1) {
			cwrong[i] -= bine[i][ma]*cwrong[i-ma];
		}
		//if (i<11) printf("   cwro[%d]=%.3lf\n", i, cwrong[i]);
	}
	
	exp[0]=exp[1]=0;
	for (int i=2; i<1002; i++) {
		double up=1;
		for (int m=1; m<i-1; m++) up += pb(i,m)*exp[i-m];
		exp[i]=up/(1-pb(i,0));
		//if (i<10) printf("   exp[%d]=%.6lf\n", i, exp[i]);
	}*/

	int ntc, n;
	scanf("%d", &ntc);
	for (int test=1; test<=ntc; test++) {
		scanf("%d", &n);
		int x, unm=0;
		for (int i=1; i<=n; i++) {
			scanf("%d",&x);
			if (x!=i) unm++;
		}
		printf("Case #%d: %d\n", test, unm);
	}
}
