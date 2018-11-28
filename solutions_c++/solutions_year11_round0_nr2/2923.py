#include <stdio.h>
#include <string.h>

char a[200];
char b[200];
char com[27][27];
int opp[27][27];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, Case=1;
	scanf("%d", &T);
	while(T--)
	{
		int i, j, n, x, y, len, found;
		char tmp[5];
		scanf("%d", &x);
		memset(com, 0, sizeof(com));
		for (i=0; i<x; i++)
		{
			scanf("%s", tmp);
			com[tmp[0]-'A'][tmp[1]-'A']=tmp[2];
			com[tmp[1]-'A'][tmp[0]-'A']=tmp[2];
		}
		scanf("%d", &y);
		memset(opp, 0, sizeof(opp));
		for (i=0; i<y; i++)
		{
			scanf("%s", tmp);
			opp[tmp[0]-'A'][tmp[1]-'A']=1;
			opp[tmp[1]-'A'][tmp[0]-'A']=1;
		}
		scanf("%d%s", &n, a);
		memset(b, 0, sizeof(b));

		len=0;
		for (i=0; i<n; i++)
		{
			if(len>0 && com[b[len-1]-'A'][a[i]-'A']!=0) //组合
			{
				b[len-1]=com[b[len-1]-'A'][a[i]-'A'];
			}
			else
			{
				found=0;
				for (j=0;j<len;j++) //查找相斥的
				{
					if(opp[b[j]-'A'][a[i]-'A']==1) { len=0; found=1; break; }
				}
				if(found==0) //没有相斥的
				{
					b[len]=a[i];
					len++;
				}
			}
		}

		printf("Case #%d: [", Case++);
		for (i=0; i<len; i++)
		{
			if(i==0) printf("%c", b[i]);
			else printf(", %c", b[i]);
		}
		printf("]\n");
	}
	return 0;
}