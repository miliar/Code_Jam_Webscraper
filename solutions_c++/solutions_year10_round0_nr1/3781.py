#include "stdio.h"
#include "math.h"

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);
	int T,N,K,i=0,temp,temp1;
	scanf("%d", &T);

	while(T)
	{
		scanf("%d %d", &N, &K);
		i++;
		temp = int(pow((float)2,(float)(N))) -1;
		temp1 = int(pow((float)2,(float)(N)));

		if(K >= temp )
		{
			if( (K-temp) % temp1 == 0)
				printf("Case #%d: %s\n",i,"ON");
			else
				printf("Case #%d: %s\n",i,"OFF");
		}
		else
			printf("Case #%d: %s\n",i,"OFF");
		
		T--;
	}
	return 0;
}