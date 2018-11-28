#include <stdio.h>
#include <cstring>

int main()
{
	int t, n, k, tc = 0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%d", &n, &k);
		int flag = 1;
		for(int i=1; i<=n && flag; ++i)
		{
			if(!(k & 1)) flag = 0;
			k >>= 1;
		}
		printf("Case #%d: ", ++tc);
		if(flag) puts("ON");
		else puts("OFF");
	}
	return 0;
}

