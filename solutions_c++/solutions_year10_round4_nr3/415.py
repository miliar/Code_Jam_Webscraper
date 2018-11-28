#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAX 200

int tab[2][MAX][MAX];

int main()
{
	int i,j,t;
	int T,ccnt;
	int x1,x2,y1,y2;
	int r;
	int tem;
	int at,pr;
	scanf("%d",&T);
	for(ccnt=1;ccnt<=T;++ccnt)
	{
		memset(tab,0,sizeof(tab));
		scanf("%d",&r);
		while(r--)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(i=x1;i<=x2;++i)
				for(j=y1;j<=y2;++j)
					tab[0][i+1][j+1]=1;
		}
		tem=1;
		for(t=0;tem;++t)
		{
			at=t&1;
			pr=!at;
			tem=0;
			for(i=1;i<MAX;++i)
				for(j=1;j<MAX;++j)
				{
					if(!tab[at][i][j])
						tab[pr][i][j]=(tab[at][i-1][j] && tab[at][i][j-1])?1:0;
					else
						tab[pr][i][j]=(tab[at][i-1][j] || tab[at][i][j-1])?1:0;
					if(tab[pr][i][j])
						tem=1;
				}
		}
		printf("Case #%d: %d\n",ccnt,t);
	}
	return 0;
}






