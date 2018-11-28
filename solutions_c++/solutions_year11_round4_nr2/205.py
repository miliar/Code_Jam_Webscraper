#include <stdio.h>

int Weight[100][100];
int isBalance(int y,int x,int sz)
{
	//x Balance Sum
	int half = sz/2;
	int leftSum = 0, rightSum = 0;
	for (int q=0;q<half;++q)
	{
		for (int w=0;w<sz;++w)
		{
			if (q==0 && (w==0 || w==sz-1)) continue;
			leftSum += Weight[y+w][x+q] * (half -q);
			rightSum += Weight[y+w][x+sz-1-q] * (half -q);
		}
	}
	if (leftSum != rightSum) return 0;

	int topSum = 0, btSum = 0;
	for (int q=0;q<half;++q)
	{
		for (int w=0;w<sz;++w)
		{
			if (q==0 && (w==0 || w==sz-1)) continue;
			topSum += Weight[y+q][x+w] * (half -q);
			btSum += Weight[y+sz-1-q][x+w] * (half -q);
		}
	}
	if (topSum != btSum) return 0;
	
	return 1;
}

int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int R,C,D;
		scanf("%d %d %d",&R,&C,&D);
		for (int q=0;q<R;++q) 
		{
			char tmp[256];
			scanf("%s",tmp);
			for (int w=0;w<C;++w)
				Weight[q][w] = D + tmp[w] - '0';
		}

		int ret = -1;
		for (int k=10;k>=3;--k)
		{
			for (int q=0;q+k-1<R;++q) for (int w=0;w+k-1<C;++w)
			{
				if (isBalance(q,w,k)) ret = k;
			}
			if (ret>=0) break;
		}
		if (ret<0) printf("Case #%d: IMPOSSIBLE\n",kase);
		else	   printf("Case #%d: %d\n",kase,ret);

	}
	return 0;
}
