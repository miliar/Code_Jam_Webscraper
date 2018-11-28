#include<stdio.h>
#define ABS(X) ((X) > 0 ? (X) : (-(X)))

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int x1,x2,y1,y2,found;
	int T,ks,N,M,A;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d%d",&N,&M,&A);

		found=1;
		for(x1=0;x1<=N && found;x1++)
			for(y1=0;y1<=M && found;y1++)
				for(x2=0;x2<=N && found;x2++)
					for(y2=0;y2<=M && found;y2++)
						if( ABS(x1*y2 - y1*x2) == A )
						{
							found=0;
							printf("Case #%d: %d %d %d %d %d %d\n",ks,0,0,x1,y1,x2,y2);
						}

		if(found) printf("Case #%d: IMPOSSIBLE\n",ks);
	}

	return 0;
}