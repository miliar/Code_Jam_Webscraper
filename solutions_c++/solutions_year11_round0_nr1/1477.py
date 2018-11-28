#include <stdio.h>
#include <math.h>

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0;scanf("%d",&n);

		char color[10] = { 0 };
		int curpos[2] = { 1,1 };
		int spends[2] = { 0 };

		int ret = 0,x = 0;
		int p = 0,prev = 2;
		for(int i = 0;i < n;++i)
		{
			scanf("%s%d",color,&x);
			p = ('B'==color[0]?0:1);
			int dis = abs(x-curpos[p])+1;
			curpos[p] = x;
			if(prev != p)
			{
				int delta = dis-spends[1-p];
				if(delta>0) dis = delta;
				else dis = 1;
				spends[1-p] = 0;
			}
			ret += dis;
			spends[p] += dis;
			prev = p;
		}
		printf("Case #%d: %d\n",iCases,ret);
	}
	return 0;
}