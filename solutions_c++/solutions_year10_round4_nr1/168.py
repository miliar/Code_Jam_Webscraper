#include<stdio.h>

int a[222][222];

int max(int t1, int t2)
{
	if(t1 < t2) return t2;
	return t1;
}

int abs(int x)
{
	if(x < 0) return -x;
	return x;
}

int main(void)
{
	int T;
	int l0, l1, l2, l3, l4, l5, n;
	int t1, t2;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);
	//freopen("input.txt","r",stdin);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		l2 = 0;
		l3 = 0;
		l4 = 0;
		for(l1=0;l1<n*n;l1++)
		{
			scanf("%d",&a[l2][l3]);
			
			l2--;
			l3++;
			if(l2 == -1 || l3 == n)
			{
				l4++;
				l2 = l4;
				if(l2 >= n) l2 = n - 1;
				l3 = l4 - l2;
			}
		}
/*
		for(l1=0;l1<n;l1++)
		{
			for(l2=0;l2<n;l2++)
			{
				printf("%d ",a[l1][l2]);
			}
			printf("\n");
		}
*/
		int ret = 3 * n;

		for(l1=0;l1<=2*n-2;l1++)
		{
			for(l2=1-n;l2<=n-1;l2++)
			{
				
				for(l3=0;l3<n;l3++)
				{
					for(l4=0;l4<n;l4++)
					{
						t1 = l1 - l4;
						t2 = l1 - l3;
						if(0 <= t1 && t1 < n && 0 <= t2 && t2 < n)
						{
							if(a[l3][l4] != a[t1][t2]) goto maki;
						}

						t1 = l4 + l2;
						t2 = l3 - l2;

						if(0 <= t1 && t1 < n && 0 <= t2 && t2 < n)
						{
							if(a[l3][l4] != a[t1][t2]) goto maki;
						}
					}
				}

				t1 = 0;
				t1 = max(t1, abs((l1+l2)-(n-1)*2));
				t1 = max(t1, abs((l1+l2)));
				t1 = max(t1, abs((l1-l2)-(n-1)*2));
				t1 = max(t1, abs((l1-l2)-0));

				if(ret > t1+1) ret = t1 + 1;

maki: ;

			}
		}

		printf("Case #%d: %d\n",l0,ret*ret - n*n);
	}

	return 0;
}