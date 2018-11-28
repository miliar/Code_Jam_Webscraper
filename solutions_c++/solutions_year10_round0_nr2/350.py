#include <iostream>
using namespace std;

int n,i,j,ncase,cases,tmp,ans,ad;
int a[10],d[10];
int gcd(int x, int y)
{
	if (y==0)
		return x;
	else
		return gcd(y,x%y);
}

int main()
{
	freopen("B-small-attempt0.in.txt","r",stdin);
	freopen("B-small-attempt0.out.txt","w",stdout);
	scanf("%d",&cases);
	for (ncase=0; ncase<cases; ncase++)
	{
		scanf("%d",&n);
		for (i=0; i<n; i++)
			scanf("%d",&a[i]);
		for (i=0; i<n; i++)
			for (j=i+1; j<n; j++)
				if (a[i]>a[j])
				{
					tmp = a[i];
					a[i] = a[j];
					a[j] = tmp;
				}
		for (i=0; i<n-1; i++)
			d[i] = a[i+1]-a[i];
		ad = d[0];
		for (i=1; i<n-1; i++)
			ad = gcd(ad,d[i]);
		ans = (ad-a[1]%ad)%ad;
		printf("Case #%d: %d\n",ncase+1,ans);
	}
	return 0;
}
		