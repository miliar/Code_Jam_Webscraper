#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std ;


int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out.txt", "w", stdout);
	int n, kase ,k, i, j, l, ans;
	char str[1100] ;
	scanf("%d", &n);
	for(kase = 1; kase <= n; kase ++)
	{
		ans = 99999999;
		scanf("%d", &k );
		scanf("%s", str);
		char tmp[1100];
		int per[10];
		for(j = 0; j < k; j ++)
			per[j] = j;
		int div = strlen(str) / k;
		do
		{
			for(j = 0; j < div; j ++)
			{
				for( l = 0; l < k; l ++)
				{
					tmp[j * k + per[l]] = str[j * k + l] ;
				}	
			}
			int cnt = 0 ;
			int lst = -1 ;
			for(j = 0; j < strlen(str); j ++)
			{
				if(lst != tmp[j])
				{
					cnt ++;
					lst = tmp[j];	
				}				
			}
			if(cnt < ans)
				ans = cnt ;
//			printf("%s\n",tmp);
			
		}while(next_permutation(per, per + k));
		printf("Case #%d: %d\n", kase, ans);
	}
//	system("pause");
	return 0;    
}
