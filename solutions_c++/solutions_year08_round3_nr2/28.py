#include<stdio.h>

long long D[111][1111];
char s[111];
int n;

int Get(int l1, int l2, int M)
{
	int l3;
	int ret = 0;
	for(l3=l1;l3<=l2;l3++)
	{
		ret = (ret * 10 + (s[l3] - '0')) % M;
	}
	return ret % M;
}

long long Go(int M)
{
	int l1, l2, l3;

	for(l1=0;l1<n;l1++)
	{
		// itself
		for(l2=0;l2<M;l2++) D[l1][l2] = 0;
		
		D[l1][Get(0, l1, M)] = 1;
		for(l2=0;l2<l1;l2++)
		{
			int v = Get(l2+1, l1, M);

			for(l3=0;l3<M;l3++)
			{
				int x = (l3 + v) % M;
				D[l1][x] += D[l2][l3];

				int y = (l3 - v + M) % M;
				D[l1][y] += D[l2][l3];
			}
		}
	}
	return D[n-1][0];
}

int main(void)
{
	int T;
	int l0, l1, l2, l3;

	freopen("large.in","r",stdin);
	freopen("large.txt","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%s",s);
		for(n=0;s[n];n++);

		long long ret = Go(2) + Go(3) + Go(5) + Go(7) - Go(6) - Go(10) - Go(14) - Go(15) - Go(21) - Go(35) + Go(30) + Go(42) + Go(70) + Go(105) - Go(210);
		printf("Case #%d: %I64d\n",l0,ret);
	}
	return 0;
}