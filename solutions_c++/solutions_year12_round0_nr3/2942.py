#include<stdio.h>
#include<string.h>
int t,tmp,k;
int check(int x,int y)
{
	int i,j,a[20],b[20];
	for(i=0;i<k;i++)
	{
		a[i]=x%10;
		x/=10;
		b[i]=y%10;
		y/=10;
	}
	for(i=0;i<k;i++)
	{
		int tt=i;
		for(j=0;j<k;j++,tt++)
		{
			if(tt==k)tt=0;
			if(a[j]!=b[tt])break;
		}
		if(j==k)return 1;
	}
	return 0;
}
main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,abc,i,j,a,b,lena,lenb,ans;
	scanf("%d",&T);
	for(abc=1;abc<=T;abc++)
	{
		ans=0;
		scanf("%d %d",&a,&b);
		t=10,tmp=a,k=1;
		while(tmp/=10)
		{
			k++;
			t*=10;
		}
		for(i=a;i<=b;i++)
			for(j=i+1;j<=b;j++)
				if(check(i,j))
				{
					//printf("%d %d\n",i,j);
					ans++;
				}
		printf("Case #%d: %d\n",abc,ans);
		/*for(i=a;i<=b;i++)
		{
			int p=10;
			for(j=0;j<k-1;j++)
			{
				tmp=i%p;
				if(tmp==0)
				{
					p*=10;
					continue;
				}
				else
				{
					p=10;
				}
			}
		}*/
	}
}
