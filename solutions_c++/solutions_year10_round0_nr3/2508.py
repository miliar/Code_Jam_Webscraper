#include <iostream.h>

int main()
{
	// file streams
//	freopen("C-small.in","r",stdin); freopen("C-small.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small.out","w",stdout);
//	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

	// inputs
	int t;
	int r, k, n;
	int g[11];
	
	// outputs
	int x, y;
	
	// algorithm
	scanf("%d", &t);
	for (x=1; x<=t; x++)
	{	
		// read inputs
		scanf("%d %d %d", &r, &k, &n);
		for (int i=1; i<=n; i++)
			scanf("%d", &g[i]);
		
		// process
		if (n==1)
			y = r * g[1];
		else {
			y = 0;
			int i=1;
			for (int j=1; j<=r; j++)
			{
				int ip=i;
				int yr = 0;		
				while (true)
				{
					int gi = g[i];
					if (yr + gi > k) break;
					yr += gi;
					i++;
					if (i>n) i=1;
					if (i==ip) break;
				}
				y += yr;
			}
		}
		
		// write outputs
		printf("Case #%d: %d\n", x, y);
	}
	
	// end
	return 0;
}