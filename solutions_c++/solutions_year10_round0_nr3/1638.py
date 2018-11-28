#include<iostream>
#include<queue>
using namespace std;

#define MAXN 1001

long long n,T,r,k,cy;
long long 
a[MAXN],//size of Gi
b[MAXN],//amount starting from Gi
seq[MAXN],
next[MAXN],
ans,
ans1,
ans2,
tot,
len,
st,
ed;
//queue<long long> q;

void CalcAns()
{
	ans=0;
	long long c1,len0=0,now=0;
	while(1)
	{
		if(now==st)
		{
			break;
		}
		else
		{
			len0++;
			now=next[now];
		}
	}
	//进入循环前就结束了
	if(r<=len0)
	{
		c1=r;
		now=0;
		for(long long i=0;i<c1;++i)
		{
			ans+=b[now];
			now=next[now];
			return;
		}
	}
	//有进入循环节
	else
	{
		//计算进入循环前的部分
		c1=len0;
		now=0;
		for(long long i=0;i<c1;++i)
		{
			ans+=b[now];
			now=next[now];
		}
		
		//减去进入循环前的部分
		r-=len0;

		//循环次数
		long long ts=r/len;

		//余下的部分
		long long rem=r%len;
		
		//计算进入循环节部分
		ans1=ans2=0;
		c1=len;
		now=st;
		for(long long i=0;i<c1;++i)
		{
			ans1+=b[now];
			if(rem!=0&&rem==i+1)
			{
				ans2=ans1;
			}
			now=next[now];
		}

		ans+=(ans1*ts+ans2);
	}
}

int main()
{
	freopen("Cl.in","r",stdin);
	freopen("Cl.out","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;++ca)
	{
		tot=0;
		scanf("%d%d%d",&r,&k,&n);
		for(long long i=0;i<n;++i)
		{
			scanf("%lld",&a[i]);
			tot+=a[i];
		}
		if(tot<=k)
		{
			ans=tot*r;
			goto ou;
		}
		
		memset(b,0,sizeof(b));
		memset(seq,0,sizeof(seq));
		memset(next,0,sizeof(next));
		cy=0;
		long long now=0,j;
		while(1)
		{
			j=now;
			while(b[now]+a[j]<=k)
			{
				b[now]+=a[j];
				j=(j+1)%n;
			}
			seq[now]=cy;
			cy++;
			next[now]=j;
			if(b[j])
			{
				st=j;
				ed=now;
				len=seq[now]-seq[j]+1;
				break;
			}
			now=j;
		}
		
		CalcAns();

		/*
		while(!q.empty())
		{
			q.pop();
		}
		for(long long i=0;i<n;++i)
		{
			q.push(a[i]);
		}
		ans=0;
		for(long long i=0;i<r;++i)
		{
			long long tmp=0;
			while(tmp+q.front()<=k)
			{
				tmp+=q.front();
				long long t2=q.front();
				q.pop();
				q.push(t2);
			}
			ans+=tmp;
		}
		*/
ou:		printf("Case #%d: %lld\n",ca,ans);
	}
	return 0;
}
