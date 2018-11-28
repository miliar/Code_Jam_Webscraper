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
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("C.in", "r"), *outf = fopen("C.out", "w");

int C, R, A;
int Map[ 20][20];
int Best[2][ 10000];
int Upper[20], State[ 20], Plus[20];

void input()
{
	int i, j;
	char temp;
	fscanf(inf, "%d%d", &R, &C);

	A = 0;

	fr(i, R)
	{
		fr(j, C)
		{
			fscanf(inf, "%c", &temp);
			if(temp == '.')
				Map[i][j] = 0;
			else if(temp == 'x')
				Map[i][j] = -1;
			else
				j--;
		}
	}

	Plus[0] = 1;
	lo(i, 1, 10)
		Plus[i] = Plus[i-1]*2;
}

void Upper_work(int x, int su, int i, int j)
{
	if(x == C)
	{
		if( Best[ i][j] < Best[ !i][ su])
			Best[i][j] = Best[!i][su];
		return;
	}

	Upper[x] = 0;
	Upper_work(x+1, su, i, j);
	Upper[x] = 1;

	if( x != 0 && Upper[x-1] == 1)
		return;
	if( x != 0 && State[x-1] == 1)
		return;
	if( x != C-1 && State[x+1] == 1)
		return;

	Upper_work(x+1, su + Plus[x], i, j);
}

void make(int r, int x, int su, bool check)
{
	if(x == C)
	{
		if(!check)
			Best[ r%2][su] = -1;

		else
		{
			int i;
			Best[ r%2][su] = 0;

			if(r != 0)
				Upper_work(0, 0, r%2, su);
			
			fr(i, C)
				Best[ r%2][su] += State[i];

			if(Best[r%2][su] > A)
				A = Best[r%2][su];
		}

		return;
	}

	State[x] = 0;
	make(r, x+1, su, check);
	State[x] = 1;
	if( Map[r][x] != 0)
		check = false;
	if( x != 0 && State[x-1] == 1)
		check = false;

	make(r, x+1, su + Plus[x], check);
}

void work()
{
	int i;

	fr(i, R)
	{
		make(i, 0, 0, true);
	}
}

void output(int x)
{
	fprintf(outf, "Case #%d: %d\n", x, A);
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