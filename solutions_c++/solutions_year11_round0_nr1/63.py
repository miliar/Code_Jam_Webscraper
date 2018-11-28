#include <stdio.h>

#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(x) (((x)<0)?(-(x)):(x))

int cases, n;

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		scanf(" %d", &n);
		int ot=0, bt=0, op=1, bp=1, t=0;
		for(int i=0; i<n; i++)
		{
			int pos;
			char c;
			scanf(" %c %d", &c, &pos);
			if (c=='O')
			{
				ot=MAX(ABS(op-pos)+ot, t)+1;
				op=pos;
				t=ot;
			}
			else
			{
				bt=MAX(ABS(bp-pos)+bt, t)+1;
				bp=pos;
				t=bt;
			}
		}
		printf("Case #%d: %d\n", cs, t);
	}
	return 0;
}
