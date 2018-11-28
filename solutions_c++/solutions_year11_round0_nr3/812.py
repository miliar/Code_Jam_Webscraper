#include <stdio.h>
#define M 1100000
int main()
{
	int n, m, a, t, ts, r, s;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), m=M, s=0, r=0; n--; scanf("%d", &a), s+=a, m=a<m?a:m, r^=a);
		printf("Case #%d: ", t+1);
		if(r) printf("NO\n");
		else printf("%d\n", s-m);
	}
	return 0;
}