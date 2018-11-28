#include<stdio.h>

int lim[100000];
int P[100000];
int D[2222][2222];
int C[2222][2222];
int n, m;

int Go(int mat, int minus, int dep)
{
	int left = mat * 2 + 1;
	int right = mat * 2 + 2;

	if(minus < 0) return -1;

	if(dep == m)
	{
		if(lim[mat - (n-1)] - minus < 0) return -1;
		return 0;
	}
	else
	{
		if(C[mat][minus] == 0)
		{
			C[mat][minus] = 1;
			D[mat][minus] = -1;

			int lv, rv;
			lv = Go(left, minus, dep+1);
			rv = Go(right, minus, dep+1);
			if(lv >= 0 && rv >= 0)
			{
				D[mat][minus] = lv + rv + P[mat];
			}

			lv = Go(left, minus+1, dep+1);
			rv = Go(right, minus+1, dep+1);
			if(lv >= 0 && rv >= 0)
			{
				if(D[mat][minus] == -1) D[mat][minus] = lv+rv;
				else if(D[mat][minus] > lv+rv) D[mat][minus] = lv+rv;
			}
		}
		return D[mat][minus];
	}
}

int main(void)
{
	int l0, T;
	int l1, l2, l3;

	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	//freopen("input.txt","r",stdin);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&m);
		n = (1 << m);

		for(l1=0;l1<n;l1++) scanf("%d",&lim[l1]);
		l2 = (n-2)/2;
		l3 = (n-2)/2;
		for(l1=0;l1<n-1;l1++)
		{
			scanf("%d",&P[l2]);
			l2++;
			if(l2 == l3*2+1)
			{
				l3 = (l3 - 1) / 2;
				l2 = l3;
			}
		}

		for(l1=0;l1<2222;l1++) for(l2=0;l2<2222;l2++) D[l1][l2] = C[l1][l2] = 0;

		

		int ret = Go(0, 0, 0);
		for(l1=1;l1<=m;l1++)
		{
			int curr = Go(0, l1, 0);
			if(curr < 0) continue;
			if(curr < ret) ret = curr;
		}
		printf("Case #%d: %d\n",l0,ret);
	}
	return 0;
}