//Arek Wróbel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
#define ST first
#define ND second

int n;
pair<int, int> tab[10000];
int wy;

int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		scanf("%d", &n);
		wy=0;
		for (int a=0; a<n; ++a)
		{
			scanf("%d%d", &tab[a].ST, &tab[a].ND);
			for (int i=0; i<a; ++i)
			{
				if ((tab[a].ST<tab[i].ST)!=(tab[a].ND<tab[i].ND))
					++wy;
			}
		}
		printf("Case #%d: %d\n", lpt, wy);
	}
	return 0;
}
