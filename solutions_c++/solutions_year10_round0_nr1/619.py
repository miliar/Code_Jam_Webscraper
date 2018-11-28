#include<cstdio>

#define FOR(x,y,z) for(int x=y;x<=z;++x)

int n, k;

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", z, k%(1<<n) == (1<<n)-1 ? "ON" : "OFF");
	}
	return 0;
}

