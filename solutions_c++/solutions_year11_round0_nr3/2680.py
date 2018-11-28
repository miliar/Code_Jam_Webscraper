#include <cstdio>
#include <algorithm>
using namespace std;
int T[105];
int main()
{
	int t,n,g=1,y;
	scanf ("%d", &t);
	while (t--)
	{
		int x=0;
		scanf ("%d", &n);
		for (int i=0; i<n; i++) 
		{
			scanf ("%d", &T[i]);
			x=x^T[i];
		}
		if (x!=0) printf ("Case #%d: NO\n", g);
		else
		{
			x=0;
			for (int i=0; i<n; i++) 
			{
				x=x+T[i];
				if (i>0) y=min (y,T[i]);
				else y=T[i];
			}
			printf ("Case #%d: %d\n", g, x-y);
		}
		g++;
		}
return 0;
}
