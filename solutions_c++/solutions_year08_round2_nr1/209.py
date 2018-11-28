#include <cstdio>
#include <set>
#include <utility>

#define f(i, n)                         for(int i = 0; i < (long long)(n); i ++)
#define ff(i, st, end)                  for(int i = int(st); i < int(end); i ++)
#define fx(it, v)                       for( typeof( (v).begin() ) it = (v).begin(); it != (v).end; it ++ )
#define fv(i, v)                        for(int i = 0; i < (int)(v).size(); i ++)
#define all(v)                          (v).begin(), (v).end()

int T, t;
int ans;
int n;
long long x0, y0;
long long A, B, C, D, M;
long long x[100005];
long long y[100005];

long long all[3][3];

// std :: set< std :: pair<int,int> > s;

long long solve()
{
	long long res = 0;
	f(x1, 3) f(x2, 3) f(x3, 3) if( (x1 + x2 + x3) % 3LL == 0 )
		f(y1, 3) f(y2, 3) f(y3, 3) if( ( y1 + y2 + y3 ) % 3LL == 0 )
		{
			long long bu = res;
			if( (x1 == x2) && (x1 == x3) && (y1 == y2) && (y1 == y3) )
			{
				res += all[x1][y1] * (all[x1][y1] - 1) * (all[x1][y1] - 2);
//				printf("1 %d %d %d %d %d %d add: %d\n", x1, x2, x3, y1, y2, y3, res - bu);
				continue;
			}
			if( (x1 == x2) && (y1 == y2) )
			{
				res += all[x1][y1] * (all[x1][y1] - 1) * (all[x3][y3]);
//				printf("2 %d %d %d %d %d %d add: %d\n", x1, x2, x3, y1, y2, y3, res - bu);
				continue;
			}
			if( (x1 == x3) && (y1 == y3) ) if( all[x1][y1] > 1 )
			{
				res += all[x1][y1] * (all[x1][y1] - 1) * (all[x2][y2]);
//				printf("3 %d %d %d %d %d %d add: %d\n", x1, x2, x3, y1, y2, y3, res - bu);
				continue;
			}
			if( (x2 == x3) && (y2 == y3) ) if( all[x2][y2] > 1 )
			{
				res += all[x1][y1] * all[x2][y2] * (all[x2][y2] - 1);
//				printf("4 %d %d %d %d %d %d add: %d\n", x1, x2, x3, y1, y2, y3, res - bu);
				continue;
			}
			res += all[x1][y1] * all[x2][y2] * all[x3][y3];
//				printf("5 %d %d %d %d %d %d add: %d\n", x1, x2, x3, y1, y2, y3, res - bu);
		}
	return res;
}

int main()
{
	scanf("%d", &T);
	for(t = 1; t <= T; t ++)
	{
		memset(all, 0, sizeof(all));
//		s.clear();
		scanf("%d", &n);
//		printf("n: %d\n", n);
		scanf("%I64d %I64d %I64d %I64d", &A, &B, &C, &D);
//		printf("n: %d\n", n);
		scanf("%I64d %I64d", &x0, &y0);
//		printf("n: %d %I64d %I64d\n", n, x0, y0);
		scanf("%I64d", &M);
//		printf("n: %d %I64d %I64d\n", n, x0, y0);
		
//		printf("n: %d %I64d %I64d\n", n, x0, y0);
		long long X = x0, Y = y0;
		x[0] = X, y[0] = Y;
//		s.insert(std :: make_pair(x[0], y[0]));
//		printf("%I64d %I64d\n", x[0], y[0]);
		all[X % 3][Y % 3] ++;
		
		for(int i = 1; i < n; i ++)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			x[i] = X; y[i] = Y;
			all[ X % 3 ][ Y % 3 ] ++;
//			s.insert(std :: make_pair(x[i], y[i]));
//			printf("%I64d %I64d\n", x[i], y[i]);
		}
		
//		f(i, 3){ f(j, 3) printf("%I64d", all[i][j]); printf("\n"); }
		
		printf("Case #%d: %I64d\n", t, solve() / 6LL);
	}
    return 0;
}
