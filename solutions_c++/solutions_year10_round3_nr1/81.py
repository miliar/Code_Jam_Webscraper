#include<iostream>
#include<algorithm>
using namespace std;

struct node
{
	double a,b;
}p[1030];

bool cmp(node p1,node p2)
{
	if(p1.a==p2.a)return p1.b<p2.b;
	else return p1.a<p2.a;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,i,j,num,mm=1;
	scanf("%d",&t);
	while(t--)
	{
		num=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf",&p[i].a,&p[i].b);
		}
		sort(p,p+n,cmp);
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(p[j].a>p[i].a && p[j].b<p[i].b)num++;
			}
		}
		printf("Case #%d: %d\n",mm++,num);
	}
	return 0;
}