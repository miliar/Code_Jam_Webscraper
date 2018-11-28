#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
struct box
{
	int d,l,len;	
}a[10005];
int n,q[10005];
bool reach[10005];
int comp(const void *p,const void *q)
{
	return (*(struct box*)p).d - (*(struct box*)q).d;	
}
void SPFA(int u)
{
	memset(reach,false,sizeof(reach));
	for(int v=1;v<=n;v++)
		a[v].len = 0;
	reach[u] = true;
	int head,tail;
	q[0] = u; a[u].len = a[u].d;
	head = tail = 0;
	while(head <= tail)
	{
		u = q[head]; head++;
		for(int v=1;v<=n;v++)
		{
			if(abs(a[u].d-a[v].d) <= a[u].len)
				a[v].len >?= std::min(a[v].l,abs(a[u].d-a[v].d));
			if(!reach[v] && abs(a[u].d-a[v].d) <= a[u].len)
			{
				reach[v] = true;
				q[++tail] = v;	
			}	
		}
	}	
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int cn=0,t,i;
	scanf("%d",&t);
	while(t--)
	{cn++;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d%d",&a[i].d,&a[i].l);
		scanf("%d",&a[n+1].d);
		a[n+1].l = 0; n++;
	//	qsort(a+1,n,sizeof(a[0]),comp);
		a[1].len = a[1].d; SPFA(1);
		if(reach[n])
			printf("Case #%d: YES\n",cn);
		else 
			printf("Case #%d: NO\n",cn);
	}	
}
