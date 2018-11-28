#include <cstdio>

bool mohl[101][101];

int main()
{
	for(int i=1; i<=100; i++) mohl[i][0]=true;
	for(int i=1; i<=100; i++) {
		for(int p=1; p<=100; p++) {
			bool mohl_dosahnout=false;
			for(int z=1; z<i; z++) mohl_dosahnout=mohl_dosahnout | mohl[z][p];
			mohl_dosahnout=mohl_dosahnout | ((i*p)%100==0);
			mohl[i][p]=mohl_dosahnout;
		}
	}
	int pocet; scanf("%d", &pocet);
	for(int test=1; test<=pocet; test++) {
		long long int N, Pd, Pg; scanf("%lld%lld%lld", &N, &Pd, &Pg);
		if(N>=100) {
			if((Pd<100 ? Pg<100 : 1) && (Pd>0 ? Pg>0 : 1)) printf("Case #%d: Possible\n", test);
			else printf("Case #%d: Broken\n", test);
		}
		else {
			if(mohl[N][Pd] && (Pd<100 ? Pg<100 : 1) && (Pd>0 ? Pg>0 : 1)) printf("Case #%d: Possible\n", test);
			else printf("Case #%d: Broken\n", test);
		}
	}

	return 0;
}
