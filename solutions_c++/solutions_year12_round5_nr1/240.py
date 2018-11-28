#include <cstdio>
#include <cstdlib>
struct box
{
	int num,p;	
}lv[1000];
int comp(const void *p,const void *q)
{
	if((*(struct box*)q).p - (*(struct box*)p).p != 0)
	return (*(struct box*)q).p - (*(struct box*)p).p;
	return (*(struct box*)p).num - (*(struct box*)q).num;	
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,n,cn,T,a;
	scanf("%d",&T);
	for(cn=1;cn<=T;cn++)
	{
		printf("Case #%d: ",cn);
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d",&a);
		for(i=1;i<=n;i++)
		{
			lv[i].num = i-1;
			scanf("%d",&lv[i].p);
		}
		qsort(lv+1,n,sizeof(struct box),comp);
		for(i=1;i<=n;i++)
			printf("%d ",lv[i].num);
		printf("\n");	
	}	
}
