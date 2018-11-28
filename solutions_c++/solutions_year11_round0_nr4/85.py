#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
struct Node
{int va,id;}q[1200];
bool cmp(Node x,Node y)
{return x.va<y.va;}
int _,ca,i,n,a[1200],te;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&q[i].va);
			q[i].id=i;
		}
		sort(q,q+n,cmp);
		for(i=0;i<n;i++)
		a[q[i].id]=i;
		te=0;
		for(i=0;i<n;i++)
		if(a[i]!=i)te++;
		printf("Case #%d: %.9f\n",ca,double(te));
	}
}
