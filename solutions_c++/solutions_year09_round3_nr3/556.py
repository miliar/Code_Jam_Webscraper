#include <stdio.h>
#include <string.h>

int a[10];
int p , q;
int b[10];
int check[10];
int res , min;

void find(int x)
{
int i , L , r , j;

	if (x == q)
	{
		res = 0;
		for (i = 0; i < q; i ++)
		{
			L = 0; r = p+1;
			for (j = 0; j < i; j ++)
				if (b[j] > L && b[j] < b[i]) L = b[j];
				else if (b[j] < r && b[j] > b[i]) r = b[j];
			res += r - L - 2;
		}
		if (res < min) min = res;
		return;
	}
	for (i = 0; i < q; i ++)
		if (check[i] == 0)
		{
			b[x] = a[i];
			check[i] = 1;
			find(x + 1);
			check[i] = 0;
			b[x] = 0;
		}
}
int main()
{
int N , t , i;


	//freopen("C-small-attempt0.in" , "r" , stdin);
	//freopen("Csmall.txt" , "w" , stdout);
	scanf("%d" , &N);
	for (t = 1; t <= N; t ++)
	{
		scanf("%d %d" , &p , &q);
		min = 1e8;
		for (i = 0; i < q; i ++) scanf("%d" , &a[i]);
		memset(check , 0 , sizeof(check));
		find(0);
		printf("Case #%d: %d\n" , t , min);
	}
	return 0;
}