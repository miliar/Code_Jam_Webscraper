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

FILE *inf = fopen("D.in", "r"), *outf = fopen("D.out", "w");

int K, N, res;
int V[ 10];
char str[ 2000], check[ 2000];

void input()
{
	fscanf(inf, "%d %s", &K, str);
	N = strlen(str);
	res = N+1;
}

void work()
{
	int i, j;
	int su = 0;

	fr(i, K)
		V[i] = i;

	check[ N] = 0;

	do{
		for(i = 0; i < N; i += K)
		{
			fr(j, K)
				check[ i+j] = str[i + V[j]]; 
		}

		su = 1;
		lo(i, 1, N)
		{
			if( check[i] != check[i-1])
				su++;
		}

		if(su < res)
			res = su;

	} while( next_permutation( V, V + K));
}

void output(int x)
{
	fprintf(outf, "Case #%d: %d\n", x, res);
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