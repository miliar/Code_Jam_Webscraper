#include<stdio.h>
#include<algorithm>
using namespace std;

struct node
{
	double B,E,w;
} A[1001];

int T,N;
double l1,t1,left,ans,tot,b,X,S,R,t;

bool cmp(node A,node B)
{
	return A.w<B.w;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.in.txt","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
		l1=0;
		left=t;
		ans=0.0;
		b=0.0;
		for (int i=0;i<N;i++)
		{
			scanf("%lf%lf%lf",&A[i].B,&A[i].E,&A[i].w);
			l1+=A[i].E-A[i].B;
		}
		if (X-l1<=left*R)
		{
			left-=(X-l1)/R;
			ans+=(X-l1)/R;
		}
		else
		{
			ans+=left+(X-left*R-l1)/S;
			left=0;
		}
		sort(A,A+N,cmp);
		for (int i=0;i<N;i++)
		{
			if (A[i].E-A[i].B<=left*(A[i].w+R))
			{
				left-=(A[i].E-A[i].B)/(A[i].w+R);
				ans+=(A[i].E-A[i].B)/(A[i].w+R);
			}
			else
			{
				ans+=left+(A[i].E-A[i].B-left*(A[i].w+R))/(A[i].w+S);
				left=0;
			}
		}
		
		printf("Case #%d: %.8f\n",cas,ans);

	}
	//while(1);
}