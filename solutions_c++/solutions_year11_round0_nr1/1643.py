#include<stdio.h>
#include<string.h>

#define Max(a,b) ((a) > (b) ? (a) : (b))
#define mabs(a) ((a)>0?(a):-(a))

char s[105][10];
int pos[105];

int main()
{
	freopen("bot2.in","r",stdin);
	freopen("bot2.out","w",stdout);
	int t,n,i,lasto,lastb,to,tb,cs=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		lasto = lastb = 1;
		to = 0, tb = 0;
		int now;
		for(i=0;i<n;i++)
		{
			scanf("%s%d",s[i],&pos[i]);
			if(s[i][0]=='O')
			{
				now = mabs(pos[i] - lasto);
				to = Max(to+now,tb);
				to++;
				lasto = pos[i];
			}
			else
			{
				now = mabs(pos[i] - lastb);
				tb = Max(tb+now,to);
				tb++;
				lastb = pos[i];
			}
		}
		printf("Case #%d: %d\n",++cs,Max(tb,to));
	}
	return 0;
}