//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)

int n;
char bl[200];
int p[200];

int v1, v2;	//1 Orange, 2 Blue
int poz1, poz2;

int wy=0;

void make1()
{
	if (v1<v2 && poz1==p[v1]){
		++v1;
		return;
	}
	if (poz1<p[v1]) ++poz1;
	if (poz1>p[v1]) --poz1;
}

void make2()
{
	if (v2<v1 && poz2==p[v2]){
		++v2;
		return;
	}
	if (poz2<p[v2]) ++poz2;
	if (poz2>p[v2]) --poz2;
}

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		scanf("%d", &n);
		REP(i, n)
			scanf(" %c%d", &bl[i], &p[i]);
		//prog
		wy=v1=v2=0;
		poz1=poz2=1;
		for (wy=0; v1<n || v2<n; ++wy){
			while(bl[v1]=='B') ++v1;
			while(bl[v2]=='O') ++v2;
			make1();
			make2();
		}
		//wyj
		printf("Case #%d: %d\n", lpt, wy);
	}
	return 0;
}

