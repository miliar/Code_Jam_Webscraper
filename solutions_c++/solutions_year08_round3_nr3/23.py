#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i < b; i++)
#define lod(i, a, b) for(i = a; i > b; i--)

#define pb push_back

#define Max 501000

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("C.in", "r"), *outf = fopen("C.out", "w");

int N, List[ Max], Cmp[ Max], Home[ Max], P;
__int64 Tree[ Max * 5], res;
int MOD = 1000000007;

void input()
{
	int m, i, t;
	__int64 X, Y, Z;
	int st, en, mid;

	fscanf(inf, "%d%d%I64d%I64d%I64d", &N, &m, &X, &Y, &Z);
	X %= Z;
	Y %= Z;

	fr(i, m)
		fscanf(inf, "%d", &List[i]);

	lo(i, m, N)
		List[i] = (List[i - m] * X + Y * (i+1-m)) % Z;

	fr(i, N)
		Cmp[i] = List[i];

	sort(Cmp, Cmp + N);
	t = 0;

	lo(i, 1, N)
	{
		if( Cmp[i] == Cmp[t])
			continue;
		t++;
		Cmp[t] = Cmp[i];
	}

	t++;

	fr(i, N)
	{
		st = 0, en = t-1;

		while(st <= en)
		{
			mid = (st+en) / 2;
			if( Cmp[mid] == List[i])
			{
				Home[i] = mid;
				break;
			}

			if( Cmp[ mid] < List[i])
				st = mid + 1;
			else
				en = mid - 1;
		}
	}

	P = 1;
	while( P < t)
		P *= 2;

	lod(i, P*2-1, 0)
		Tree[i] = 0;
}

__int64 Count( int x)
{
	__int64 res = 0;
	while(x > 1)
	{
		if( x % 2 == 1)
			res += Tree[x-1];
		x /= 2;
	}
	
	return res;
}

void Update(int x)
{
	x /= 2;
	while( x >= 1)
	{
		Tree[ x] = (Tree[x*2] + Tree[x*2+1]) % MOD;
		x /= 2;
	}
}

void work()
{
	int i;
	__int64 H;

	fr(i, N)
	{
		H = (Count( P + Home[i]) + 1) % MOD;
		Tree[ P + Home[i]] = (Tree[ P + Home[i]] + H) % MOD;
		Update( P + Home[i]);
		res = (res + H) % MOD;
	}
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		res = 0;
		work();

		fprintf(outf, "Case #%d: %d\n", i+1, res);
	}

	return 0;
}