#include <stdio.h>

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,t,i;
	int n,d,x;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		scanf("%d",&n);
		d = 0;
		for (i = 1;i <= n;i++)
		{
			scanf("%d",&x);
			if(i != x)
				d++;
		}
		printf("Case #%d: %d.000000\n",t,d);
	}
	return 0;
}