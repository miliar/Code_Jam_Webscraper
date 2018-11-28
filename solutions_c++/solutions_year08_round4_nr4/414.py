#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std ;


int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int n, kase ,k;
    int i, j, l, ans;
    int div,total,itmp;
	char str[1110] ;
	char strtmp[1100];
	int per[10];
	scanf("%d", &n);
	for(kase = 1; kase <= n; kase ++)
	{
		ans = 10000000;
		scanf("%d", &k );
		scanf("%s", str);
		
		for(j = 0; j < k; j ++)
			per[j] = j;
		
        div = strlen(str) / k;
		do
		{
			for(j = 0; j < div; j ++)
			{
				for( l = 0; l < k; l ++)
				{
					strtmp[j * k + per[l]] = str[j * k + l] ;
				}	
			}
			total = 0 ;
			itmp = -1 ;
			for(j = 0; j < strlen(str); j ++)
			{
				if(itmp != strtmp[j])
				{
					total ++;
					itmp = strtmp[j];	
				}				
			}
			if(total < ans)
				ans = total ;
			
		}while(next_permutation(per, per + k));
		printf("Case #%d: %d\n", kase, ans);
	}
	
	return 0;    
}
