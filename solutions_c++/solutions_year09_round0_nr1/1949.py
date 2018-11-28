#include<stdio.h>
char str[5005][17];
char a[500];
char b[17][30];
int tot[17];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int L,D,N,i,j,k,l,count,cs=1,n;
	while(scanf("%d %d %d",&L,&D,&N)==3)
	{
		for(i=0;i<D;i++)
		{
			scanf("%s",str[i]);
		}
		
		for(l=0;l<N;l++)
		{
			n=0;
			scanf("%s",a);
			for(i=0;a[i];i++)
			{
				if(a[i]=='(')
				{
					for(i++,k=0;a[i]!=')';i++)
						b[n][k++]=a[i];
					b[n][k]=0;
					tot[n]=k;
				}
				else
				{
					b[n][0]=a[i];
					b[n][1]=0;
					tot[n]=1;
				}
				n++;
			}
			count=0;
			for(i=0;i<D;i++)
			{
				for(j=0;j<L;j++)
				{
					for(k=0;k<tot[j];k++)
						if(str[i][j]==b[j][k])
							break;
					if(k==tot[j])
						break;
				}
				if(j==L)
					count++;
			}
			printf("Case #%d: %d\n",cs++,count);
		}
	}
	return 0;
}