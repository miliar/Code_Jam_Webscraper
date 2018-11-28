#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
struct Node{double s,e,v;}q[3100];
bool cmp1(Node x,Node y)
{return x.s<y.s;}
bool cmp2(Node x,Node y)
{return x.v<y.v;}
int _,ca,i,n,qn;
double L,W,rs,rt,ans;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		scanf("%lf%lf%lf%lf%d",&L,&W,&rs,&rt,&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&q[i].s,&q[i].e,&q[i].v);
		}
		sort(q,q+n,cmp1);qn=n;
		for(i=1;i<n;i++)
		{
			q[qn].s=q[i-1].e;
			q[qn].e=q[i].s;
			q[qn++].v=0;
		}
		q[qn].s=0;q[qn].e=q[0].s;q[qn++].v=0;
		q[qn].s=q[n-1].e;q[qn].e=L;q[qn++].v=0;
		sort(q,q+qn,cmp2);
		ans=0.0;
	//	for(i=0;i<qn;i++)
	//	{
	//		printf("%d %lf %lf %lf\n",i,q[i].s,q[i].e,q[i].v);
	//	}puts("");
		for(i=0;i<qn;i++)
		{
			double tt;
			if(rt*(rs+q[i].v)>q[i].e-q[i].s)
			{
			//	puts("USE");
				tt=(q[i].e-q[i].s)/(rs+q[i].v);
				rt-=tt;
			}
			else
			{
				tt=rt+(q[i].e-q[i].s-rt*(rs+q[i].v))/(q[i].v+W);
				rt=0.0;
			}
		//	printf("%d %.2f\n",i,tt);
			ans+=tt;
		}
		printf("Case #%d: %.7f\n",ca,ans);
	}
}
