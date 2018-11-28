#include<iostream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n, k;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas){
		scanf("%d%d", &n, &k);
		int mask = (1 << n) - 1;		
		if((k & mask) == mask) printf("Case #%d: ON\n", cas);
		else printf("Case #%d: OFF\n", cas);
	}
	return 0;
}