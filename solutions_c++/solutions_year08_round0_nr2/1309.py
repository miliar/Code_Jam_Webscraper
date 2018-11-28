#include<stdio.h>
#include<algorithm>
using namespace std;

int n,m;

int aBegin[101],bBegin[101],aEnd[101],bEnd[101];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T,T1,time;
	int i,j;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d%d",&time,&n,&m);
		for(i=1;i<=n;i++)
		{
			int hh,mm;
			scanf("%d:%d",&hh,&mm);
			aBegin[i]=hh*60+mm;
			scanf("%d:%d",&hh,&mm);
			aEnd[i]=hh*60+mm;
		}

		for(i=1;i<=m;i++)
		{
			int hh,mm;
			scanf("%d:%d",&hh,&mm);
			bBegin[i]=hh*60+mm;
			scanf("%d:%d",&hh,&mm);
			bEnd[i]=hh*60+mm;
		}

		sort(aBegin+1,aBegin+1+n);
		sort(bEnd+1,bEnd+1+m);

		int ansA=n;
		i=n,j=m;
		for(;i>=1 && j>=1;)
		{
			if(aBegin[i]>=bEnd[j]+time)
			{
				ansA--;
				i--;
				j--;
			}
			else
			{
				j--;
			}
		}

		sort(bBegin+1,bBegin+1+m);
		sort(aEnd+1,aEnd+1+n);

		int ansB=m;
		i=m,j=n;
		for(;i>=1 && j>=1;)
		{
			if(bBegin[i]>=aEnd[j]+time)
			{
				ansB--;
				i--;
				j--;
			}
			else
			{
				j--;
			}
		}


		printf("Case #%d: %d %d\n",T1,ansA,ansB);
	}
	return 0;
}