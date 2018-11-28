#include <stdio.h>
#include <memory.h>

int su,data[1025],T,P;
__int64 cost[1025];
__int64 dynamic[1025][11][2];

void process()
{
	int i,j,m,k;
	__int64 min1,min2;

	memset(dynamic,100,sizeof(dynamic));
	for(i=su-1;i>=su/2;i--) {
		m=(data[i*2+2-su]>data[i*2+1-su]) ? data[i*2+2-su]:data[i*2+1-su];
		dynamic[i][m][0]=0; 
		if(m!=0) dynamic[i][m-1][1]=cost[i];
	}

	for(i=su/2-1;i>=1;i--) {
		for(j=P;j>=0;j--)
			for(m=0;m<=1;m++) {
				min1=100000000; min1*=100;
				for(k=0;k<=P && k<=j+m;k++) {
					if(min1>dynamic[i*2+1][k][0]) min1=dynamic[i*2+1][k][0];
					if(min1>dynamic[i*2+1][k][1]) min1=dynamic[i*2+1][k][1];
				}
				min2=100000000; min2*=100;
				for(k=0;k<=P && k<=j+m;k++) {
					if(min2>dynamic[i*2][k][0]) min2=dynamic[i*2][k][0];
					if(min2>dynamic[i*2][k][1]) min2=dynamic[i*2][k][1];
				}

				if(dynamic[i][j][m]>min1+min2+m*cost[i]) dynamic[i][j][m]=min1+min2+m*cost[i];
			}
	}
	min1=dynamic[1][0][0];
	if(min1>dynamic[1][0][1]) min1=dynamic[1][0][1];
	printf("Case #%d: %I64d\n",++T,min1);
}

int main()
{
	int i,test,p,start,end,j;

	freopen("B-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	for(scanf("%d",&test);test;test--) {
		scanf("%d",&p); su=1; P=p;
		while(p) { su*=2; p--; }
		for(i=1;i<=su;i++) {
			scanf("%d",&data[i]);
			data[i]=P-data[i];
		}
		start=su;
		for(j=1;j<=P;j++) {
			start/=2; end=start*2-1;
			for(i=start;i<=end;i++) scanf("%I64d",&cost[i]);
		}
		process();
	}
	return 0;
}
