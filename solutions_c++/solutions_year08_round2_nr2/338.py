#include <stdio.h>
#include <memory.h>
int p[1001], pn;
bool bo[1001];

void init()
{
	int i, j;
	pn = 0;
	memset(bo, 0, sizeof(bo));
	for (i = 2; i < 1001; i++)
	{
		if (!bo[i])
		{
			p[pn++]= i;
			for (j = i * i; j < 1001; j +=i)
			{
				bo[j] = true;
			}
		}
	} 
}

int fa[1001];

int findfa(int u)
{
	while(u!=fa[u]) u=fa[u];
	return u;
}

int main()
{
 		freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
	int i,j ,k,start, T, t, A, B,P , num;
	init();
	scanf("%d", &T);
	for (t=1;t<=T;t++)
	{
		scanf("%d%d%d",&A,&B,&P);
		for (i = 0; i < pn; i++)
		{
			if (p[i] >= P) break;
		}
		start = i;
		num = B - A + 1;
		for (i = A; i<=B;i++) fa[i] = i;
		for (i = A; i<=B;i++)
		{
			for (j = A; j <i; j++)
			{
				if (findfa(j) == findfa(i)) continue;
				for (k = start; k < pn && p[k] <= j; k++)
				{
					
					if (i%p[k] == 0  && j %p[k] ==0)
					{
						fa[findfa(j)] = i;
						num--;
						break;
					}
				} 
			}
		}
		printf("Case #%d: %d\n", t, num);
		
	}
	return 0;
}
