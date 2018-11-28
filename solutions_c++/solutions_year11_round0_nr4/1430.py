#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int t,n,a,g=1;	
	scanf ("%d", &t);
	while (t--)
	{
		int w=0;
		scanf ("%d", &n);
		for (int i=1; i<=n; i++) 
		{
			scanf ("%d", &a);
			if (a!=i) w++;
		}
		printf ("Case #%d: %d.000000\n", g, w);	
		g++;
	}
return 0;
}
