#include <stdio.h>
#define N 110
int mx(int x, int y) { return x>y?x:y; }
int ab(int x) { return x<0?-x:x; }
int main()
{
	int n, t1, t2, p1, p2, p, t, ts;
	char s[5];
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(t1=0, t2=0, p1=1, p2=1, scanf("%d", &n); n--; )
		{
			scanf("%s%d", s, &p);
			if(s[0]=='O') { t1=mx(t2, t1+ab(p-p1))+1; p1=p; }
			else { t2=mx(t1, t2+ab(p-p2))+1; p2=p; }
		}
		printf("Case #%d: %d\n", t+1, mx(t1, t2));
	}
	return 0;
}