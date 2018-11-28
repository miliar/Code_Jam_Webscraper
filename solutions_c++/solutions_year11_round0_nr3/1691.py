#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#define max(a,b) (((a)>(b))?(a):(b))
using namespace std;

int main()
{
	freopen("inp.txt", "r", stdin);
	freopen("outp.txt", "w", stdout);
	int t, n;
	int c[1111];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{	
		scanf("%d", &n);
		int res = 0, val = 1000001;
		long long sum=0;
		for (int j=0;j<n;j++)
		{
			scanf("%d", &c[j]);
			res ^= c[j];
			val = val+c[j]-max(val, c[j]);
			sum += c[j];
		}
		if (!res)
			printf("Case #%d: %lld\n", i, sum-val);
		else
			printf("Case #%d: NO\n", i);
	}
	return 0;
}