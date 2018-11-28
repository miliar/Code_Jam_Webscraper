#include <stdio.h>
#include <string.h>

int a[105][105];
int e[105][105];

int check(void){
	int i, j;
	for(i=1;i<=100;i++)
		for(j=1;j<=100;j++)
			if(a[i-1][j] && a[i][j-1])
				e[i][j]=1;
			else if(!a[i-1][j] && !a[i][j-1])
				e[i][j]=0;
			else
				e[i][j]=a[i][j];
	int r=0;
	for(i=1;i<=100;i++)
		for(j=1;j<=100;j++){
			a[i][j]=e[i][j];
			if(a[i][j]) r=1;
		}
	return r;
}

int main(void)
{
	int T,i, R;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d",&R);
		memset(a,0,sizeof(a));
		memset(e,0,sizeof(e));

		for(i=0;i<R;i++){
			int xa,ya,xb,yb;
			scanf("%d%d%d%d",&xa,&ya,&xb,&yb);
			if(xa>xb){int tmp=xa;xa=xb;xb=tmp;}
			if(ya>yb){int tmp=ya;ya=yb;yb=tmp;}
			for(int xi=xa;xi<=xb;xi++)
				for(int xj=ya;xj<=yb;xj++)
					a[xi][xj] = 1;
		}
		int t=0;
		while(check())
			t++;
		if(R==0) t=0;else ++t;
		printf("Case #%d: %d\n", cs, t);
		/*for(i=1;i<=100;i++)
			for(j=1;j<=100;j++){

			}*/
		
	}
	return 0;
}
