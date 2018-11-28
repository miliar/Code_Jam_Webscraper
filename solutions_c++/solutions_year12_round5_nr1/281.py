#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int T;
int n;
struct mission
{
	int l,p,num;
}m[1009];

void init()
{
	scanf("%d",&n);
	for (int i=0;i<n;i++)
	{
		scanf("%d",&m[i].l);
		m[i].num=i;
	}
	for (int i=0;i<n;i++)
		scanf("%d",&m[i].p);
}

bool cmp(const struct mission &x,const struct mission &y)
{
	/*
	if (x.p>y.p) return true;
	if (x.p<y.p) return false;
	if (x.p!=0)
	{
		if (x.l<y.l) return false;
		if (x.l>y.l) return false;
	}
	*/
	int s=(x.l*x.p-y.l*y.p);
	if (s>0) return true;
	if (s<0) return false;
	if (x.p>y.p) return true;
	if (x.p<y.p) return false;
	return x.num<y.num;

}

void work()
{
	sort(m,m+n,cmp);
	for (int i=0;i<n;i++)
		printf(" %d",m[i].num);
	printf("\n");
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		printf("Case #%d:",t);
		work();
	}
	return 0;
}