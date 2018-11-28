#include<cstdio>
int main()
{
	int t,n,i,j,k,a[20],s1,s2,fl,sum,ans,s,ca=0,st1,st2;
	scanf("%d",&t);
	while(t--)
	{
		ca++;
		s = 0;
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			s = s+a[i];
		}
		k = 1<<n;
		fl = 0;
		ans = 0;
		for (i=0;i<k;i++)
		{
			s1 = 0;
			s2 = 0;
			sum = 0;
			st1 = 0;
			st2 = 0;
			for (j=0;j<n;j++)
			{
				if (i&(1<<j))
				{
					s1 = s1^a[j];
					sum = sum + a[j];
					st1 = 1;
				}
				else
				{
					st2 = 1;
					s2 = s2^a[j];
				}
			}
			if (s1==s2 && st1==1 && st2==1)
			{
				fl = 1;
	//			printf("s1 = %d sum = %d\n",s1,sum);
				j = (sum > (s-sum))?sum:(s-sum);
				if (ans < j)
					ans = j;
			}
		}
		if (fl==0)
			printf("Case #%d: NO\n",ca);
		else
			printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
