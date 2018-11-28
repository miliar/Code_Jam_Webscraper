#include<cstdio>
#include<algorithm>
const int mn=105;
struct pt
{
	int t,s;
	bool f;
}a[mn*4];

int T,t,na,nb;
bool cmp(const pt&a,const pt& b)
{
	if(a.t!=b.t)return a.t<b.t;
	return !a.f;
}
int main()
{
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%d%d",&t,&na,&nb);
		int t1,t2,t3,t4;
		for(int i=0;i<na;i++)
		{
			scanf("%d:%d %d:%d",&t1,&t2,&t3,&t4);
			t1=t1*60+t2,t2=t3*60+t4;
			a[i*2].t=t1, a[i*2].s=0, a[i*2].f=1;
			a[i*2+1].t=t2+t, a[i*2+1].s=0, a[i*2+1].f=0;
		}
		for(int i=na;i<na+nb;i++)
		{
			scanf("%d:%d %d:%d",&t1,&t2,&t3,&t4);
			t1=t1*60+t2,t2=t3*60+t4;
			a[i*2].t=t1, a[i*2].s=1, a[i*2].f=1;
			a[i*2+1].t=t2+t, a[i*2+1].s=1, a[i*2+1].f=0;
		}
		std::sort(a,a+2*(na+nb),cmp);
		int num[2]={},ans[2]={};
		for(int i=0;i<2*(na+nb);i++)
		{
			if(a[i].f)
				if(num[a[i].s]>0)num[a[i].s]--;
				else ans[a[i].s]++;
			else
				num[1-a[i].s]++;
		}
		printf("Case #%d: %d %d\n",tn,ans[0],ans[1]);
	}
	return 0;
}
