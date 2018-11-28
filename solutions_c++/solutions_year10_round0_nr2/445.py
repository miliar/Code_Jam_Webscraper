#include<stdio.h>

int T, C;
int a[10], b[10];

int gcd(int x, int y)
{
	if(x == 0) return y;
	if(x > y) return gcd(y, x);
	return gcd(y%x, x);
}

int main(void)
{
	int l1;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int n;
	scanf("%d",&T);
	for(C=1;C<=T;C++)
	{
		scanf("%d",&n);
		for(l1=0;l1<n;l1++) scanf("%d",&a[l1]);
		int ret = 0;
		for(l1=0;l1+1<n;l1++)
		{
			b[l1] = a[l1] - a[l1+1];
			if(b[l1] < 0) b[l1] = -b[l1];
			
			ret = gcd(ret, b[l1]);
		}
		printf("Case #%d: %d\n",C,(ret - a[0] % ret)%ret);
	}
}