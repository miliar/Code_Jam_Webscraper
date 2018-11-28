#include<cstdio>
#include<algorithm>
using namespace std;
int t, n, m, a;
bool found;
int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf ("%d", &cases);
	for (int ca = 1; ca <= cases; ++ ca)
	{
		scanf ("%d%d%d", &m, &n , &a);
		found = false;
		printf ("Case #%d: ", ca);
		for (int x = 0; x <= m; ++ x)
			for (int y = 0; y <= n; ++ y)
				for (int xx = 0; xx <= m; ++ xx)
					for (int yy = 0; yy <= n; ++ yy)
						if (abs (x*yy - xx*y) == a)
						{
							printf ("0 0 %d %d %d %d\n", x, y, xx, yy);
							found = true;
							goto finish;
						}
		finish:
		if (!found)	puts ("IMPOSSIBLE");
	}
}