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
#define Max 11000

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("A.in", "r"), *outf = fopen("A.out", "w");

int N, M, V;
int Cu[ Max], Best[ Max];

struct Op{
	int ao;
	int change;
} op[ Max];

void input()
{
	int i;

	fscanf(inf, "%d%d", &N, &V);
	M = N / 2;

	lo(i, 1, (M+1))
	{
		fscanf(inf, "%d%d", &op[i].ao, &op[i].change);
	}

	lo(i, (M+1), (N+1))
	{
		fscanf(inf, "%d", &Cu[ i]);
		Best[i] = -1;
	}
}

void work()
{
	int i, j, left, right;
	int x, y, su;

	lod(i, M, 0)
	{
		left = i*2;
		right = i*2+1;

		Cu[i] = (op[i].ao == 0 ? (Cu[ left] | Cu[ right]) : (Cu[ left] & Cu[ right]));
		Best[i] = -1;

		fr(j, 4)
		{
			x = j / 2;
			y = j % 2;

			if(x != Cu[ left] && Best[ left] == -1)
				continue;
			if(y != Cu[ right] && Best[ right] == -1)
				continue;

			su = (x == Cu[ left] ? 0 : Best[ left]) + (y == Cu[ right] ? 0 : Best[ right]);

			if(Cu[i] != (op[i].ao == 0 ? (x | y) : (x & y)))
			{
				if( Best[i] == -1 || su < Best[i])
					Best[i] = su;
			}
		}

		if( op[i].change == 0)
			continue;

		fr(j, 4)
		{
			x = j / 2;
			y = j % 2;

			if(x != Cu[ left] && Best[ left] == -1)
				continue;
			if(y != Cu[ right] && Best[ right] == -1)
				continue;

			su = (x == Cu[ left] ? 0 : Best[ left]) + (y == Cu[ right] ? 0 : Best[ right]) + 1;

			if(Cu[i] != (op[i].ao == 1 ? (x | y) : (x & y)))
			{
				if( Best[i] == -1 || su < Best[i])
					Best[i] = su;
			}
		}
	}
}

void output(int x)
{
	fprintf(outf, "Case #%d:", x);

	if( Cu[1] == V)
		fprintf(outf, " 0\n");
	else
	{
		if( Best[1] == -1)
			fprintf(outf, " IMPOSSIBLE\n");
		else
			fprintf(outf, " %d\n", Best[1]);
	}
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		work();
		output(i+1);
	}
	return 0;
}