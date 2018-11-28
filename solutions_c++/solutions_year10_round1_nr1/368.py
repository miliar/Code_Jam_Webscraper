#include<stdio.h>

int T;
int n, K;

char a[111][111];

int Go(char x)
{
	int l1, l2, l3;
	for(l1=0;l1<n;l1++)
	{
		for(l2=0;l2<n;l2++)
		{
			if(a[l1][l2] == x)
			{
				for(l3=0;l3<K;l3++)
				{
					if(l2+l3 >= n) break;
					if(a[l1][l2+l3] != x) break;
				}
				if(l3 == K) return 1;

				for(l3=0;l3<K;l3++)
				{
					if(l1+l3 >= n) break;
					if(a[l1+l3][l2] != x) break;
				}
				if(l3 == K) return 1;

				for(l3=0;l3<K;l3++)
				{
					if(l1+l3 >= n || l2+l3 >= n) break;
					if(a[l1+l3][l2+l3] != x) break;
				}
				if(l3 == K) return 1;
				
				for(l3=0;l3<K;l3++)
				{
					if(l1-l3 < 0 || l2+l3 >= n) break;
					if(a[l1-l3][l2+l3] != x) break;
				}
				if(l3 == K) return 1;
			}
		}
	}
	return 0;
}

int main(void)
{
	int l0, l1, l2, l3;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&K);
		for(l1=0;l1<n;l1++)
		{
			scanf("%s",a[l1]);
		}
		for(l1=0;l1<n;l1++)
		{
			l3 = n-1;
			for(l2=n-1;l2>=0;l2--)
			{
				if(a[l1][l2] != '.')
				{
					a[l1][l3] = a[l1][l2];
					l3--;
				}
			}
			for(l2=l3;l2>=0;l2--) a[l1][l2] = '.';
		}
		int R = Go('R');
		int B = Go('B');

		printf("Case #%d: ",l0);
		if(R&B) printf("Both");
		else if(R) printf("Red");
		else if(B) printf("Blue");
		else printf("Neither");
		printf("\n");
	}

	return 0;
}