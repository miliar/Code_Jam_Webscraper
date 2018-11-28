#include<iostream>
using namespace std;
struct person
{
	int l,r,s;
}wal[1024];
int times,len,sp,r,ti,n;
inline bool cmp2(const person &a,const person &b)
{
	return (a.l<b.l);
}
inline bool cmp(const person &a,const person &b)
{
	return (a.s<b.s);
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d%d%d%d%d",&len,&sp,&r,&ti,&n);
		for (int a=1;a<=n;++a)
		{
			scanf("%d%d%d",&wal[a].l,&wal[a].r,&wal[a].s);
			//wal[a].p=a;
		}
		sort(wal+1,wal+1+n,cmp2);
		int now=0,all=n;;
		for (int a=1;a<=n;++a)
		{
			if (wal[a].l!=now)
			{
				++all;
				wal[all].l=now;
				wal[all].r=wal[a].l;
				wal[all].s=0;
			}
			now=wal[a].r;
		}
		if (now!=len)
		{
			++all;
			wal[all].l=now;
			wal[all].r=len;
			wal[all].s=0;
		}
		sort(wal+1,wal+1+all,cmp);
		double res=ti,ans=0,ll;
		for (int a=1;a<=all;++a)
		{
		//	printf("[%d]",wal[a].s);
			ll=wal[a].r-wal[a].l;
			if(ll/(r+wal[a].s)<=res)
			{
				res-=ll/(r+wal[a].s);
				ans+=ll/(r+wal[a].s);
			}else
			{
				ll-=(r+wal[a].s)*res;
				ans+=res;
				res=0;
				////////
				ans+=ll/(wal[a].s+sp);
			}
		}
		printf("Case #%d: %.10lf\n",z,ans);
	}	
}
