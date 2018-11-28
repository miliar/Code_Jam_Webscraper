#include <iostream>


const double infin = 1e18;


using namespace std;


int c[1046], v[1046];


bool fail(long long t, int n, int d)
{
	long long leftPosition = -infin;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < v[i]; j++)
		{
			leftPosition += (long long)d;
			if(leftPosition < c[i])
				leftPosition = max(leftPosition, (long long)c[i] - t);
			else
				if(leftPosition - c[i] > t)
					return true;
		}
	}
	return false;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n, d;
		scanf("%d%d", &n, &d);
		d *= 2;
		fprintf(stderr, "%d\n", _);
		for(int i = 0; i < n; i++)
		{
			scanf("%d%d", &c[i], &v[i]);
			c[i] *= 2;
		}
		long long l = 0;
		long long r = 2 * infin;
		while(l < r)
		{
			long long m = (l + r) / 2;
			if(!fail(m, n, d))
				r = m;
			else
				l = m + 1;
		}
		printf("Case #%d: %.9llf\n", _ + 1, (double)l / (double)2);
	}
}