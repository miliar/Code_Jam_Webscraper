#include<stdio.h>

const int MAXN = 10000000;

long long a[MAXN];
long long b[MAXN];
long long ret;

long long left, right, mid;

int n;
int T;
int C, D;

int Try(long long move)
{
	int l1;

	if(move < 0) return 0;

	b[0] = a[0] - move;
	for(l1=1;l1<n;l1++)
	{
		b[l1] = a[l1] - move;
		if(b[l1] < b[l1-1] + D) b[l1] = b[l1-1] + D;
		if(b[l1] > a[l1] + move) return 0;
	}

	if(ret == -1) ret = move;
	else
	{
		if(move < ret) ret = move;
	}

	return 1;
}

int main(void)
{
	int l0, l1, l2, l3;
	int t1, t2;

	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);

	scanf("%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d\n",l0);
		scanf("%d %d",&C,&D);
		n = 0;
		for(l1=0;l1<C;l1++)
		{
			scanf("%d %d",&t1,&t2);
			for(l2=0;l2<t2;l2++)
			{
				a[n++] = t1;
			}
		}

		for(l1=0;l1<n;l1++)
		{
			a[l1] = a[l1] + a[l1];
		}

		ret = -1;

		left = 1;
		right = 1000000000000000000LL;

		D = D + D;

		while(left < right)
		{
			mid = (left + right) / 2;
			int flag = Try(mid);

			if(flag == 0)
			{
				left = mid + 1;
			}
			else
			{
				right = mid - 1;
			}
		}
		mid = (left + right) / 2;
		Try(mid);
		Try(mid - 1);
		Try(mid + 1);
		Try(mid - 2);
		Try(mid + 2);
		Try(mid - 3);
		Try(mid + 3);
		Try(mid - 4);
		Try(mid + 4);
		Try(mid - 5);
		Try(mid + 5);

		printf("Case #%d: %.10Lf\n",l0,(long double)ret / (long double)2.0);
	}
}