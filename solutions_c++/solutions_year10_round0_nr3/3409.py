#include <iostream>

using namespace std;

int t,i,j,r,k,n,v;
int a[1001],next[1001];
long long s[1001];

int f(int i)
{
	if (i+1 == n+1) return 1;
	return i+1;
}

int main()
{
	freopen("c.in","rt",stdin);
	freopen("c.out","wt",stdout);
	cin >> t;
	for (v = 1;v<=t;v++)
	{
		scanf("%d%d%d",&r,&k,&n);	
		for (i = 1;i<=n;i++)
			scanf("%d",&a[i]);
		for (i = 1;i<=n;i++)
		{
			if (a[i]>k)
			{
				s[i] = 0;
				next[i] = i;
				continue;
			}
			long long sum = a[i];
			j = f(i);
			while (true)
			{
				if (j == i)
				{
					next[i] = i;
					s[i] = sum;
					break;
				}
				else if (sum+a[j]>k)
				{
					next[i] = j;
					s[i] = sum;
					break;
				}
				else
				{
					sum += a[j];
					j = f(j);
				}	
			}
		}
		long long ans = 0;
		int p = 1;
		for (i = 1;i<=r;i++)
		{
			ans += s[p];
			p = next[p];		
		}
		cout << "Case #" << v << ": ";
		cout << ans << endl;
	}
	return 0;
}