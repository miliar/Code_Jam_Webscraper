#include <cstdio>
#include <cmath>

using namespace std;

long long s2(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3)
{
	return ((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3));
}

int main()
{
	int t;
	scanf("%d",&t);

	for(int z=1;z<=t;z++)
	{
		int n,m,a;
		scanf("%d%d%d",&n,&m,&a);

		int x2,y2,x3,y3;

		for(x2=0;x2<=n;x2++)
			for(y2=0;y2<=m;y2++)
				for(x3=0;x3<=n;x3++)
					for(y3=0;y3<=m;y3++)
						if( s2(0,0,x2,y2,x3,y3) == a )
						{
							goto out;
						}
out:
		if( x2 == n+1 )
			printf("Case #%d: IMPOSSIBLE\n", z);
		else
			printf("Case #%d: 0 0 %d %d %d %d\n", z, x2, y2, x3, y3);

	}
	return 0;
}