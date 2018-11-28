//Arek Wróbel - skater
#include <cstdio>
typedef long long LL;
using namespace std;

LL r, k, n;
LL g[2001];
LL sum[2001];
LL jump[1001];

LL v;
bool vis[1001];
LL zap[1001];	//zapis gdzie dochodze po danej ilosci ruchow ze startu

LL wy;

inline LL binsjmp(const LL mv)	//mv - ostatni z poprzedniego
{
	int pocz=mv+1;
	int kon=mv+n;
	int sred;
	while (pocz+1<kon)
	{
		sred=(pocz+kon)/2;
		if (sum[sred]-sum[mv]>k)
			kon=sred; else
			pocz=sred;
	}
	if (sum[kon]-sum[mv-1]>k) return pocz;
	return kon;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		//wej
		scanf("%I64d", &r);
		scanf("%I64d", &k);
		scanf("%I64d", &n);
		for (int i=1; i<=n; ++i)
			scanf("%I64d", &g[i]);
		//prog
		//reset
		wy=0;
		for (int i=0; i<=n; ++i)
			vis[i]=false;
		//podwojenie tablicy
		for (int i=1; i<=n; ++i)
			g[i+n]=g[i];
		//sumy czesciowe
		g[0]=sum[0]=0;
		for (int i=1; i<=2*n; ++i)
		{
			sum[i]=sum[i-1]+g[i];
		}
		//tworzenie 'jump'
		for (int i=0; i<=n; ++i)
			jump[i]=binsjmp(i);
		//symulacja
		v=0;	//ostatni z poprzedniego
		for (int i=0; i<r; ++i)
		{
				wy+=sum[jump[v]]-sum[v];
				v=jump[v];
				if (v>=n) v-=n;
		}
		//wyj
		//for (int i=0; i<=2*n; ++i) printf("%2d: %2d %2d\n", i, g[i], sum[i]);//debug
		//for (int i=0; i<=n; ++i) printf("jump[%2d]: %2d\n", i, jump[i]);//debug
		printf("Case #%d: ", lpt);
		printf("%I64d\n", wy);
	}
	return 0;
}
