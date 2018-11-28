#include <stdio.h>

int t,r,k,n,g[1000];
int i,j,temp,answer,top,num;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		printf("Case #%d: ",id);
		scanf("%d%d%d",&r,&k,&n);
		for (i=0;i<n;i++)
			scanf("%d",&g[i]);
		top=0;
		answer=0;
		while (r--)
		{
			temp=0;
			num=0;
			while (temp+g[top]<=k && num<n)
			{
				num++;
				temp+=g[top];
				top=(top+1)%n;
			}
			answer+=temp;
		}
		printf("%d\n",answer);
	}
	return 0;
}