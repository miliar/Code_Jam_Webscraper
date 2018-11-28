#include<cstdio>
#include<cstring>
const int mn=5500;
int T,k,n,a[mn];
bool f[mn];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%d",&k,&n);
		memset(f,0,sizeof(f));
		for(int i=1,p=1,c;i<=k;i++)
		{
			c=0;
			while(c<i)
			{
				if(!f[p])
				{
					c++;
					if(c==i)a[p]=i,f[p]=1;
				}
				p++;
				if(p>k)p=1;
			}
		}
		printf("Case #%d:",tn);
		for(int i=1,t;i<=n;i++)
		{
			scanf("%d",&t);
			printf(" %d",a[t]);
		}
		putchar('\n');
	}
	return 0;
}
