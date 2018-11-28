#include<stdio.h>

#define INF 1000000000

int n, m;
int a[111][111];
int b[111][111];
int G[111][111];
int mapping[111111];
int Gn;

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

void Go(int l1, int l2)
{
	int temp;

	if(G[l1][l2] == 0)
	{
		G[l1][l2] = Gn;

		int l3, l4, dir;
		for(temp=0;temp<4;temp++)
		{
			l3 = l1 + dx[temp];
			l4 = l2 + dy[temp];

			dir = b[l3][l4];
			if(dir != -1)
			{
				if(l3 + dx[dir] == l1 && l4 + dy[dir] == l2)
				{
					Go(l3, l4);
				}
			}
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;
	int T;

	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);

	scanf("%d",&T);


	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&m);
		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				scanf("%d",&a[l1][l2]);
			}
		}
		for(l1=0;l1<=n+1;l1++)
		{
			a[l1][0] = a[l1][m+1] = INF;
		}
		for(l2=0;l2<=m+1;l2++)
		{
			a[0][l2] = a[n+1][l2] = INF;
		}

		Gn = 0;

		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				int lowest = a[l1][l2];
				int dir = -1;
				
				for(l3=0;l3<4;l3++)
				{
					if(a[l1 + dx[l3]][l2 + dy[l3]] < lowest)
					{
						lowest = a[l1 + dx[l3]][l2 + dy[l3]];
						dir = l3;
					}
				}
				b[l1][l2] = dir;
			}
		}

		for(l1=1;l1<=n;l1++) for(l2=1;l2<=m;l2++) G[l1][l2] = 0;

		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				if(b[l1][l2] == -1)
				{
					Gn++;
					Go(l1, l2);
				}
			}
		}

		for(l1=1;l1<=Gn;l1++) mapping[l1] = 0;
		int mn = 0;

		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				if(mapping[ G[l1][l2] ] == 0)
				{
					mapping[ G[l1][l2] ] = ++mn;
				}
			}
		}

		printf("Case #%d:\n",l0);
		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				if(l2 > 1) printf(" ");
				printf("%c",mapping[G[l1][l2]]+'a'-1);
			}
			printf("\n");
		}
	}
}