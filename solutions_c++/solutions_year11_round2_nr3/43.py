#include<stdio.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

const int MAXN = 100+1;

int a[MAXN][MAXN];
int n;
int T, m;
int b[MAXN][MAXN];
int bn;
int len[MAXN];
int up[MAXN], down[MAXN];
int ret = 0;
int upper;
int col[MAXN];
int check[MAXN];
int val[MAXN];

void Go(int Dep)
{
	if(Dep == n)
	{
		int l1, l2;
		int kind = n;
		for(l1=1;l1<n;l1++)
		{
			for(l2=0;l2<l1;l2++)
			{
				if(col[l1] == col[l2])
				{
					kind--;
					break;
				}
			}
		}
		if(kind <= ret) return;

		int cnt = 0;
		for(l1=0;l1<bn;l1++)
		{
			for(l2=1;l2<=upper;l2++) check[l2] = 0;
			for(l2=0;l2<len[l1];l2++)
			{
				check[col[b[l1][l2]]] = 1;
			}
			cnt = 0;
			for(l2=1;l2<=upper;l2++) if(check[l2]) cnt++;
			if(cnt != kind) return;
		}

		ret = kind;
		for(l1=0;l1<n;l1++) val[l1] = col[l1];
	}
	else
	{
		int l1;
		for(l1=1;l1<=upper;l1++)
		{
			col[Dep] = l1;
			Go(Dep + 1);
		}
	}
}

int main(void)
{
	freopen("c1.in","r",stdin);
	freopen("c1.out","w",stdout);

	int l0, l1, l2, l3;

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&m);
		for(l1=0;l1<n;l1++) for(l2=0;l2<n;l2++) a[l1][l2] = 0;

		for(l1=0;l1<n;l1++)
		{
			l2 = (l1 + 1) % n;
			a[l1][l2] = a[l2][l1] = 1;
		}

		for(l1=0;l1<m;l1++)
		{
			scanf("%d",&up[l1]);
			up[l1]--;
		}
		for(l1=0;l1<m;l1++)
		{
			scanf("%d",&down[l1]);
			down[l1]--;

			a[up[l1]][down[l1]] = 1;
			a[down[l1]][up[l1]] = 1;
		}

		bn = 1;
		for(l1=0;l1<n;l1++) b[0][l1] = l1;
		len[0] = n;

		for(l1=0;l1<m;l1++)
		{
			for(l2=0;l2<bn;l2++)
			{
				int flag1 = -1, flag2 = -1;

				for(l3=0;l3<len[l2];l3++)
				{
					if(b[l2][l3] == up[l1]) flag1 = l3;
					if(b[l2][l3] == down[l1]) flag2 = l3;
				}

				if(flag1 == -1 || flag2 == -1) continue;

				// div
				if(flag1 > flag2)
				{
					Swap(flag1, flag2);
				}

				len[bn] = 0;
				for(l3=flag1;l3<=flag2;l3++)
				{
					b[bn][len[bn]] = b[l2][l3];
					len[bn]++;
				}
				bn++;

				for(l3=flag2;l3<len[l2];l3++)
				{
					b[l2][l3 - (flag2 - flag1 - 1)] = b[l2][l3];
				}
				len[l2] -= flag2 - flag1 - 1;

				break;
			}
		}

		/*
		for(l1=0;l1<bn;l1++)
		{
			for(l2=0;l2<len[l1];l2++)
			{
				printf("%d ",b[l1][l2] + 1);
			}
			printf("\n");
		}
		*/

		upper = len[0];
		for(l1=0;l1<bn;l1++) if(upper > len[l1]) upper = len[l1];

		ret = 0;

		Go(0);

		printf("Case #%d: %d\n",l0,ret);
		for(l1=0;l1<n;l1++)
		{
			if(l1) printf(" ");
			printf("%d",val[l1]);
		}
		printf("\n");
	}
	return 0;
}