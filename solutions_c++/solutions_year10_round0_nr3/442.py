#include<iostream>
using namespace std;
typedef __int64 llong;
int a[1003];
bool flag[1003];
llong val[1000002];
int d[1003];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,t,num,pos,zt,times,n,oo=1,l,r,mark;
	llong money,sum,ans;
	bool f;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",oo++);
		memset(flag,false,sizeof(flag));
		scanf("%d%d%d",&t,&num,&n);
		for(i=1;i<=n;i++)
			scanf("%d",&a[i]);
		times=0;
		money=0;
		pos=1;
		while(true)
		{
			if(flag[pos])break;
			times++;
			mark=pos;
			flag[pos]=true;
			d[pos]=times;
			sum=0;
			f=false;
			while(true)
			{
				if(sum+a[pos]>num)break;
				if(f && pos==mark)
					break;
				f=true;
				sum+=a[pos];
				pos++;
				if(pos>n)pos=1;
			}
			money+=sum;
			val[times]=money;
		}
		l=d[pos];
		r=times;
		if(t<=r)
		{
			printf("%I64d\n",val[t]);
			continue;
		}
		ans=val[r];
		t-=r;
		ans+=(t/(r-l+1))*(val[r]-val[l-1]);
		t%=(r-l+1);
		if(t)
		{
			ans+=val[l+t-1]-val[l-1];
		}
		printf("%I64d\n",ans);
	}
	return 0;
}