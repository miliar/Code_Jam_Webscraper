#include <stdio.h>

int o[1000], b[1000];
char col[1000];
int lcol;
int ol, bl, ml;

int t;
int l;
char s[5];
char c;
int p;
int pi;
int op, bp;
int orp, brp;
int time;

int main()
{
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\outputLargeA.txt", "wt", stdout);

	scanf("%d", &t);
	for (int test=1; test<=t; test++)
	{
		ol=0;
		bl=0;
		lcol=0;
		time=0;
		scanf("%d", &l);
		for (int i=0; i<l; i++)
		{
			scanf("%s%d", s, &p);
			c = s[0];
			if (c=='O')
			{
				o[ol++]=p-1;
			}
			else
			{
				b[bl++]=p-1;
			}
			col[lcol++]=c;
		}

		pi=0; op=0; bp=0;
		orp=0; brp=0;

		for (time=0; pi<lcol; )
		{
			if (col[pi]=='O')
			{
				while (orp!=o[op])
				{
					orp+=o[op]>orp?1:-1;
					if (brp!=b[bp])
					{
						brp+=b[bp]>brp?1:-1;
					}
					time++;
				}
				time++;
				if (brp!=b[bp])
				{
					brp+=b[bp]>brp?1:-1;
				}
				op++;
				pi++;
			}
			else
			{
				while (brp!=b[bp])
				{
					brp+=b[bp]>brp?1:-1;
					if (orp!=o[op])
					{
						orp+=o[op]>orp?1:-1;
					}
					time++;
				}
				time++;
				if (orp!=o[op])
				{
					orp+=o[op]>orp?1:-1;
				}
				bp++;
				pi++;
			}
		}
		if (test!=0)
		{
			printf("\n");
		}
		printf("Case #%d: %d", test, time);
	}

	return 0;
}