#include <stdio.h>
#include <string.h>

int main()
{
	long long i,N,n, A, B, C, D, x0, y0, M,ii,r,X,Y,i1,i2,i3;
	long long rr[9];
	scanf("%d",&N);
	for (ii=0;ii<N;++ii)
	{
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n, &A, &B, &C, &D, &x0, &y0,&M);
		X=x0;
		Y=y0;		
		memset(rr,0,sizeof(rr));
		for (i=0;i<n;++i)
		{
			//printf("%lld %lld\n",X,Y);
			rr[3*(X%3)+(Y%3)]++;
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}
/*		for (i=0;i<9;++i) printf("%lld ",rr[i]);
		printf("\n");*/
		r=0;
		for (i1=0;i1<9;++i1)
			if ((((i1%3)+(i1%3)+(i1%3))%3)==0 && (((i1/3)+(i1/3)+(i1/3))%3)==0)
				r+=rr[i1]*(rr[i1]-1)*(rr[i1]-2);
		for (i1=0;i1<9;++i1)
			for (i2=0;i2<9;++i2) if (i2!=i1)
				for (i3=0;i3<9;++i3) if (i3!=i1 && i3!=i2)
					if ((((i1%3)+(i2%3)+(i3%3))%3)==0 && (((i1/3)+(i2/3)+(i3/3))%3)==0)
						r+=rr[i1]*rr[i2]*rr[i3];
		for (i1=0;i1<9;++i1)
			for (i2=0;i2<9;++i2) if (i2!=i1)
				if ((((i1%3)+(i2%3)+(i2%3))%3)==0 && (((i1/3)+(i2/3)+(i2/3))%3)==0)
					r+=rr[i1]*rr[i2]*(rr[i2]-1);
		printf("Case #%d: %d\n",ii+1,r/6);
	}
	return 0;
}
