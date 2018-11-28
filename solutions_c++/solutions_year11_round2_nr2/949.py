#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

int t,c,d,p[1000][2];
double ans,mid,l,r,temp;
int i,j,sum;


int cmp(const void *a,const void *b)
{
	return *(int *)a-*(int *)b;
}

bool test()
{
	int i;
	for (i=0;i<c;i++)
	{
		if (p[i][0]-mid>=temp+d)
		{
			if (p[i][0]-mid+d*(p[i][1]-1)-p[i][0]>mid)return false;
			temp=p[i][0]-mid+d*(p[i][1]-1);
		}
		else 
		{
			if (temp+d*p[i][1]-p[i][0]>mid)return false;
			temp=temp+d*p[i][1];
		}
	}
	if (temp-p[c-1][0]<mid)return true;else return false;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		sum=0;
		scanf("%d%d",&c,&d);
		for (i=0;i<c;i++){scanf("%d%d",&p[i][0],&p[i][1]);sum+=p[i][1];}
		qsort(p,c,sizeof(p[0]),cmp);

		l=0;r=d*sum;
		while(r-l>0.000001)
		{
			mid=(l+r)/2;
			temp=p[0][0]-mid-d;
			if (test())r=mid;else l=mid;
		}

		printf("Case #%d: %.1f\n",id,r);
	}

	return 0;
}