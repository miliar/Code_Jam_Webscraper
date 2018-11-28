#include<stdio.h>
int T, N, M[1050];
__int64 d[11][1025][11];
__int64 cost[11][1025];
inline __int64 max(__int64 a,__int64 b)
{
	return a<b?b:a;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	int t, i, j,k, p, p1, p2;
	for(t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for(i=1;i<=(1<<N);i++)
		{
			scanf("%d",&M[i]);
			if(M[i] > N) M[i] = N;
			M[i] = N-M[i];
		}

		k=(1<<N);
		for(i=1;i<=N;i++){
			k >>= 1;
			for(j=1;j<=k;j++){
				scanf("%d",&cost[i][j]);
				for(p=0;p<=N;p++) d[i][j][p] = 0x7ffffffe;
				
				if(i==1){
					d[i][j][max(M[j*2], M[j*2-1])] = 0;
					if(max(M[j*2],M[j*2-1]) != 0) d[i][j][max(M[j*2], M[j*2-1])-1] = cost[i][j];
				}
			}
		}

		k=(1<<N);
		for(i=1;i<N;i++){
			k >>= 1;
			for(j=1;j<=k;j+=2){
				for(p1=0;p1<=N;p1++) for(p2=0;p2<=N;p2++){
					if(d[i+1][(j+1)/2][max(p1,p2)] > d[i][j][p1] + d[i][j+1][p2]) d[i+1][(j+1)/2][max(p1,p2)] = d[i][j][p1] + d[i][j+1][p2];
					if(max(p1,p2)!=0 && d[i+1][(j+1)/2][max(p1,p2)-1] > d[i][j][p1] + d[i][j+1][p2] + cost[i+1][(j+1)/2])  d[i+1][(j+1)/2][max(p1,p2)-1] = d[i][j][p1] + d[i][j+1][p2] + cost[i+1][(j+1)/2];
				}
			}
		}
		printf("Case #%d: %I64d\n",t,d[N][1][0]);

	}
	return 0;
}