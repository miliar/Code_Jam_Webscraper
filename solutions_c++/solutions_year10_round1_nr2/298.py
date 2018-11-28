#include <cstdio>
#include <cstdlib>


#define MAX 128
#define MAXA 256
#define INF 0x3f3f3f3f


int min(int a, int b)
{
	if (a < b)
	{
		return a;
	}
	return b;
}

int max(int a, int b)
{
	if (a > b)
	{
		return a;
	}
	return b;
}


int del, ins, m, n;

int v[MAX];
int pd[MAX][MAXA];

int main()
{
	int t;
	int cas;


	scanf("%d", &t);
	for (cas=1; cas<=t; cas++)
	{
		printf("Case #%d: ", cas);
		scanf("%d %d %d %d", &del, &ins, &m, &n);
		int i;

		for (i=0; i<n; i++)
		{
			scanf("%d", &v[i]);
		}

		int j;

		for (j=0; j<MAXA; j++)
		{
			pd[0][j] = min(del,abs(j-v[0]));
		}

		for (i=1; i<n; i++)
		{
			for (j=0; j<MAXA; j++) //deleta
			{
				pd[i][j] = pd[i-1][j] + del;
			}

			
			int menor;
			int k;
			for (j=0; j<MAXA; j++) //muda
			{
				menor = INF;
				for (k=max(0,j-m); k<=min(255,j+m); k++)
				{
					menor = min(menor, pd[i-1][k]+abs(v[i]-j));
				}
				pd[i][j] = min(pd[i][j], menor);
			}


if (m!=0)
{

//			for (j=0; j<MAXA; j++) //insere
			j = v[i];
			{
				menor = INF;
				for (k=0; k<MAXA; k++)
				{
//					k=j;
					int temp;
					temp = abs(k-v[i]);
					if (temp <=m)
					{
						temp = 0;
					}
					else if (temp%m == 0)
					{
						temp = temp/m - 1;
					}
					else
					{
						temp = temp/m;
					}
					menor = min(menor, pd[i-1][k] + temp*ins);
				}
				pd[i][j] = min(pd[i][j], menor);
			}
}

		}
		int mm = INF;

/*		for (i=0; i<n; i++)
		{
			for (j=0; j<MAXA; j++)
			{
				printf("%d ", pd[i][j]);
			}	
			printf("\n");
		}
*/
		for (i=0; i<MAXA; i++)
		{
			mm = min(mm, pd[n-1][i]);
		}
		printf("%d\n", mm);
	}
	
	return 0;
}
