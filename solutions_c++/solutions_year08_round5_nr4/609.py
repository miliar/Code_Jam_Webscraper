#include <stdio.h>
#include <string.h>

#define M 100000008
#define X 10007

short map[4][M];

int main()
{
	int N,H,W,R;
	int r[10],c[10];
	int i,j,k,t;
	short *p1,*p2,*p3,*p4,*pt;

	scanf("%d",&N);
	for(k=1;k<=N;k++)
	{
		scanf("%d%d%d",&H,&W,&R);
		for(i=0;i<R;i++)
		{
			scanf("%d%d",r+i,c+i);
			c[i]--;
		}

		p1=map[0];
		p2=map[1];
		p3=map[2];
		p4=map[3];

		memset(p1,0,sizeof(short)*W);
		memset(p2,0,sizeof(short)*W);
		memset(p3,0,sizeof(short)*W);
		memset(p4,0,sizeof(short)*W);

		p1[0]=1;
		for(i=1;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				if(p1[j]==0) goto next;
				for(t=0;t<R;t++)
				{
					if(r[t]==i && c[t]==j) goto next;
				}

				p2[j+2]+=p1[j];
				if(p2[j+2]>=X) p2[j+2]-=X;

				p3[j+1]+=p1[j];
				if(p3[j+1]>=X) p3[j+1]-=X;
next:
				;
			}
			pt=p1;p1=p2;p2=p3;p3=p4;p4=pt;
			memset(pt,0,sizeof(short)*W);
		}

		printf("Case #%d: %d\n",k,p1[W-1]);
	}

	return 0;
}
