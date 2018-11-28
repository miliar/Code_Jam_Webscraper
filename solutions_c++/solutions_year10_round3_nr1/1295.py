#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int t,n;
struct A
{
	int l;
	int r;
};

A a[1003];
int cmp(const void*a,const void*b)
{
	struct A*c=(A*)a;
	struct A*d=(A*)b;
	return c->l>d->l?1:-1;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&t);
	int i,j,k;
	for(k=1;k<=t;++k)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%d%d",&a[i].l,&a[i].r);
		qsort(a,n,sizeof(a[0]),cmp);
		
		int cnt=0;
		for(i=0;i<n;++i)
			for(j=i+1;j<n;++j)
				if(a[j].r<a[i].r) cnt++;
		printf("Case #%d: %d\n",k,cnt);

	}
	return 1;

}