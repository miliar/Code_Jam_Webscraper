#include<stdio.h>

const int INF = 0x7fffffff;

int DC, IC, M, n;
int a[500];
int D[500][1000];
int C[500][1000];
int T;

int opt;

int SNSD(int v1, int v2)
{

	if(v1 > v2) return SNSD(v2, v1);
	if(v1 == v2) return 1;

	if(M == 0)
	{
		return 3000000;
	}

	return (v2 - v1) / M + (!!((v2-v1)%M));
}

int Go(int n, int last)
{
	//printf("[%d,%d]",n,last);
	if(n == 0)
	{
		if(a[0] == last) return 0;

		int curr;
		int best = DC + IC;
		
		if(a[0] == last || M != 0)
		{
			curr = IC * SNSD(a[0], last);
			if(curr < best) best = curr;
		}

		curr = a[0] - last;
		if(curr < 0) curr = -curr;
		if(curr < best) best = curr;
		return best;
	}
	if(C[n][last] == 0)
	{
		int curr, l1, l2;
		C[n][last] = 1;

		D[n][last] = DC * (n + 1) + IC;

		for(l1=1;l1<=n;l1++)
		{
			curr = (n - l1 + 1) * DC + Go(l1-1, last);
			if(D[n][last] > curr) D[n][last] = curr;

			curr = (n - l1 + 1) * DC + IC;
			for(l2=last-M;l2<=last+M;l2++)
			{
				if(l2 < 0 || l2 > 255) continue;
				if(D[n][last] > curr + Go(l1-1,l2))
				{
					D[n][last] = curr + Go(l1-1,l2);
				}
			}
		}

		// normal insert
		if(a[n] == last || M != 0)
		{
			curr = IC * SNSD(a[n], last);
			for(l1=a[n]-M;l1<=a[n]+M;l1++)
			{
				if(l1 < 0 || l1 > 255) continue;
				if(D[n][last] > curr + Go(n-1, l1))
				{
					D[n][last] = curr + Go(n-1, l1);
				}
			}
		}

		// replace
		curr = a[n] - last;
		if(curr < 0) curr = -curr;
		if(curr > DC+IC) curr = DC+IC;
		for(l1=last-M;l1<=last+M;l1++)
		{
			if(l1 < 0 || l1 > 255) continue;
			if(D[n][last] > curr + Go(n-1, l1))
			{
				D[n][last] = curr + Go(n-1, l1);
			}
		}
	}
	return D[n][last];
}

void Try(int x)
{
	if(x < opt) opt = x;
}

int _abs(int x)
{
	if(x < 0) x = -x;
	return x;
}

int Bar(int x, int y, int z)
{
	if(M == 0)
	{
		if(x == y && y == z) return 0;
		return 3000000;
	}
	else
	{
		return (SNSD(x, y) + SNSD(y, z) - 2) * IC;
	}
	return 0;
}

int Foo(int A, int B, int C)
{
	int x, y, z;
	int loc_best = INF;

	for(x=0;x<=255;x++)
	{
		for(y=0;y<=255;y++)
		{
			for(z=0;z<=255;z++)
			{
				int loc_curr = _abs(x-A) + _abs(y-B) + _abs(z-C) + Bar(x,y,z);
				if(loc_best > loc_curr)
					loc_best = loc_curr;
			}
		}
	}
	return loc_best;
}

int Heh(void)
{
	opt = INF;

	if(n == 1)
	{
		Try(Foo(a[0], a[0], a[0]));
	}
	if(n == 2)
	{
		Try(Foo(a[0], a[1], a[1]));
		Try(Foo(a[0], a[0], a[0]) + DC);
		Try(Foo(a[1], a[1], a[1]) + DC);
	}
	if(n == 3)
	{
		Try(Foo(a[0], a[1], a[2]));
		Try(Foo(a[0], a[1], a[1]) + DC);
		Try(Foo(a[1], a[2], a[2]) + DC);
		Try(Foo(a[0], a[2], a[2]) + DC);
		Try(Foo(a[0], a[0], a[0]) + DC+DC);
		Try(Foo(a[1], a[1], a[1]) + DC+DC);
		Try(Foo(a[2], a[2], a[2]) + DC+DC);
	}

	return opt;
}

int main(void)
{
	int l0, l1, l2;
	
	//freopen("input.txt","r",stdin);
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"..%d\n",l0);
		scanf("%d %d %d %d",&DC,&IC,&M,&n);
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);
		
		for(l1=0;l1<n;l1++) for(l2=0;l2<=255;l2++) D[l1][l2] = C[l1][l2] = 0;

		int ret = DC * n;
		for(l1=0;l1<=255;l1++)
		{
			int val = Go(n-1, l1);
			if(val < ret) ret = val;
		}

		int ohmy = Heh();
		if(ret != ohmy)
		{
			fprintf(stderr,"%d.......... %d %d\n",l0,ret,ohmy);
		}

		printf("Case #%d: %d\n",l0,ohmy);
		
		
	}
	return 0;
}