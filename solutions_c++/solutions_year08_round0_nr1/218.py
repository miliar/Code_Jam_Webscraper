#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define  INF 10000000

struct  eng
{
	char s[110];
}eg[110];

int qu[1100];
int f[11000][110];

int cmp(const void *a, const void *b)
{
	eng *A = (eng *)a;
	eng *B = (eng *)b;
	return strcmp(A->s , B->s);
}


int bs(char t[], int len)
{
	int l, h, m;
	for(int i = 0; i < len; i++)
	{
		if(!strcmp(t, eg[i].s)) return i;
	}
/*	l = 0, h = len-1;
	while(l <= h)
	{
		m = (l+h)/2;
		int tmp = strcmp(t, eg[m].s);
		if(tmp< 0) h = m-1;
		else if(tmp > 0) l = m + 1;
		else return m;
	}
	return -1;*/
}
int main()
{
	int n, s, q;
	char th[110];
	int kcase=0;
	freopen("A-large.in", "r", stdin);
	freopen("o.txt", "w", stdout);
	scanf("%d", &n);
	while(n--)
	{
		scanf("%d", &s);
		getchar();
		for(int i = 0; i < s; i++) gets(eg[i].s);
		qsort(eg, s, sizeof(eng), cmp);
		//for(int i = 0; i < s; i++) printf("%s\n", eg[i].s);
		scanf("%d", &q);
		getchar();
		for(int i = 0; i < q; i++)
		{
			gets(th);
			qu[i] = bs(th, s);
		//	printf("%d ", qu[i]);
		}
	/*	for(int i = 0; i < q; i++)
		{
			printf("%d ", qu[i]);
		}*/
	//	printf("\n");
		for(int i = 0; i < q; i++)
			for(int j = 0; j < s; j++) f[i][j] = INF;
		for(int i = 0; i < s; i++)
		{
			if(qu[0] != i) f[0][i] = 0;
			else f[0][i] = INF;
		}
		
		for(int i = 1; i < q; i++)
		{
			for(int j = 0; j < s; j++)
			{
				if(j == qu[i]) f[i][j] = INF;
				else 
				{
					int min = INF+INF;
					
					for(int k = 0; k < s; k++)
					{
						int temp = f[i-1][k] + (k != j);
						if(min > temp) min = temp;
					}
					f[i][j] = min;
				}
			}
		}
		
		/*for(int i = 1; i < q; i++)
		{
			for(int j = 0; j < s; j++)
			{
				printf("%d ", f[i][j]);
			}
			printf("\n");
		}*/
		int ans = INF+INF;
		for(int i = 0; i < s; i++)
			if(ans > f[q-1][i]) ans = f[q-1][i];
		printf("Case #%d: %d\n", ++kcase, ans); 
	}
	return 0;
}
