#include <cstdio>

int main()
{
	int T,count=0,R,k,N;
	scanf("%d",&T);
	while(count<T)
	{
		scanf("%d %d %d",&R,&k,&N);
		int *B=new int[N];
		for(int i=0;i<N;i++)
			scanf("%d",&B[i]);
		int q=0,b,n,nr=0;
		for(int i=0;i<R;i++)
		{
			n=k;
			b=q;
			do
			{
				n-=B[q];
				q++;
				if(q==N)
					q=0;
			}while(n>=B[q] && q!=b);
			nr+=k-n;
		}
		delete []B;
		count++;
		fprintf(stderr,"Case %d done\r",count);
		printf("Case #%d: %d\n",count,nr);
	}
	return 0;
}
