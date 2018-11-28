#include <stdio.h>
#include <string.h>

int tc, ntc;
int N, M, A;

int myabs(int x)
{
	return (x<0)?-x:x;
}

int main()
{
	scanf("%d",&ntc);
	int x1,y1,x2,y2;
	bool found;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d %d %d",&N,&M,&A);
		
		found = false;
		for (x1=0; x1<=N; x1++) for (y1=0; y1<=M; y1++)
		for (x2=0; x2<=N; x2++) for (y2=0; y2<=M; y2++)
			if (myabs(x1*y2 - x2*y1) == A) 
			{
				found = true;
				goto fin;
			}
			
		fin:;
		printf("Case #%d: ",tc);
		if (!found) printf("IMPOSSIBLE\n");
		else printf("%d %d %d %d %d %d\n",0,0,x1,y1,x2,y2);
		
	}
}