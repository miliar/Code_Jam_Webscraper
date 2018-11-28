#include<stdio.h>

int n, m;

char a[111][111];
int b[1111], c[1111][1111];
int P;
int D[111][1111];

int bc[1111];

int BC(int flag)
{
	if(flag == 0) return 0;
	if(flag == 1) return 1;

	return BC(flag & 1) + BC(flag >> 1);
}

int mat(char *s, int flag)
{
	int l1;

	for(l1=0;l1<m;l1++)
	{
		if(flag & (1 << l1))
		{
			if(s[l1] == 'x') return 0;
		}
	}
	return 1;
}

int main(void)
{
	int T;
	int l0, l1, l2, l3, l4;

	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&m);

		for(l1=0;l1<n;l1++) scanf("%s",a[l1]);


		P = (1 << m);
		for(l1=0;l1<P;l1++) b[l1] = 0;
		for(l1=0;l1<P;l1++) for(l2=0;l2<P;l2++) c[l1][l2] = 0;

		for(l1=0;l1<P;l1++)
		{
			for(l2=3;l2<P;l2<<=1)
			{
				if((l1 & l2) == l2)
				{
					b[l1] = 1;
					break;
				}
			}
		}

		for(l1=0;l1<P;l1++)
		{
			if(b[l1]) continue;
			for(l2=0;l2<P;l2++)
			{
				if(b[l2]) continue;

				for(l3=0;l3<m;l3++)
				{
					if((l1 & (1 << l3)) && (l2 & (1 << (l3 + 1))))
					{
						c[l1][l2] = 1;
						break;
					}
					if((l2 & (1 << l3)) && (l1 & (1 << (l3 + 1))))
					{
						c[l1][l2] = 1;
						break;
					}
				}
			}
		}
		for(l1=0;l1<P;l1++) bc[l1] = BC(l1);

		for(l1=0;l1<n;l1++) for(l2=0;l2<P;l2++) D[l1][l2] = 0;

		for(l1=0;l1<P;l1++)
		{
			if(b[l1]) continue;
			if(mat(a[0], l1))
			{
				D[0][l1] = bc[l1];
			}
		}

		for(l1=1;l1<n;l1++)
		{
			for(l2=0;l2<P;l2++)
			{
				if(b[l2]) continue;
				if(!mat(a[l1-1],l2)) continue;
				for(l3=0;l3<P;l3++)
				{
					if(b[l3]) continue;
					if(!mat(a[l1],l3)) continue;
					if(c[l2][l3]) continue;

					int temp = D[l1-1][l2] + bc[l3];
					if(temp > D[l1][l3]) D[l1][l3] = temp;
				}
			}
		}

		int ret = 0;
		for(l1=0;l1<P;l1++) if(ret < D[n-1][l1]) ret = D[n-1][l1];
		printf("Case #%d: %d\n",l0,ret);

	}
}