#include <cstdio>
#include <algorithm>
#include <cstring>
#define FOR(i,s,e) for (int i=(s); i<(int)(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(int)(e); i++)
using namespace std;

int C, D, Pd, Pg, Wd, G, Wg, ok;
long long n;

int main(){

	scanf("%d", &C);
	FOE(tc,1,C){

		ok = 1;
		scanf("%I64d%d%d", &n, &Pd, &Pg);
		
		D = 1;
		while (D * Pd %  4) D *= 2;
		while (D * Pd % 25) D *= 5;
		Wd = D * Pd / 100;
		
		if ((long long)D > n) ok = 0;

		G = 1;
		while (G * Pg %  4) G *= 2;
		while (G * Pg % 25) G *= 5;
		Wg = G * Pg / 100;
		
		if (Pg == 100 && Pd != 100) ok = 0;
		if (Pg == 0 && Pd != 0) ok = 0;
		
		
		printf("Case #%d: %s\n", tc, ok ? "Possible" : "Broken");

	}

	return 0;
}
