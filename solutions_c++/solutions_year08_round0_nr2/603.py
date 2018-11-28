#include<stdio.h>
#include<string.h>
struct AA
{
	int sta,end;
}aa[105];
struct BB
{
	int fro,to;
}bb[105];
int main()
{
	int ca, na, nb, ta, tb, t, i, j, k, len, pos, leap;
	int flaga[105], flagb[105];
	char str1[15], str2[105];
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &ca);
	for(i=1; i<=ca; i++)
	{
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);
		for(j=0; j<na; j++)
		{
			scanf("%s %s", str1, str2);
			len = strlen(str1);
			aa[j].sta = ((str1[0] - '0') * 10 + (str1[1] - '0')) * 60;
			aa[j].sta = aa[j].sta + (str1[3] - '0') * 10 + (str1[4] - '0');
			aa[j].end = ((str2[0] - '0') * 10 + (str2[1] - '0')) * 60;
			aa[j].end = aa[j].end + (str2[3] - '0') * 10 + (str2[4] - '0');
		}
		for(j=0; j<nb; j++)
		{
			scanf("%s %s", str1, str2);
			len = strlen(str1);
			bb[j].fro = ((str1[0] - '0') * 10 + (str1[1] - '0')) * 60;
			bb[j].fro = bb[j].fro + (str1[3] - '0') * 10 + (str1[4] - '0');
			bb[j].to = ((str2[0] - '0') * 10 + (str2[1] - '0')) * 60;
			bb[j].to = bb[j].to + (str2[3] - '0') * 10 + (str2[4] - '0');
		}
		ta = na;
		tb = nb;
		memset(flaga, 0, sizeof(flaga));
		memset(flagb, 0, sizeof(flagb));
		for(j=0; j<na; j++)
		{
			int min = 999999;
			leap = 0;
			for(k=0; k<nb; k++)
			{
				if((aa[j].end + t) <= bb[k].fro && !flagb[k])
				{
					if(min > (bb[k].fro - aa[j].end - t))
					{
						min = bb[k].fro - aa[j].end - t;
						pos = k;
						leap = 1;
					}
				}
			}
			if(leap == 1)
			{
				flagb[pos] = 1;
				tb --;
			}
		}

		for(j=0; j<nb; j++)
		{
			int min = 999999;
			leap = 0;
			for(k=0; k<na; k++)
			{
				if((bb[j].to + t) <= aa[k].sta && !flaga[k])
				{
					if(min > (aa[k].sta - bb[j].to - t))
					{
						min = aa[k].sta - bb[j].to - t;
						pos = k;
						leap = 1;
					}
				}
			}
			if(leap == 1)
			{
				flaga[pos] = 1;
				ta --;
			}
		}
		printf("Case #%d: %d %d\n", i, ta, tb);
	}
	return 0;
}