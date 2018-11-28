#include <cstdio>
#include <algorithm>
using namespace std;

struct train
{
	int time,flag;
}a[200],b[200];

int cmp(train x,train y)
{
	return (x.time<y.time || x.time==y.time&&x.flag>y.flag);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int N,n,t,na,nb,i,j,k,h,m,max,tmp;
	scanf("%d",&N);
	for(n=1;n<=N;n++)
	{
		scanf("%d%d%d",&t,&na,&nb);
		for(i=j=k=0;i<na;i++,j++,k++)
		{
			scanf("%d:%d",&h,&m);
			a[j].time=h*60+m,a[j].flag=1;
			scanf("%d:%d",&h,&m);
			b[k].time=h*60+m+t,b[k].flag=2;
		}
		for(i=0;i<nb;i++,j++,k++)
		{
			scanf("%d:%d",&h,&m);
			b[k].time=h*60+m,b[k].flag=1;
			scanf("%d:%d",&h,&m);
			a[j].time=h*60+m+t,a[j].flag=2;
		}
		sort(a,a+na+nb,cmp);
		sort(b,b+na+nb,cmp);
		printf("Case #%d: ",n);
		max=tmp=0;
		for(i=0;i<na+nb;i++)
			if(a[i].flag==1)
			{
				tmp++;
				if(max<tmp)
					max=tmp;
			}
			else
				tmp--;
		printf("%d ",max);
		max=tmp=0;
		for(i=0;i<na+nb;i++)
			if(b[i].flag==1)
			{
				tmp++;
				if(max<tmp)
					max=tmp;
			}
			else
				tmp--;
		printf("%d\n",max);
	}
	return 0;
}