#include<stdio.h>
#include<string.h>
#define mm(a) memset(a,0,sizeof(a))
struct mm
{
	int s,t;
};
bool operator<(const mm&a,const mm&b)
{
	return a.s<b.s;
}
mm a[111],b[111];
int sta[60*24],stb[60*24];

int main()
{
	int i,j,w,n,m,k,t,p,q,e=1;
	freopen("test.in","r",stdin);
	freopen("test.txt","w",stdout);
	scanf("%d",&w);
	while(w--)
	{
		scanf("%d",&t);
		scanf("%d%d",&n,&m);
		mm(sta);
		mm(stb);
		for(i=0;i<n;i++)
		{
			scanf("%d:%d",&p,&q);
			a[i].s=p*60+q;
			scanf("%d:%d",&p,&q);
			a[i].t=p*60+q;
			sta[a[i].s]++;
			stb[a[i].t+t]--;
		}
		for(i=0;i<m;i++)
		{
			scanf("%d:%d",&p,&q);
			b[i].s=p*60+q;
			scanf("%d:%d",&p,&q);
			b[i].t=p*60+q;
			stb[b[i].s]++;
			sta[b[i].t+t]--;
		}
		int nea=0,neb=0,ala=0,alb=0;
		for(i=0;i<24*60;i++)
		{
			if(sta[i]>0)
			{
				if(sta[i]<=ala)
					ala-=sta[i];
				else nea+=sta[i]-ala,ala=0;
			}
			else if(sta[i]<0)
				ala-=sta[i];

			if(stb[i]>0)
			{
				if(stb[i]<=alb)
					alb-=stb[i];
				else neb+=stb[i]-alb,alb=0;
			}
			else if(stb[i]<0)
				alb-=stb[i];
		}
		printf("Case #%d: %d %d\n",e++,nea,neb);
	}
	return 0;
}