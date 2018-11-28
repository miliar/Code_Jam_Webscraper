#include<stdio.h>
int main()
{
	int t, n, s, p, sc;
	scanf("%d",&t);
	
	for(int tc=1; tc<=t; tc++)
	{
		scanf("%d%d%d",&n,&s,&p);
		int cnt=0, num;
		sc=0;
		for(int i=0; i<n; i++)
		{
			scanf("%d",&num);
			if(num>=(3*p-4)&&num<=(3*p-3)&&sc<s&&num>=2)
			{
				sc++;
				cnt++;
			}
			else if(num>=(3*p-2))
			{
				cnt++;
			}
		}
		if(s>n)
		printf("Case #%d: 0\n",tc);
		else
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}
