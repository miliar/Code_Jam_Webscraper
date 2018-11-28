#include <cstdio>

int main(void)
{
	int cases;
	
	scanf("%d", &cases);
	
	for(int t = 1; t <= cases ; ++t )
	{
		int n , k;
		scanf("%d %d", &n, &k);
		
		int res = k%(1<<n);
		
		if( res == (1<<n)-1 ) 
			printf("Case #%d: ON\n", t);
		else
			printf("Case #%d: OFF\n", t);
		
	}
	return 0;
}
