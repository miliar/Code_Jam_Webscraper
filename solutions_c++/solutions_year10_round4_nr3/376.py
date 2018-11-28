#include <stdio.h>
#include <memory.h>
#define limit 200

int su,T;
bool data[2][202][202];

void process()
{
	int i,j,k,time=0,died;

	for(k=1;k<=limit;k++) {
		died=0;
		for(i=1;i<=limit;i++)
			for(j=1;j<=limit;j++) {
				if(data[0][i][j]) died=1;

				if(!data[0][i-1][j] && !data[0][i][j-1]) data[1][i][j]=0;
				else if(data[0][i-1][j] && data[0][i][j-1]) data[1][i][j]=1;
				else {
					if(data[0][i][j]) data[1][i][j]=1;
				}
			}
		if(died==0) break;
		else {
			time++;
			memcpy(data[0],data[1],sizeof(data[1]));
			memset(data[1],0,sizeof(data[1]));
		}
	}
	printf("Case #%d: %d\n",++T,time);
}

int main()
{
	int test,r,j,i,x1,x2,y1,y2,tmp;

	freopen("C-small-attempt0.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	for(scanf("%d",&test);test;test--) {
		scanf("%d",&su);
		memset(data,0,sizeof(data));
		for(r=1;r<=su;r++) {
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			if(x1>x2) { tmp=x1; x1=x2; x2=tmp; }
			if(y1>y2) { tmp=y1; y1=y2; y2=tmp; }
			for(i=y1;i<=y2;i++)
				for(j=x1;j<=x2;j++)
					data[0][i][j]=1;
		}
		process();
	}
	return 0;
}