#include<cstdio>
#include<memory>
int h,t,n,m,i,j,k,r,f[1024],g[1024],o;
char a[13][13];
int ok(int x,int y)
{
	int z;
	for(z=0;z<m;z++)
		if((1<<z)&y)
		{
			if(a[i][z]!='.')return 0;
			if(z&&(1<<(z-1))&y)return 0;
			if(z&&(1<<(z-1))&x)return 0;
			if(z<m-1&&(1<<(z+1))&y)return 0;
			if(z<m-1&&(1<<(z+1))&x)return 0;
		}
	return 1;
}
int s(int x)
{
	int p;
	p=0;
	while(x)
	{
		p+=x%2;x/=2;
	}
	return p;
}
int main()
{
	freopen("c.in.txt","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for(h=0;h++<t;)
	{
		scanf("%d%d\n",&n,&m);
		for(i=0;i<n;i++)gets(a[i]);
		memset(f,-1,sizeof(f));
		f[0]=0;
		for(i=0;i<n;i++)
		{
			memset(g,-1,sizeof(g));
			for(j=0;j<1<<m;j++)
				if(f[j]>=0)
					for(k=0;k<1<<m;k++)
						if(ok(j,k))
						{
							r=f[j]+s(k);
							if(r>g[k])g[k]=r;
						}
			memcpy(f,g,sizeof(f));
		}
		o=0;
		for(i=0;i<1<<m;i++)
			if(f[i]>o)o=f[i];
		printf("Case #%d: %d\n",h,o);
	}
	return 0;
}