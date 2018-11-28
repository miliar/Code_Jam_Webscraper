#include<stdio.h>

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int T;
int n, m;
int N;
int ret1, ret2;
int tt;

int a[1111], b[1111], c[1111], d[1111];

int main(void)
{
	int l0;
	int l1, l2;
	int t1, t2, t3, t4;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&tt);
		scanf("%d %d",&n,&m);
		N = 0;
		for(l1=0;l1<n;l1++)
		{
			scanf("%d:%d %d:%d",&t1,&t2,&t3,&t4);
			a[N] = t1 * 60 + t2;
			b[N] = t3 * 60 + t4;
			c[N] = 0;
			N++;
		}
		for(l1=0;l1<m;l1++)
		{
			scanf("%d:%d %d:%d",&t1,&t2,&t3,&t4);
			a[N] = t1 * 60 + t2;
			b[N] = t3 * 60 + t4;
			c[N] = 1;
			N++;
		}

		for(l1=0;l1<N;l1++) 
		{
			for(l2=l1+1;l2<N;l2++)
			{
				if(a[l1] > a[l2])
				{
					Swap(a[l1], a[l2]);
					Swap(b[l1], b[l2]);
					Swap(c[l1], c[l2]);
				}
			}
		}
		ret1 = ret2 = 0;

		for(l1=0;l1<N;l1++)
		{
			int idx = -1;
			d[l1] = 0;
			for(l2=0;l2<l1;l2++)
			{
				if(d[l2] == 0 && c[l1] != c[l2] && b[l2] + tt <= a[l1])
				{
					if(idx == -1 || (b[l2] < b[idx]))
						idx = l2;
					break;
				}
			}
			if(idx == -1)
			{
				if(c[l1] == 0) ret1++;
				else ret2++;
			}
			else
			{
				d[idx] = 1;
			}
		}
		printf("Case #%d: %d %d\n",l0,ret1,ret2);
	}

}