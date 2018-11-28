#include <iostream>
using namespace std;
int map[101][101];
int temp[101][101];
int M[2000];
int main()
{
	int t, i, j, n, m, cas = 0, r, k;
	int x1, x2, y1, y2;
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{
		int res = 0;
		int p, num;
		scanf("%d", &p);
		num = (1 << p);
		for(i = 0; i < num; i ++)
		{
			scanf("%d", &M[i]);
			M[i] = p - M[i];
			if(M[i] < 0) M[i] = 0;
		}
		int price;
		for(i = p - 1; i >= 0; i --)
		{
			for(j = 0; j < (1 << i); j ++)
				scanf("%d", &price);
		}
		int index = p;
		while(index != 0)
		{
			for(i = 0; i < num; i += (1 << index))
			{
				for(j = 0; j < (1 << index) ; j ++)
				{
					if(M[i + j] != 0)
						break;
				}
				if(j != (1 << index))
				{
					res ++;
					for(j = 0; j < (1 << index) ; j ++)
					{
						if(M[i + j] != 0)
							M[i + j] --;
					}
				}
			}
			for(i = 0; i < num; i ++)
			{
				if(M[i] != 0)
					break;
			}
			if(i == num)
				break;
			index --;
		}
		printf("Case #%d: %d\n", ++cas, res);
	}
}