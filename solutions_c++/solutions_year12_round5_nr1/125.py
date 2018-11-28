#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
const int V=1200;
struct Node
{
	int id,p,l;
}q[V];
bool cmp(Node x,Node y)
{
	if(x.p*y.l!=y.p*x.l)
	return x.p*y.l>y.p*x.l;
	return x.id<y.id;
}
int i,n,_,ca;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&_);
	for(ca=1;ca<=_;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%d",&q[i].l);
		for(i=0;i<n;i++)
		scanf("%d",&q[i].p);
		for(i=0;i<n;i++)
		q[i].id=i;
		sort(q,q+n,cmp);
		printf("Case #%d:",ca);
		for(i=0;i<n;i++)
		printf(" %d",q[i].id);
		puts("");
	}
}
