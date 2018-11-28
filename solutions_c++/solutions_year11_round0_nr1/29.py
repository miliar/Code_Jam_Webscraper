#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <math.h>

int main()	{
	int T=0;
	scanf("%d",&T);
	for(int k=0; k!=T; ++k)	{
		int N = 0, a[2] = {1,1};
		int r[2] = {0,0}; //n turns made
		int total = 0; // total = current
		scanf("%d",&N);
		for(int i=0; i!=N; ++i)	{
			char str[2];
			int x=0, pos=0;
			scanf("%s %d",str,&pos);
			x = (str[0]=='B');
			int need = abs(pos-a[x])+1;
			a[x] = pos;
			r[x] += need;
			if (r[x]<=r[1-x])
				r[x] = 1+r[1-x];
			total = r[x];
		}
		printf("Case #%d: %d\n",k+1,total);
	}
	return 0;
}

