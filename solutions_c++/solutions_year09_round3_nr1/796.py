#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int list[300];
int mark[100];

int main()
{
	long long ans, d, max;
	int aa, nn, i, j, len;
	char buffer[100];
	gets(buffer);
	nn = atoi(buffer);
	for (aa = 1; aa<= nn; ++aa)
	{
		gets(buffer);
		len = strlen(buffer);
		max = 1;
		memset(list,-1,sizeof(list));
		memset(mark,0,sizeof(mark));
		list[buffer[0]] = 1;
		mark[1] = 1;
		for ( i = 1; i < len; ++i )
		{
			if ( list[buffer[i]] >= 0 ) continue;
			j = 0;
			while (mark[j]) j++;
			list[buffer[i]] = j;
			mark[j]= 1;
			max++;
		}
		d = 1;
		ans = 0;
		if ( max == 1) max = 2;
		for ( i = len-1; i >= 0; --i )
		{
			//printf("%d\n",list[buffer[i]]);
			ans += d*list[buffer[i]];
			d *= max;
		}
		printf("Case #%d: %lld\n",aa,ans);
	}
	return 0;
}
