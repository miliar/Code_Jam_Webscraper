#include<cstdio>
int S, xS, mN;
int main(){
	int T;
	scanf("%d", &T);
	int n;
	for (int it=1; it<=T; it++){
		scanf("%d", &n);
		S = 0;
		xS = 0;
		mN = 100000000;
		int t;
		for (int i=0; i<n; i++){
			scanf("%d", &t);
			S += t;
			xS ^= t;
			if (t<mN)
				mN = t;
		}
		if (xS != 0)
			printf("Case #%d: NO\n", it);
		else
			printf("Case #%d: %d\n", it, S-mN);
	}
	return 0;
}
