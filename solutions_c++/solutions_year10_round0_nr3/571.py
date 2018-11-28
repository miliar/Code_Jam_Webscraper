#include<cstdio>

const int mx=1010;
__int64 r,k,n,g[2*mx],sum[2*mx];
int next[mx];
bool us[mx];

int cal(int p)
{
	int i;
	__int64 sum=0;
	for(i=p;i<p+n;i++)
	{
		sum+=g[i];
		if(sum>k)break;
		//printf("sum=%I64d,g[i]=%I64d\n",sum,g[i]);
	}
	//printf("p=%d,i=%d\n",p,i);
	return (int)(i%n);
}

__int64 cal2(int a,int b)
{
	__int64 ans;
	if(a==b) ans= sum[n-1];
	else if(a>b)
	{
		ans= sum[b+n-1]-(a?sum[a-1]:0);
	}
	else
	{
		ans= sum[b-1]-(a?sum[a-1]:0);
	}
	//printf("cal2(%d,%d)=%I64d\n",a,b,ans);
	return ans;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("coutput2.txt","w",stdout);
	int t,ca=1,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%I64d",&g[i]);
		for(i=0;i<n;i++)next[i]=-1;
		for(i=0;i<n;i++)g[n+i]=g[i];
		sum[0]=g[0];
		for(i=1;i<2*n;i++)
			sum[i]=sum[i-1]+g[i];
		/*
		printf("sum[0]=%I64d,",sum[0]);
		for(i=1;i<2*n;i++)
			printf("sum[%d]=%I64d,",i,sum[i]);printf("\n");
*/
		int s=0,p;
		while(1)
		{
			p=next[s]=cal(s);
			if(next[p]!=-1)
				break;
			s=next[s];
		}//printf("o1\n");
		/*
		for(i=0;i<n;i++)
		{
			printf("%d ",next[i]);
		}printf("\n");
*/
		int len1=0,len2=0;
		s=0;
		while(1)
		{
			if(p==s)break;
			else {len1++;s=next[s];}
		}
		len2++;s=next[p];
		while(1)
		{
			if(p==s)break;
			else {len2++;s=next[s];}
		}
		//printf("len1=%d,len2=%d\n",len1,len2);
		__int64 ans=0;
		if(r<=len1)
		{
			int s=0;
			for(i=0;i<k;i++)
			{
				ans+=cal2(s,next[s]);
				s=next[s];
			}
			//printf("cal2(0,0)=%I64d\n",cal2(0,0));
		}
		else
		{
			int s=0;
			for(i=0;i<len1;i++)
			{
				ans+=cal2(s,next[s]);
				s=next[s];
			}
			__int64 kk=r-len1;
			__int64 mod=kk%len2,div=kk/len2;//if(mod==0)mod=len2;
			//printf("mod=%I64d,div=%I64d,len2=%d\n",mod,div,len2);
			s=p;
			for(i=0;i<len2;i++)
			{
				if(i>=mod)
					ans+=div*cal2(s,next[s]);
				else
					ans+=(div+1)*cal2(s,next[s]);
				s=next[s];
			}
		}
		printf("Case #%d: %I64d\n",ca++,ans);
	}

	return 0;
}
