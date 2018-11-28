#include<cstdio>
#include<memory>

int l,i,j,k,p,n,m;
char a[5005][16],b[999],d[5005],e[128];

int main()
{
	freopen("d:\\a.in","r",stdin);
	freopen("d:\\a.out","w",stdout);
	scanf("%d%d%d",&l,&n,&m);
	for(i=0;i<n;i++)
		scanf(" %s",a[i]);
	for(i=1;i<=m;i++)
	{
		scanf(" %s",b);
		memset(d,1,n);
		k=0;
		for(j=0;j<l;j++)
		{
			memset(e,0,128);
			if(b[k]=='(')for(k++;b[k]!=')';k++)e[b[k]]=1;
			e[b[k++]]=1;
			for(p=0;p<n;p++)
				d[p]&=e[a[p][j]];
		}
		k=0;
		for(j=0;j<n;j++)k+=d[j];
		printf("Case #%d: %d\n",i,k);
	}
	return 0;
}