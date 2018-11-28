#include <stdio.h>
#include <math.h>
#include <limits.h>
typedef long long I;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int c,n,m,x;
	I s;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		s = 0;
		x = 0;
		m = INT_MAX;
		scanf("%d",&n);
		while (n--)
		{
			scanf("%d",&c);
			x = x ^ c;
			s += c;
			if(m > c)
				m = c;
		}
		printf("Case #%d: ",t);
		if(x != 0)
			printf("NO\n");
		else
			printf("%lld\n",s-m);
	}
	return 0;
}