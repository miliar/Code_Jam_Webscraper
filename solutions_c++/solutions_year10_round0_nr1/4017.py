#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int cas, maxcas;
	int n, k;

	scanf("%d\n",&maxcas);

	for(cas = 1; cas <= maxcas; cas++) {
		scanf("%d %d\n",&n ,&k);
		while(--n) {
			if(k&1) k /= 2;
			else {
				k = 0;
				break;
			}
		}
		if(k&1) printf("Case #%d: ON\n",cas);
		else printf("Case #%d: OFF\n",cas);
	}

	return 0;
}