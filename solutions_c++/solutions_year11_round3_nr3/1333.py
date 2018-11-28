#include <stdio.h>
#include <algorithm>
#define maxx 110

using namespace std;


int a[maxx],b[maxx],c[maxx],ans;

int gcd(int a,int b)
{
	int temp;
	while(b != 0)
	{
		temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}


int solve(int x,int y,int l,int h)
{
	int temp;
	temp = l % x;
	temp = l - temp;
	if(temp < l) temp += x;
	for(;;)
	{
		if(temp > h || ((temp > y) && ( y != 0))) return -1;
		if(y % temp == 0) return temp;
		temp += x;
	}
}

int main ()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int T,cas,i,nono;

	int n,h,l,temp;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++) scanf("%d",&a[i]);

		sort(a,a+n);

		c[n-1] = a[n-1];
		for(i=n-2;i>=0;i--)
		{
			c[i] = gcd(c[i+1],a[i]);
		}
		c[n] = 0;

		b[0] = a[0];
		nono = n;
		for(i=1;i<n;i++)
		{
			temp = gcd(b[i-1],a[i]);
			b[i] = b[i-1] / temp;
			b[i] *= a[i];
			if(b[i] > h)
			{
				nono = i;
				break;
			}
		}



		ans = solve(1,c[0],l,h);
		i=0;
		while(ans == -1)
		{
			if(i == n || i >= nono) break;
			ans = solve(b[i],c[i+1],l,h);
			i++;
		}

		if(ans == -1)
		{
			printf("Case #%d: NO\n",cas);
		}
		else
		{
			printf("Case #%d: %d\n",cas,ans);
		}
		
	}


}