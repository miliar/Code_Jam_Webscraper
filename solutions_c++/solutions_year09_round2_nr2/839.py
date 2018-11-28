#include<iostream>

using namespace std;

int a[100],t,l;
char c;

inline int checker()
{
	for(int i=l-1;i;--i)
		if(a[i+1]>a[i])
			return i;
	return l;
}

int cmp(const void *a,const void *b)
{
	return *(int *)a-*(int *)b;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d\n",&t);
	a[0]=10;
	for(int k=1;k<=t;++k)
	{
		printf("Case #%d: ",k);
		l=0;
		for(;;)
		{
			scanf("%c",&c);
			if(c=='\n')
				break;
			a[++l]=c-'0';
		}
		int p=checker();
		if(p==l)
		{
			qsort(a+1,l,sizeof(int),cmp);
			int g;
			for(int i=1;i<=l;++i)
				if(a[i])
				{
					printf("%d",a[i]);
					g=i;
					break;
				}
			printf("0");
			for(int i=1;i<=l;++i)
				if(g!=i)
					printf("%d",a[i]);
		}
		else
		{
			int minx=a[p],g=0;
			qsort(a+p,l-p+1,sizeof(int),cmp);
			for(int i=1;i<p;++i)
				printf("%d",a[i]);
			for(int i=p;i<=l;++i)
				if(a[i]>minx&&a[g]>a[i])
					g=i;
			printf("%d",a[g]);
			for(int i=p;i<=l;++i)
				if(g!=i)
					printf("%d",a[i]);
		}
		puts("");
	}
	return 0;
}
