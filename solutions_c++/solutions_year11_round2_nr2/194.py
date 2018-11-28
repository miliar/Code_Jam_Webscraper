#include<stdio.h>
#include<string.h>
#include<algorithm>
#define MAX 1000000
using namespace std;
const double eps=1e-8;
struct data{
	int p,v;
}x[MAX];
bool cmp(const data &a,const data &b){
	return a.p<b.p;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.txt","w",stdout);
	int cs,i,j,c,d,cnt;
	double l,r,md,now;
	scanf("%d",&cs);
	for(int dd=1;dd<=cs;dd++)
	{
		scanf("%d%d",&c,&d);
		for(i=0;i<c;i++)
			scanf("%d%d",&x[i].p,&x[i].v);
		sort(x,x+c,cmp);
		l=0;
		r=1e13;
		cnt = 0;
		while(fabs(r-l)>eps&&cnt<100000)
		{
			cnt++;
			md=(l+r)*0.5;
			for(now=-1e12,i=0;i<c;i++)
			{
				now=max(now,x[i].p-md);
				now+=(double)d*(x[i].v-1);
				if(now>x[i].p+md)
					break;
				now+=d;
			}
			if(i==c)
				r=md;
			else
				l=md;
		}
		printf("Case #%d: %.7f\n",dd,l);
	}
}
