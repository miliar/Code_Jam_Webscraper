#include<iostream>
#include<algorithm>
using namespace std;
int gcd(int a, int b)
{
	if(a>=b)
	{
		if(a%b==0)
			return b;
		gcd(b, a%b);
	}
	else
	{
		if(b%a==0)
			return a;
		gcd(a, b%a);
	}
}
int main()
{
	freopen("B.in", "r", stdin);	
	freopen("B.out", "w", stdout);
	int n, k, i, ii, j, p, t[1005]={0}, b, d, c;
	scanf("%d\n", &c);
	for(ii=1; ii<=c; ii++)
	{
		scanf("%d", &n);
		for(i=1; i<=n; i++)
			scanf("%d", &t[i]);
		sort(t+1, t+1+n);
		i=n-1;
		do
		{
			d=t[n]-t[i];
			i--;
		}
		while(d==0 && i>0);
		for(i=n; i>=1; i--)
			for(j=i-1; j>=1; j--)
			{
				b=t[i]-t[j];
				if(b!=0)
				{
					d=gcd(b, d);
				}
			}
		p=(d-t[1]%d)%d;
		printf("Case #%d: %d\n", ii, p);
	}
	return 0;
}