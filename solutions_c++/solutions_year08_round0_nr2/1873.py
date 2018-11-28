#include <cstdio>
#include <algorithm>

int n,test,na,nb,t,i,j, e[2][2000], a,b,ca,cb;

int gett()
{
	int h,m;
	scanf("%d:%d",&h,&m);
	return h*60+m;
}

int main()
{
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B-small-attempt1.out","wt",stdout);
	scanf("%d",&n);
	for (test=1; test<=n; test++)
	{
		memset(e,0,sizeof(e));
		scanf("%d",&t);
		scanf("%d%d",&na,&nb);
		for (i=0; i<na; i++)
		{
			e[0][gett()]-=1;
			e[1][gett()+t]+=1;
		}
		for (i=0; i<nb; i++)
		{
			e[1][gett()]-=1;
			e[0][gett()+t]+=1;
		}
		a=b=0;
		ca=cb=0;
		for(i=0; i<24*60; i++)
		{
			ca+=e[0][i];
			//if (ca) printf("ca=%d ",ca);
			if (ca<0)
			{
				ca++;
				a++;
			}
			cb+=e[1][i];
			//if (cb) printf(" cb=%d ",cb);
			if (cb<0)
			{
				cb++;
				b++;
			}
		}
		printf("Case #%d: %d %d\n",test,a,b);
	}
	return 0;
}

/*
2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02

*/