#include<stdio.h>
#include<memory>
const int N=1000000+32;
int r[N];
int get(int x)
{
	int t=x,y;
	while(t!=r[t])
		t=r[t];
	while(x!=t)
	{
		y=r[x];
		r[x]=t;
		x=y;
	}
	return t;
}
bool u[N];
int pr[N],g;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,c,o,t,s,ans;
	__int64 a,b,p,x;
	memset(u,0,sizeof(u));
	g=0;
	for(i=2;i<N;i++)
		if(!u[i])
		{
			pr[g++]=i;
			for(j=i+i;j<N;j+=i)
				u[j]=true;
		}
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%I64d%I64d%I64d",&a,&b,&p);
		for(i=0;i<=b-a;i++)
			r[i]=i;
		for(i=0;i<g;i++)
			if(pr[i]>=p)
				break;
		for(;i<g;i++)
		{
			p=pr[i];
			t=-1;
			for(x=((a-1)/p+1)*p;x<=b;x+=p)
			{
				s=get(x-a);
				if(t==-1)
					t=s;
				else
					r[s]=t;
			}
		}
		ans=0;
		for(i=0;i<=b-a;i++)
			if(get(i)==i)
				ans++;
		printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}
