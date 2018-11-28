#include "stdio.h"
#include "stdlib.h"

typedef struct T
{
	int st,et,to;
}T;

T a[1000];

int cmp(const void *a,const void *b)
{
	T *c=(T *)a;
	T *d=(T *)b;
	if(c->st!=d->st)
	{
		return c->st-d->st;
	}
	if(c->et!=d->et)
	{
		return c->et-d->et;
	}
	return c->to-d->to;
}

int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t1,t2,ca,v,i,t,n,s[2],j,h1,h2,m1,m2;
	scanf("%d",&ca);
	for(v=1;v<=ca;v++)
	{
		scanf("%d",&t);
		scanf("%d%d",&t1,&t2);
		for(i=0,n=0;i<t1;i++,n++)
		{
			scanf("%d:%d",&h1,&m1);
			scanf("%d:%d",&h2,&m2);
			a[n].st=h1*60+m1;
			a[n].et=h2*60+m2;
			a[n].to=0;
		}
		for(i=0;i<t2;i++,n++)
		{
			scanf("%d:%d",&h1,&m1);
			scanf("%d:%d",&h2,&m2);
			a[n].st=h1*60+m1;
			a[n].et=h2*60+m2;
			a[n].to=1;
		}
		qsort(a,n,sizeof(a[0]),cmp);
		bool ex[1000]={0};
		s[1]=s[0]=0;
		for(i=0;i<n;i++)
		{
			for(j=i-1;j>=0;j--)
			{
				if(!ex[j])
				{
					if(a[i].to!=a[j].to)
					{
						if(a[j].et+t<=a[i].st)
						{
							ex[j]=true;
							break;
						}
					}
				}
			}
			if(j>=0)
			{
				;
			}
			else
			{
				s[a[i].to]++;
			}
		}
		printf("Case #%d: %d %d\n",v,s[0],s[1]);
	}
	return 0;
}