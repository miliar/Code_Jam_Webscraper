#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int T,l,t,n,c,a[1000010];
int i,start,sum;

int cmp(const void *a,const void *b)
{return *(int *)b-*(int *)a;}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);freopen("b.out","w",stdout);
	scanf("%d",&T);
	for (int id=1;id<=T;id++)
	{
		scanf("%d%d%d%d",&l,&t,&n,&c);
		sum=t;
		for (i=0;i<c;i++)
		{
			scanf("%d",&a[i]);
		}
		for (;i<n;i++)a[i]=a[i%c];
		for (i=0;i<n;i++)
			if (t>a[i]*2) {t-=a[i]*2;a[i]=0;}
			else {a[i]-=t/2;t=0;break;}
		qsort(a,n,sizeof(a[0]),cmp);
		for (i=0;i<l;i++)
		{
			sum+=a[i];
		}
		for (;i<n;i++)sum+=a[i]*2;

		printf("Case #%d: %d\n",id,sum);
	}
	return 0;
}