#include <iostream>
#include <fstream>
using namespace std;

bool yes[110];
int x[110];
int v[110];
int T,n,k,b,t;
int main ()
{
	freopen ("input", "r", stdin);
	freopen ("output", "w", stdout);
	
	scanf ("%d", &T);
	for (int cas=1;cas<=T;cas++)
	{
		int res=0;
		scanf("%d%d%d%d", &n, &k, &b, &t); 
		int co=0;
		
		for (int i=1;i<=n;i++)
		{
			scanf ("%d", &x[i]);
			yes[i]=0;
		}
		for (int i=1;i<=n;i++)
			scanf ("%d", &v[i]);
		for (int i=1;i<=n;i++)
		{
			double L=b-x[i];
			double V=v[i];

			if (L/V<=t)
			{
				yes[i]=1;
				co++;
			}
		}

		int bad=0;
		int good=0;
		for (int i=n;i>=1;i--)
		if (good<k)
		{
			if (!yes[i]) bad++;
			else
			{
				res+=bad;
				good++;
			}
		}
		if (good<k)
			printf ("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf ("Case #%d: %d\n", cas, res);
	}

	return 0;
}
