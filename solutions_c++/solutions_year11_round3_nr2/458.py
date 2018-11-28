#include <stdio.h>

#define MAX 1100

int d[MAX];
int a[MAX];
int built[MAX];

int tempo(int n, int t)
{
	int i;
	int resp=0;

	for(i=0;i<n;++i)
	{
		if(!built[i])
			resp+=2*d[i];
		else
		{
			int dt = t-resp;
			if(dt<0)
				dt=0;
			if(dt>=2*d[i])
				dt=2*d[i];
			resp+=dt+d[i]-(dt/2);

		}
	}
	return resp;
}

int main()
{
	int T,ccnt;

	int l,t,n,c;

	int i,j;

	scanf("%d",&T);
	for(ccnt=1;ccnt<=T;++ccnt)
	{
		scanf("%d %d %d %d",&l,&t,&n,&c);
		for(i=0;i<c;++i)
			scanf("%d",&a[i]);
		for(j=0;j*c<n;++j)
			for(i=0;i<c && i+j*c<n;++i)
				d[i+j*c]=a[i];

		for(i=0;i<n;++i)
			built[i]=0;

		int resp=100100100;

		if(l==0)
			resp=tempo(n,t);
		else if(l==1)
			for(i=0;i<n;++i)
			{
				built[i]=1;
				int cand = tempo(n,t);
				built[i]=0;

				if(cand<resp)
					resp=cand;
			}
		else
			for(i=0;i<n;++i)
			{
				built[i]=1;
				for(j=i+1;j<n;++j)
				{
					built[j]=1;
					int cand = tempo(n,t);
					built[j]=0;

					if(cand<resp)
						resp=cand;

				}
				built[i]=0;
			}

		printf("Case #%d: %d\n",ccnt,resp);
	}
	return 0;
}

