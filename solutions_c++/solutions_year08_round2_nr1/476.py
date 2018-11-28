#include<stdio.h>
struct mm
{
	__int64 x,y ;
}a[1000000];
int main()
{
	__int64  N,A,B,C,D,x0,y0,M;
	int test,k,i,j,z;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	while(scanf("%d",&test) == 1)
	{
		for(k = 1;k <= test ;k ++)
		{
			scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&N,&A,&B,&C,&D,&x0,&y0,&M);
			int i ;
			a[0].x = x0;
			a[0].y = y0;
			for(i = 1 ;i <= N -1; i ++)
			{
				a[i].x = (A*x0 + B)%M;
				a[i].y = (C*y0 + D)%M;
				x0 = a[i].x;
				y0= a[i].y;
			}
			__int64  count = 0 ;
			for(i = 0 ;i < N ; i ++)
				for(j = i +1; j < N ; j ++)
					for(z = j +1; z < N  ; z ++)
					{
						if(((a[i].x + a[j].x + a[z].x)%3 == 0 )&&((a[i].y + a[j].y + a[z].y ) %3 == 0))
							count ++;
					}
			printf("Case #%d: %I64d\n",k,count);
	}

	}
	return 0;
}