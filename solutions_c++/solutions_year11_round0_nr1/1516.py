#include<cstdio>

int main()
{
	freopen("D:\\data\\A-small-attempt0.in","r",stdin);
	freopen("D:\\data\\A-small-attempt0.out","w",stdout);
	int t=0,tt;
	scanf("%d",&tt);
	while(tt--)
	{
		int n,m=0,i,j,k,x=0,y=0,a[105]={0},b[105]={0},s[105]={0};
		char c[105];
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&c[i],&s[i]);
			if(c[i]=='O')
			{
				a[x++]=s[i];
			}
			else
			{
				b[y++]=s[i];
			}
		}
		x=y=i=0;
		j=k=1;
		while(i<n)
		{
			if(c[i]=='O')
			{
				if(j==s[i])
				{
					i++;
					x++;
				}
				else
				{
					if(s[i]>j)
						j++;
					else
						j--;
				}
				if(b[y]>k)
					k++;
				else if(b[y]<k)
					k--;
			}
			else
			{
				if(k==s[i])
				{
					i++;
					y++;
				}
				else
				{
					if(s[i]>k)
						k++;
					else
						k--;
				}
				if(a[x]>j)
					j++;
				else if(a[x]<j)
					j--;
			}
			m++;
		}
		printf("Case #%d: %d\n",++t,m);
	}
}
