#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef long long LL;
int main()
{
	LL t , i , j , k , l , p , c , ans;
	freopen("B-large.in","r",stdin);
	freopen("bl.out","w",stdout);
	scanf("%lld" , &t);
	for (k = 1;k <= t;k ++)	{
		scanf("%lld%lld%lld" , &l , &p , &c);
		LL cnt = 0;
		i = l;

		while (i<p)	{
			i=i*c;
			cnt ++;
		}
		j = 1;
		ans = 0;
		while (j<cnt)	{
			j = j*2;
			ans ++;
		}

		printf("Case #%lld: %lld\n" , k , ans);

	}
	return 0;
}