#include<stdio.h>
#include<stdlib.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	int n;
	scanf("%d",&t);
	for(int tt=0;tt<t;tt++)
	{
		scanf("%d",&n);
		int now1,now2;
		char s[101];
		now1=now2=1;
		int t1=0,t2=0;
		for(int i=0;i<n;i++)
		{
			int d;
			scanf("%s %d",s,&d);
			if(s[0]=='O')
			{
				t1+=abs(now1-d)+1;
				now1=d;
				if(t1<=t2) t1=t2+1;
			}
			else
			{
				t2+=abs(now2-d)+1;
				now2=d;
				if(t2<=t1) t2=t1+1;
			}
		}
		if(t2>t1) t1=t2;
		printf("Case #%d: %d\n",tt+1,t1);
	}
	return 0;
}
