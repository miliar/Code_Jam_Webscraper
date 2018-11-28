#include<iostream>
int main()
{
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int css,cs,a,d[100],ct,tp,k,i,j,n;
	char s[100];
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			for(j=n-1;j>=0;j--)
				if(s[j]=='1')break;
			d[i]=j;
		}
		ct=0;i=0;
		for(;i<n;i++)
			if(d[i]>i)
			{
				for(j=i+1;;j++)
					if(d[j]<=i)break;
				for(k=j;k>i;k--)
					d[k]=d[k-1];
				ct+=j-i;
			}
		printf("Case #%d: %d\n",css,ct);
	}
	return 0;
}
