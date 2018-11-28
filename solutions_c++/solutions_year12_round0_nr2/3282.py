#include<cstdio>

int nots(int sum)
{
	int max=-1;
	if (sum%3==0) max=sum/3;
	if (((sum+1)%3==0) && ((sum+1)/3>0)) max=(sum+1)/3;
	if (((sum+2)%3==0) && ((sum+2)/3>0)) max=(sum+2)/3;
	return max;
}

int surp(int sum)
{
	int max=-1;
	if ((sum+2)%3==0) max=(sum+2)/3;
	if (sum%3==0) max=sum/3+1;
	if ((sum+4)%3==0) max=(sum+4)/3;
	if (max<2) return -1;
	return max;
}

int mx(int a,int b)
{if (a>b) return a;return b;
}

int main()
{
	int n,s,p,sum,t,i,j,tt,nr[150];
	
	freopen("r.in","r",stdin);
	freopen("w.out","w",stdout);
	scanf("%d",&t);
	for (tt=1;tt<=t;++tt)
	{
		scanf("%d %d %d",&n,&s,&p);
		for (i=0;i<=s;++i) nr[i]=0;
		for (i=1;i<=n;++i) 
		{
			scanf("%d",&sum);
			int countns=0,counts=0;
			if (nots(sum)>=p) countns=1;
			if (surp(sum)>=p) counts=1;
			for (j=s;j>0;--j)
				nr[j]=mx(nr[j-1]+counts,nr[j]+countns);
			if (countns) ++nr[0];
		}
		printf("Case #%d: %d\n",tt,nr[s]);
	}
return 0;
}
			