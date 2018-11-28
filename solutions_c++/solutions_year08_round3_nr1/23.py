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

#define Max 1100

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("A.in", "r"), *outf = fopen("A.out", "w");

int P, N, L;
int List[ Max];

void input()
{
	int i;
	fscanf(inf, "%d%d%d", &P, &N, &L);

	fr(i, L)
		fscanf(inf, "%d", &List[i]);

	sort(List, List + L);
	reverse(List, List + L);
}

__int64 work()
{
	int i;
	__int64 res = 0, temp;

	fr(i, L)
	{
		temp = (i / N) + 1;
		res += List[i] * temp;
	}

	return res;
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		fprintf(outf, "Case #%d: %I64d\n", i+1, work());
	}

	return 0;
}