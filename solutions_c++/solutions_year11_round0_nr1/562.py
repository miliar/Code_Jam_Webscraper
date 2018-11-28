#include<cstdio>

int abs(int x)
{
	if (x < 0) return -x; else return x;
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
	int cases;
	scanf("%d" ,  &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		int n;
		scanf("%d" , &n);
		int oPosi = 1;
		int bPosi = 1;
		int oTime = 0;
		int bTime = 0;
		int totalTime = 0;
		char type[2];
		int posi;
		for (int i = 0; i < n; ++i)
		{
			scanf("%s%d", type , &posi);
			if (type[0] == 'O')
			{
				int move = abs(posi - oPosi);
				if (oTime + move > totalTime) totalTime = oTime + move;
				++totalTime;
				oPosi = posi;
				oTime = totalTime;
			}
			else
			{
				int move = abs(posi - bPosi);
				if (bTime + move > totalTime) totalTime = bTime + move;
				++totalTime;
				bPosi = posi;
				bTime = totalTime;
			}
		}
		printf("Case #%d: %d\n", ca , totalTime);
	}
}
