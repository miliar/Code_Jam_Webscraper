#include <cstdio>
#include <cstdlib>
int A,N,M,Test,Case;

inline int area(int x1,int y1,int x2,int y2,int x3,int y3)
{
	#define cpt(x1,y1,x2,y2) ((x1)*(y2)-(x2)*(y1))
	return labs(cpt(x2-x1,y2-y1,x3-x1,y3-y1));
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&Test);Test;Test--)
	{
		scanf("%d%d%d",&N,&M,&A);
		for (int x3=0;x3<=N;++x3)
			for (int x2=0;x2<=N;++x2)
				for (int y2=0;y2<=M;++y2)
					for (int y3=0;y3<=M;++y3)
						if (area(0,0,x2,y2,x3,y3)==A)
						{
							printf("Case #%d: %d %d %d %d %d %d\n",++Case,0,0,x2,y2,x3,y3);
							goto okl;
						}
		printf("Case #%d: IMPOSSIBLE\n",++Case);
		okl:;
	}
	return 0;
}
