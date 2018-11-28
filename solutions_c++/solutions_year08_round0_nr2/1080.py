#include <stdio.h>
#include <stdlib.h>

struct Time
{
	int h,min;
};
struct trainTime
{
	Time start;
	Time arrive;
};
Time add(Time a,int min)
{
	Time b=a;
	b.h=b.h+(b.min+min)/60;
	b.min=(b.min+min)%60;
	return b;
}
int timeCmp(Time a,Time b)
{
	if(a.h>b.h)
		return 1;
	else if(a.h==b.h&&a.min>b.min)
		return 1;
	else 
		return 0;
}
int cmp(const void *a,const void *b)
{
	trainTime *c=(trainTime *)a;
	trainTime *d=(trainTime *)b;
	return timeCmp(c->start,d->start);
}
int find(trainTime a,trainTime *b,int nB,int t,int *vA)
{
	int i;
	a.arrive=add(a.arrive,t);
	for(i=0;i<nB;i++)
		if(vA[i]==0&&timeCmp(a.arrive,b[i].start)==0)
			break;
	if(i==nB)
		return -1;
	else 
		return i;
}
int fcount(int *aP,int *bP,int nA,int nB)
{
	int vA[110]={0};
	int vB[110]={0};
	int count=nA;
	for(int i=0;i<nA;i++)
		if(aP[i]>=0)
			vB[aP[i]]=1;
	int v[110]={0};
	for(int i=0;i<nB;i++)
	{
		int n=1;
		int p=i;
		if(v[p]==0)
		{
			v[p]=1;
			while(p!=-1)
			{
				if(n%2==1)
					p=bP[p];
				else
				{
					p=aP[p];
					v[p]=1;
					count--;
				}
				n++;
			}
		}
	}
	return count;
}
int main()
{
	int aCase,t,nA,nB;
	int aP[110],bP[110];
	int aCount,bCount;
	trainTime aTime[110],bTime[110];
	scanf("%d",&aCase);
	for(int k=1;k<=aCase;k++)
	{
		scanf("%d%d%d",&t,&nA,&nB);
		for(int i=0;i<nA;i++)
			scanf("%d:%d %d:%d",&aTime[i].start.h,&aTime[i].start.min,&aTime[i].arrive.h,&aTime[i].arrive.min);
		for(int i=0;i<nB;i++)
			scanf("%d:%d %d:%d",&bTime[i].start.h,&bTime[i].start.min,&bTime[i].arrive.h,&bTime[i].arrive.min);
		qsort(aTime,nA,sizeof(aTime[0]),cmp);
		qsort(bTime,nB,sizeof(bTime[0]),cmp);
		int vA[110]={0};
		for(int i=0;i<nA;i++)
		{
			aP[i]=find(aTime[i],bTime,nB,t,vA);
			vA[aP[i]]=1;
		}
		int vB[110]={0};
		for(int i=0;i<nB;i++)
		{
			bP[i]=find(bTime[i],aTime,nA,t,vB);
			vB[bP[i]]=1;
		}
		aCount=fcount(aP,bP,nA,nB);
		bCount=fcount(bP,aP,nB,nA);
		printf("Case #%d: %d %d\n",k,aCount,bCount);
	}
	return 0;
}
