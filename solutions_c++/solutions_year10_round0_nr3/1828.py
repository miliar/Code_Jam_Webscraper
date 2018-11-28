#include <iostream>

using namespace std;

int r, k, n;
int a[2000];
long long b[4000];

long long getSum(int from, int to)
{
	return b[to] - b[from-1];
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d%d", &r, &k, &n);
		for(int i=0;i<n;i++)
		{
			scanf("%d", &a[i]);
		}
		b[0] = 0;
		for(int i=1;i<=2*n+3;i++)
		{
			b[i] = b[i-1] + a[(i-1)%n];
		}
		long long res = 0;
		int cur = 1;
		while(r--)
		{
			int last = cur + n - 1;
			int l = cur, h = last, m;
			while(h - l > 1) 
			{
				int m = (h+l)/2;
				if(getSum(cur, m) > k)
				{
					h = m;
				}
				else 
				{
					l = m;
				}
			}
			if(getSum(cur, h) <= k) 
			{
				m = h;
			}
			else 
			{
				m = l;
			}
			res += getSum(cur, m);
			cur = m+1;
			if(cur > n)
			{
				cur -= n;
			}
		}
		cout<<"Case #"<<tt<<": "<<res<<endl;
	}
	return 0;
}