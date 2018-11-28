#include <stdio.h>

int n,cap,rd;
int a[1001];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int ct,cs=1;
	scanf("%d",&ct);
	while(ct--)
	{
		printf("Case #%d: ",cs++);
        scanf("%d%d%d",&rd,&cap,&n);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		int t = 0;
		for(i=0;i<n;i++)
			t += a[i];
		if(t<=cap)
			printf("%d\n",rd * t);
		else
		{
			int now,sum,ret;
			now  = ret = 0; 
			while(1)
			{
				sum = 0;
				while(1)
				{
					sum += a[now];
					if(sum>cap)
						break;
					now++;
					if(now==n) now = 0;
				}
				sum -= a[now];
				ret += sum;
				rd--;
				if(rd==0)
					break;
			}
			printf("%d\n",ret);
		}
	}
	return 0;
}