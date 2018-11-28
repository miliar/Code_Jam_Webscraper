#include <iostream>
#include <algorithm>
using namespace std;

typedef __int64 LL;

int a[1010];
int L,N,C;
LL t;

struct PN
{
	int id;
	int val;
}q[1000010];
bool flag[1000010];
int qn;

bool cmp(const PN &u,const PN &v)
{
	return u.val>v.val;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%d%I64d%d%d",&L,&t,&N,&C);
		int i;
		for(i=1;i<=C;++i) scanf("%d",&a[i]);
		LL sum=0;
		for(i=1;i<=N;++i)
		{

			if(sum<t/2)
				sum = sum + a[(i-1)%C+1];
			else
				break;
		}
		qn=0;
		int p=i-1;
		q[qn].id=i-1;
		q[qn].val=sum-t/2;
		qn++;
		for(;i<=N;++i)
		{
			q[qn].id=i;
			q[qn].val=a[(i-1)%C+1];
			qn++;
		}
		LL ans=0;
		sort(q,q+qn,cmp);
		for(i=1;i<=N;++i) flag[i]=false;
		for(i=0;i<qn&&i<L;++i)
		{
			flag[q[i].id]=true;
			ans = ans+q[i].val;
			if(q[i].id==p) ans= ans+2*(a[(p-1)%C+1]-(sum-t/2));
		}
		for(i=1;i<=N;++i)
		{
			if(!flag[i]) ans = ans + a[(i-1)%C+1]*2;
		}
		printf("Case #%d: %I64d\n",cas,ans);
	}

	return 0;
}