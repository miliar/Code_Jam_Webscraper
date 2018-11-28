#include <stdio.h>
#include <string.h>

int n;
char a[305][305];
char b[305][305];

int large=1000000000;

int check(int x,int y){
	memset(b,0,sizeof(b));
	int i, j;
	for(i=1;i<2*n;i++)
		for(j=1;j<2*n;j++)
			b[i][j]=a[i][j];
	for(i=1;i<x;i++)
		for(j=1;j<=4*n;j++)
			if(b[2*x - i][j]>='0' && b[2*x-i][j]<='9' && b[2*x-i][j]!=b[i][j])
				return large;
			else
				b[2*x-i][j] = b[i][j];
	for(i=1;i<=4*n;i++)
		for(j=1;j<y;j++)
			if(b[i][2*y-j]>='0' && b[i][2*y-j]<='9' && b[i][2*y-j]!=b[i][j])
				return large;
			else
				b[i][2*y-j] = b[i][j];
	//printf("%d %d\n",x,y);
	return (x-n+y)*(x-n+y);
}

int main(void)
{
	int T, i, j;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		gets(a[0]);
		for(i=1;i<2*n;i++)
			gets(a[i]+1);
		int minsq = large;
		
		
		for(i=n;i<=2*n;i++)
			for(j=n;j<=2*n;j++){
				int r = check(i, j);
				if(r < minsq)
					minsq = r;
			}
//horz
		memset(b,0,sizeof(b));
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				b[i][j] = a[i][2*n-j];
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				a[i][j] = b[i][j];

		for(i=n;i<=2*n;i++)
			for(j=n;j<=2*n;j++){
				int r = check(i, j);
				if(r < minsq)
					minsq = r;
			}
//vert
		memset(b,0,sizeof(b));
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				b[i][j] = a[2*n-i][j];
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				a[i][j] = b[i][j];
		for(i=n;i<=2*n;i++)
			for(j=n;j<=2*n;j++){
				int r = check(i, j);
				if(r < minsq)
					minsq = r;
			}
//horz
		memset(b,0,sizeof(b));
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				b[i][j] = a[i][2*n-j];
		for(i=1;i<2*n;i++)
			for(j=1;j<2*n;j++)
				a[i][j] = b[i][j];

		for(i=n;i<=2*n;i++)
			for(j=n;j<=2*n;j++){
				int r = check(i, j);
				if(r < minsq)
					minsq = r;
			}

		printf("Case #%d: %d\n", cs, minsq - n*n);
		fprintf(stderr,"Case #%d: %d\n", cs, minsq - n*n);
	}
	return 0;
}
