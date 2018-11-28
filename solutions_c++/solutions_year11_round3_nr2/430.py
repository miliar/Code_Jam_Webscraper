//B

#include <iostream>
#include <stdio.h>
using namespace std;

#define LL long long

int main()
{
	//files
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	//vars
	int tt,t;
	int L,N,C;
	LL T;
	int a,b;
	LL cur,best;
	LL dist[1005],sum[1005];
	//testcase loop
	scanf("%d",&tt);
		for (t=1; t<=tt; t++)
		{
			memset(dist,0,sizeof(dist));
			memset(sum,0,sizeof(sum));
			//input
			cin >> L >> T >> N >> C;
				for (a=0; a<C; a++)
					cin >> dist[a];
			//compute distances
				for (a=C; a<N; a++)
					dist[a]=dist[a%C];
			//compute prefix sums
			sum[0]=0;
				for (a=1; a<=N; a++)
					sum[a]=sum[a-1]+dist[a-1];
			//brute force
			best=sum[N]*2;
				if (L)
					for (a=0; a<=N; a++)
						for (b=(L<2?N:a+1); b<=N; b++)
						{
							//half speed up to a
							cur=sum[a]*2;
							//full speed from a to a+1
								if (cur>=T)
									cur+=dist[a];
								else
								if (cur+dist[a]<=T)
									cur+=dist[a]*2;
								else
									cur+=(T-cur) + dist[a]-(T-cur)/2;
							//half speed up to b
							cur+=(sum[b]-sum[a+1])*2;
							//full speed from b to b+1 (if it exists)
								if (b<N)
									if (cur>=T)
										cur+=dist[b];
									else
									if (cur+dist[b]<=T)
										cur+=dist[b]*2;
									else
										cur+=(T-cur)*2 + dist[b]-(T-cur);
							//half speed to the end
								if (b<N)
									cur+=(sum[N]-sum[b+1])*2;
							//new best?
								if (cur<best)
									best=cur;
						}
			//output
			printf("Case #%d: ",t);
			cout << best << endl;
		}
	return(0);
}