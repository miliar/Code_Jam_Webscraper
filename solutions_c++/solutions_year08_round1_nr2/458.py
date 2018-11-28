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

#define Eps 1e-09
#define Inf 1000

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

//FILE *inf = fopen("b.in", "r"), *outf = stdout;
FILE *inf = fopen("b.in", "r"), *outf = fopen("b.out", "w");

int N, M, Sink, Now[ 30];
int Plus[ 30], num[ 150];
int An, an_num;

void input()
{
	int i, j, t;
	int x, y;

	fscanf(inf, "%d%d", &N, &M);
	Sink = N + N;

	Plus[0] = 1;
	lo(i, 1, Sink)
		Plus[i] = Plus[i-1] * 2;

	fr(i, N)
		Now[i] = 0;

	fr(i, M)
	{
		fscanf(inf, "%d", &t);

		num[i] = 0;

		fr(j, t)
		{
			fscanf(inf, "%d%d", &x, &y);
			x--;

			num[ i] += Plus[ x + y*N];
		}
	}
}

void process(int x, int sel, int sel_s, int res)
{
	if(x == Sink)
	{
		if(sel_s >= an_num || sel != N)
			return;

		int i;

		fr(i, M)
		{
			if( (num[i] & res) == 0)
				return;
		}

		an_num = sel_s;
		An = res;

		return;
	}

	if( N - sel < Sink - x)
		process(x+1, sel, sel_s, res);
	if( N - sel > 0)
	{
		if( x < N || (x >= N && Now[x-N] == 0))
		{			
			Now[x] = 1;
			process(x+1, sel+1, sel_s + (x < N ? 0 : 1), res + Plus[x]);
			Now[x] = 0;
		}
	}
}

void output(int x)
{
	int i;
	vi V(Sink, 0);

	lod(i, (Sink-1), (N-1))
	{
		if( Plus[i] <= An)
			An -= Plus[i], V[ i - N] = 1;
	}

	fprintf(outf, "Case #%d:", x);

	fr(i, N)
		fprintf(outf, " %d", V[i]);
	fprintf(outf, "\n");
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);
	
	fr(i, T)
	{
		input();
		an_num = Sink;
		process(0,0,0,0);	

 		if( an_num != Sink)
			output(i+1);
		else
			fprintf(outf, "Case #%d: IMPOSSIBLE\n", i+1);
	}

	return 0;
}