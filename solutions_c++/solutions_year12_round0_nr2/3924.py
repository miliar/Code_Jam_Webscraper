#include <stdio.h>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int k,nk;
	scanf("%d",&nk);
	int n,s,p,tmp,i,cnt;
	for(k=1;k<=nk;k++)
	{
		cnt = 0;
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&tmp);
			if(p>10)
			{
				continue;
			}
			else if(tmp >= 3*p)
				cnt++;
			else if(tmp >= 3*p-2 && p-1>=0)
				cnt++;
			else if(tmp >= 3*p -4 && s>0 && p-2>=0)
			{
				s--;
				cnt++;
			}
		}
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}