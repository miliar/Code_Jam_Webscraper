#include <cstdio>
#include <cstdlib>
using namespace std;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i ) 
#define MaxA 2000005

int Tests, n, m, d[15], C, x, y;
int br[MaxA], p;

int main()
{
	int i, k ; 
//	freopen("C1.in", "r", stdin);
//	freopen("C.out", "w", stdout);
	int T = 0;
	for( scanf("%d", &Tests) ; Tests -- ; ) 
	{
		++T;
		printf("Case #%d: ", T);
		scanf("%d%d", &n, &m);
		C = 0;
		rep( i, n, m ) 
		{
			++p;
			x = i;
			d[0] = 0;
			while (x)
			{
				d[++d[0]] = x % 10;
				x =(int) x / 10;
			}
			for (int j = 1; j < d[0]; j++)
			{
				y = 0;
				drep( k, d[0], 1 ) y = y * 10 + d[(k - j - 1 + d[0]) % d[0] + 1];
				if (y > i && y <= m && br[y] != p)
				{
					++C;
					br[y] = p;
				}
			}
		}
		printf("%d\n", C);
	}
	return 0;
}

