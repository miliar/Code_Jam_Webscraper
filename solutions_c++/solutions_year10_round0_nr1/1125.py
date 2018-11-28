#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, i, j, n, k, cas = 0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %d",&n, &k);
		n = (1 << n);
		if(k % n == n - 1)
			printf("Case #%d: ON\n", ++cas);
		else 
			printf("Case #%d: OFF\n", ++cas);	
	}		
}